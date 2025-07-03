import abc
import contextlib
import copy
import graphlib
import json
from collections import OrderedDict
from pathlib import Path
from typing import Literal

from docutils import nodes

from fake_bpy_module.analyzer.nodes import (
    ArgumentListNode,
    ArgumentNode,
    AttributeListNode,
    AttributeNode,
    BaseClassListNode,
    BaseClassNode,
    ChildModuleListNode,
    ChildModuleNode,
    ClassNode,
    CodeDocumentNode,
    DataNode,
    DataTypeListNode,
    DataTypeNode,
    DefaultValueNode,
    DependencyListNode,
    DependencyNode,
    DescriptionNode,
    EnumItemListNode,
    EnumItemNode,
    EnumNode,
    FunctionListNode,
    FunctionNode,
    FunctionReturnNode,
    ModuleNode,
    NameNode,
    NodeBase,
)
from fake_bpy_module.utils import (
    find_children,
    get_first_child,
    remove_unencodable,
)

from .code_writer import CodeWriter, CodeWriterIndent
from .translator import CodeDocumentNodeTranslator


def sorted_entry_point_nodes(document: nodes.document) -> list[NodeBase]:
    all_class_nodes: list[ClassNode] = []
    all_function_nodes: list[FunctionNode] = []
    all_data_nodes: list[DataNode] = []
    all_enum_nodes: list[EnumNode] = []
    all_high_priority_class_nodes: list[ClassNode] = []

    class_nodes = find_children(document, ClassNode)
    for class_node in class_nodes:
        class_name = class_node.element(NameNode).astext()
        if class_name in ("bpy_prop_collection", "bpy_prop_collection_idprop",
                          "bpy_prop_array", "bpy_struct"):
            all_high_priority_class_nodes.append(class_node)
        else:
            all_class_nodes.append(class_node)
    all_function_nodes.extend(find_children(document, FunctionNode))
    all_data_nodes.extend(find_children(document, DataNode))
    all_enum_nodes.extend(find_children(document, EnumNode))

    all_class_nodes = all_high_priority_class_nodes \
        + sorted(all_class_nodes, key=lambda n: n.element(NameNode).astext())

    # Sort class data (with class inheritance dependencies)
    class_name_to_node = OrderedDict()
    for class_node in all_class_nodes:
        class_name = class_node.element(NameNode).astext()
        class_name_to_node[class_name] = class_node

    graph = {}
    for class_node in all_class_nodes:
        src_name = class_node.element(NameNode).astext()
        base_class_list_node = class_node.element(BaseClassListNode)
        base_class_nodes = find_children(base_class_list_node, BaseClassNode)

        dst_names = []
        for base_class_node in base_class_nodes:
            dtype_list_node = base_class_node.element(DataTypeListNode)
            dtype_nodes = find_children(dtype_list_node, DataTypeNode)
            dtypes = [dt.astext().replace("`", "") for dt in dtype_nodes]

            dst_names = [dtype for dtype in dtypes
                         if dtype in class_name_to_node]
        graph[src_name] = dst_names

    sorter = graphlib.TopologicalSorter(graph)
    sorted_class_names = list(sorter.static_order())
    sorted_class_nodes = [class_name_to_node[name]
                          for name in sorted_class_names]

    # Sort function data
    sorted_function_nodes = sorted(
        all_function_nodes, key=lambda n: n.element(NameNode).astext())

    # Sort constant data
    sorted_constant_nodes = sorted(
        all_data_nodes, key=lambda n: n.element(NameNode).astext())

    # Sort enum data
    sorted_enum_nodes = sorted(
        all_enum_nodes, key=lambda n: n.element(NameNode).astext())

    # Merge
    sorted_nodes = sorted_enum_nodes
    sorted_nodes.extend(sorted_class_nodes)
    sorted_nodes.extend(sorted_function_nodes)
    sorted_nodes.extend(sorted_constant_nodes)

    return sorted_nodes


def make_union(dtype_nodes: list[DataTypeNode]) -> str:
    types = {n.to_string() for n in set(dtype_nodes)}
    # Only keep float as according to flake8-pyi PIY041
    if "int" in types and "float" in types:
        types.remove("int")
    return ' | '.join(sorted(types))


class BaseWriter(metaclass=abc.ABCMeta):
    def __init__(self) -> None:
        self.file_format = ""

    @abc.abstractmethod
    def write(self, filename: str, document: nodes.document,
              style_config: str = 'ruff') -> None:
        raise NotImplementedError


class PyCodeWriterBase(BaseWriter):
    def __init__(self) -> None:
        super().__init__()

        self._writer: CodeWriter = CodeWriter()
        self.ellipsis_strings = {
            "constant": " = None",
            "function": "pass",
            "attribute": " = None",
            "method": "pass",
            "class": "pass"
        }
        self.file_format = "py"

    def _is_accept_none(self, node: DataTypeNode, variable_kind: str) -> bool:
        node_attrs = node.attributes
        if variable_kind == 'FUNC_ARG':
            if "option" not in node_attrs:
                return False
            return "never none" not in node_attrs["option"]
        if variable_kind == 'FUNC_RET':
            if "option" not in node_attrs:
                return False
            return "accept none" in node_attrs["option"]
        if variable_kind == 'CLS_ATTR':
            if "option" not in node_attrs:
                return False
            return ("accept none" in node_attrs["option"] or
                    "never none" not in node_attrs["option"])

        return False

    # pylint: disable=R0912
    def _write_function_code(self, func_node: FunctionNode) -> None:
        func_name = func_node.element(NameNode).astext()
        arg_nodes = find_children(
            func_node.element(ArgumentListNode), ArgumentNode)
        return_node = func_node.element(FunctionReturnNode)

        wt = self._writer

        gen_types = ""
        if "generic-types" in func_node.attributes:
            gen_types = f"[{func_node.attributes['generic-types']}]"
        wt.add(f"def {func_name}{gen_types}(")

        current_status: Literal['NONE', 'POSONLYARG', 'ARG', 'KWONLYARG'] = 'NONE'
        for i, arg_node in enumerate(arg_nodes):
            arg_name = arg_node.element(NameNode).astext()
            dtype_list_node = arg_node.element(DataTypeListNode)
            default_value_node = arg_node.element(DefaultValueNode)

            arg_type = arg_node.attributes["argument_type"]
            is_arg = arg_type in ("arg", "kwarg", "vararg")
            is_posonlyarg = arg_type == "posonlyarg"
            is_kwonlyarg = arg_type == "kwonlyarg"
            if current_status == 'NONE':
                if is_posonlyarg:
                    current_status = 'POSONLYARG'
                elif is_arg:
                    current_status = 'ARG'
                elif is_kwonlyarg:
                    current_status = 'KWONLYARG'
                    wt.add("*, ")
                else:
                    raise ValueError("Invalid Current Status: "
                                     f"{current_status} ({arg_type})")
            elif current_status == 'POSONLYARG':
                if is_posonlyarg:
                    pass    # Do nothing.
                elif is_arg:
                    current_status = 'ARG'
                    wt.add("/, ")
                elif is_kwonlyarg:
                    current_status = 'KWONLYARG'
                    wt.add("/, ")
                    wt.add("*, ")
                else:
                    raise ValueError("Invalid Current Status: "
                                     f"{current_status} ({arg_type})")
            elif current_status == 'ARG':
                if is_arg:
                    pass    # Do nothing.
                elif is_kwonlyarg:
                    current_status = 'KWONLYARG'
                    wt.add("*, ")
                else:
                    raise ValueError("Invalid Current Status: "
                                     f"{current_status} ({arg_type})")

            if arg_node.attributes["argument_type"] == "vararg":
                arg_name = f"*{arg_name}"
            elif arg_node.attributes["argument_type"] == "kwarg":
                arg_name = f"**{arg_name}"

            if not dtype_list_node.empty():
                dtype_nodes = find_children(dtype_list_node, DataTypeNode)
                dtype_str = make_union(dtype_nodes)
                for dtype_node in dtype_nodes:
                    if self._is_accept_none(dtype_node, 'FUNC_ARG'):
                        dtype_str = f"{dtype_str} | None"
                        break

                if not default_value_node.empty():
                    wt.add(f"{arg_name}: {dtype_str}="
                           f"{default_value_node.astext()}")
                else:
                    wt.add(f"{arg_name}: {dtype_str}")
            elif not default_value_node.empty():
                wt.add(f"{arg_name}={default_value_node.astext()}")
            else:
                wt.add(f"{arg_name}")

            if i != len(arg_nodes) - 1:
                wt.add(", ")
        if return_node.empty():
            wt.addln(") -> None:")
        else:
            dtype_list_node = return_node.element(DataTypeListNode)
            if not dtype_list_node.empty():
                dtype_nodes = find_children(dtype_list_node, DataTypeNode)
                dtype = make_union(dtype_nodes)
                for dtype_node in dtype_nodes:
                    if self._is_accept_none(dtype_node, 'FUNC_RET'):
                        dtype = f"{dtype} | None"
                        break
                wt.addln(f") -> {dtype}:")
            else:
                wt.addln(") -> None:")

        desc_node = func_node.element(DescriptionNode)
        if "deprecated" in func_node.attributes:
            desc_node.insert(0, nodes.Text(func_node.attributes["deprecated"]))

        with CodeWriterIndent(1):
            # documentation
            if (
                not desc_node.empty()
                or any(
                    n.element(DescriptionNode).empty() == ""
                    or not n.element(DataTypeListNode).empty()
                    for n in arg_nodes
                )
                or not return_node.empty()
            ):
                wt.add(f"''' {desc_node.astext()}")
                wt.new_line(2)
                for arg_node in arg_nodes:
                    name_node = arg_node.element(NameNode)
                    desc_node = arg_node.element(DescriptionNode)
                    dtype_list_node = arg_node.element(DataTypeListNode)
                    if not desc_node.empty():
                        wt.addln(f":param {name_node.astext()}: "
                                 f"{desc_node.astext()}")
                    if not dtype_list_node.empty():
                        dtype_nodes = find_children(dtype_list_node,
                                                    DataTypeNode)
                        dtype_str = make_union(dtype_nodes)
                        for dtype_node in dtype_nodes:
                            if self._is_accept_none(dtype_node, 'FUNC_ARG'):
                                dtype_str = f"{dtype_str} | None"
                                break
                        wt.addln(f":type {name_node.astext()}: {dtype_str}")
                if not return_node.empty():
                    desc_node = return_node.element(DescriptionNode)
                    dtype_list_node = return_node.element(DataTypeListNode)
                    if not desc_node.empty():
                        wt.addln(f":return: {desc_node.astext()}")
                    if not dtype_list_node.empty():
                        dtype_nodes = find_children(dtype_list_node,
                                                    DataTypeNode)
                        dtype = make_union(dtype_nodes)
                        for dtype_node in dtype_nodes:
                            if self._is_accept_none(dtype_node, 'FUNC_RET'):
                                dtype = f"{dtype} | None"
                                break
                        wt.addln(f":rtype: {dtype}")
                wt.addln("'''")
            else:
                wt.addln(self.ellipsis_strings["function"])
            wt.new_line(2)

    # pylint: disable=R0914,R0915
    def _write_class_code(self, class_node: ClassNode) -> None:
        wt = self._writer

        base_class_list_node = class_node.element(BaseClassListNode)
        name_node = class_node.element(NameNode)
        desc_node = class_node.element(DescriptionNode)
        attr_nodes = find_children(class_node.element(AttributeListNode),
                                   AttributeNode)
        method_nodes = find_children(class_node.element(FunctionListNode),
                                     FunctionNode)

        gen_types = ""
        if "generic-types" in class_node.attributes:
            gen_types = f"[{class_node.attributes['generic-types']}]"

        if base_class_list_node.empty():
            wt.addln(f"class {name_node.astext()}{gen_types}:")
        else:
            base_class_nodes = find_children(base_class_list_node,
                                             BaseClassNode)
            dtypes = []
            for base_class_node in base_class_nodes:
                dtype_list_node = base_class_node.element(DataTypeListNode)
                if not dtype_list_node.empty():
                    dtype_nodes = find_children(dtype_list_node, DataTypeNode)
                    if len(dtype_nodes) >= 2:
                        dtype = ' | '.join(n.to_string() for n in dtype_nodes)
                    else:
                        dtype = dtype_nodes[0].to_string()
                    dtypes.append(dtype)
            # bpy_prop_collection must be higher priority than bpy_struct.
            bpy_struct_index = -1
            bpy_prop_collection_index = -1
            for i, dtype in enumerate(dtypes):
                if dtype == "bpy_struct":
                    bpy_struct_index = i
                elif dtype.startswith("bpy_prop_collection["):
                    bpy_prop_collection_index = i
            if (bpy_struct_index != -1) and (bpy_prop_collection_index != -1):
                tmp = dtypes[bpy_struct_index]
                dtypes[bpy_struct_index] = dtypes[bpy_prop_collection_index]
                dtypes[bpy_prop_collection_index] = tmp
            wt.addln(f"class {name_node.astext()}{gen_types}"
                     f"({', '.join(dtypes)}):")

        with CodeWriterIndent(1):
            if not desc_node.empty():
                wt.addln(f"''' {desc_node.astext()}")
                wt.addln("'''")
                wt.new_line(1)

            for attr_node in attr_nodes:
                name_node = attr_node.element(NameNode)
                dtype_list_node = attr_node.element(DataTypeListNode)
                desc_node = attr_node.element(DescriptionNode)
                if "deprecated" in attr_node.attributes:
                    desc_node.insert(
                        0, nodes.Text(attr_node.attributes["deprecated"]))

                dtype_str = None
                if not dtype_list_node.empty():
                    dtype_nodes = find_children(dtype_list_node, DataTypeNode)
                    dtype_str = make_union(dtype_nodes)
                    for dtype_node in dtype_nodes:
                        if self._is_accept_none(dtype_node, 'CLS_ATTR'):
                            dtype_str = f"{dtype_str} | None"
                            break

                if dtype_str is not None:
                    wt.addln(f"{name_node.astext()}: {dtype_str}"
                             f"{self.ellipsis_strings['attribute']}")
                else:
                    wt.addln(f"{name_node.astext()}: typing.Any"
                             f"{self.ellipsis_strings['attribute']}")

                if (not desc_node.empty()) or (dtype_str is not None):
                    wt.add("''' ")
                    if not desc_node.empty():
                        wt.add(f"{desc_node.astext()}")
                    if dtype_str is not None:
                        wt.new_line(2)
                        wt.addln(f":type: {dtype_str}")
                    wt.addln("'''")
                    wt.new_line(1)
            if len(attr_nodes) > 0:
                wt.new_line(1)

            for method_node in method_nodes:
                func_type = method_node.attributes["function_type"]
                arg_list_node = method_node.element(ArgumentListNode)
                name_node = method_node.element(NameNode)

                if "option" in method_node.attributes:
                    if method_node.attributes["option"] == "overload":
                        wt.addln("@typing.overload")

                gen_types = ""
                if "generic-types" in method_node.attributes:
                    gen_types = f"[{method_node.attributes['generic-types']}]"
                if func_type in ("function", "method"):
                    if not arg_list_node.empty():
                        wt.add(f"def {name_node.astext()}{gen_types}(self, ")
                    else:
                        wt.add(f"def {name_node.astext()}{gen_types}(self")
                elif func_type == "classmethod":
                    if not arg_list_node.empty():
                        wt.addln("@classmethod")
                        wt.add(f"def {name_node.astext()}{gen_types}(cls, ")
                    else:
                        wt.addln("@classmethod")
                        wt.add(f"def {name_node.astext()}{gen_types}(cls")
                elif func_type == "staticmethod":
                    if not arg_list_node.empty():
                        wt.addln("@staticmethod")
                        wt.add(f"def {name_node.astext()}{gen_types}(")
                    else:
                        wt.addln("@staticmethod")
                        wt.add(f"def {name_node.astext()}{gen_types}(")
                else:
                    raise NotImplementedError(
                        f"func_type={func_type} is not supported")

                arg_nodes = find_children(arg_list_node, ArgumentNode)
                start_kwarg = False
                for i, arg_node in enumerate(arg_nodes):
                    arg_name = arg_node.element(NameNode).astext()
                    dtype_list_node = arg_node.element(DataTypeListNode)
                    default_value_node = arg_node.element(DefaultValueNode)

                    is_kwonlyarg = (
                        arg_node.attributes["argument_type"] == "kwonlyarg"
                    )
                    if not start_kwarg and is_kwonlyarg:
                        wt.add("*, ")
                        start_kwarg = True

                    if arg_node.attributes["argument_type"] == "vararg":
                        arg_name = f"*{arg_name}"
                    elif arg_node.attributes["argument_type"] == "kwarg":
                        arg_name = f"**{arg_name}"

                    if not dtype_list_node.empty():
                        dtype_nodes = find_children(dtype_list_node,
                                                    DataTypeNode)
                        dtype_str = make_union(dtype_nodes)
                        for dtype_node in dtype_nodes:
                            if self._is_accept_none(dtype_node, 'FUNC_ARG'):
                                dtype_str = f"{dtype_str} | None"
                                break

                        if not default_value_node.empty():
                            wt.add(f"{arg_name}: {dtype_str}="
                                   f"{default_value_node.astext()}")
                        else:
                            wt.add(f"{arg_name}: {dtype_str}")
                    elif not default_value_node.empty():
                        wt.add(f"{arg_name}="
                               f"{default_value_node.astext()}")
                    else:
                        wt.add(arg_name)

                    if i != len(arg_nodes) - 1:
                        wt.add(", ")

                return_node = method_node.element(FunctionReturnNode)
                if return_node.empty():
                    wt.addln(") -> None:")
                else:
                    dtype_list_node = return_node.element(DataTypeListNode)
                    if not dtype_list_node.empty():
                        dtype_nodes = find_children(dtype_list_node,
                                                    DataTypeNode)
                        dtype = make_union(dtype_nodes)
                        for dtype_node in dtype_nodes:
                            if self._is_accept_none(dtype_node, 'FUNC_RET'):
                                dtype = f"{dtype} | None"
                                break
                        wt.addln(f") -> {dtype}:")
                    else:
                        wt.addln(") -> None:")

                desc_node = method_node.element(DescriptionNode)
                with CodeWriterIndent(2):
                    # documentation
                    if (
                        not desc_node.empty()
                        or not arg_list_node.empty()
                        or not return_node.empty()
                    ):
                        wt.addln(f"''' {desc_node.astext()}")
                        wt.new_line(1)

                        arg_nodes = find_children(arg_list_node, ArgumentNode)
                        for arg_node in arg_nodes:
                            name_node = arg_node.element(NameNode)
                            desc_node = arg_node.element(DescriptionNode)
                            dtype_list_node = arg_node.element(DataTypeListNode)
                            wt.addln(f":param {name_node.astext()}: "
                                     f"{desc_node.astext()}")
                            if not dtype_list_node.empty():
                                dtype_nodes = find_children(
                                    dtype_list_node, DataTypeNode)
                                dtype_str = make_union(dtype_nodes)
                                for dtype_node in dtype_nodes:
                                    if self._is_accept_none(
                                            dtype_node, 'FUNC_ARG'):
                                        dtype_str = f"{dtype_str} | None"
                                        break
                                wt.addln(f":type {name_node.astext()}: "
                                         f"{dtype_str}")

                        if not return_node.empty():
                            desc_node = return_node.element(DescriptionNode)
                            dtype_list_node = return_node.element(
                                DataTypeListNode)

                            wt.addln(f":return: {desc_node.astext()}")

                            if not dtype_list_node.empty():
                                dtype_nodes = find_children(dtype_list_node,
                                                            DataTypeNode)
                                dtype = make_union(dtype_nodes)
                                for dtype_node in dtype_nodes:
                                    if self._is_accept_none(
                                            dtype_node, 'FUNC_RET'):
                                        dtype = f"{dtype} | None"
                                        break
                                wt.addln(f":rtype: {dtype}")
                        wt.addln("'''")
                    else:
                        wt.addln(self.ellipsis_strings["method"])
                    wt.new_line()

            if (len(attr_nodes) == 0
                    and len(method_nodes) == 0
                    and desc_node.empty()):
                wt.addln(self.ellipsis_strings["class"])
                wt.new_line(2)

    def _write_constant_code(self, data_node: DataNode) -> None:
        wt = self._writer

        name_node = data_node.element(NameNode)
        dtype_list_node = data_node.element(DataTypeListNode)
        desc_node = data_node.element(DescriptionNode)
        if "deprecated" in data_node.attributes:
            desc_node.insert(0, nodes.Text(data_node.attributes["deprecated"]))

        if not dtype_list_node.empty():
            dtype_nodes = find_children(dtype_list_node, DataTypeNode)
            dtype = make_union(dtype_nodes)
            for dtype_node in dtype_nodes:
                node_attrs = dtype_node.attributes
                if "option" not in node_attrs:
                    continue
                if ("accept none" in node_attrs["option"] or
                        "never none" not in node_attrs["option"]):
                    dtype = f"{dtype} | None"
                    break
            wt.addln(f"{name_node.astext()}: {dtype}"
                     f"{self.ellipsis_strings['constant']}")
        else:
            wt.addln(f"{name_node.astext()}: typing.Any"
                     f"{self.ellipsis_strings['constant']}")
        if not desc_node.empty():
            wt.addln(f"''' {remove_unencodable(desc_node.astext())}")
            wt.addln("'''")
        wt.new_line(2)

    def _write_enum_code(self, enum_node: EnumNode) -> None:
        wt = self._writer

        enum_name = enum_node.element(NameNode).astext()
        enum_item_list_node = enum_node.element(EnumItemListNode)
        enum_item_nodes = find_children(enum_item_list_node, EnumItemNode)

        enum_item_strs = []
        for enum_item_node in enum_item_nodes:
            enum_item_name = enum_item_node.element(NameNode).astext()
            enum_item_desc = enum_item_node.element(DescriptionNode).astext()
            enum_item_desc = enum_item_desc.replace("\n", "")
            if len(enum_item_desc) != 0:
                enum_item_strs.append(f"'{enum_item_name}',"
                                      f"  # {enum_item_desc}")
            else:
                enum_item_strs.append(f"'{enum_item_name}',")

        enum_item_strs_lines = "\n".join(enum_item_strs)
        wt.addln(f"type {enum_name} = typing.Literal[\n"
                 f"{enum_item_strs_lines}\n]")

    def write(self, filename: str, document: nodes.document,
              style_config: str = 'ruff') -> None:
        # At first, sort data to avoid generating large diff.
        # Note: Base class must be located above derived class
        sorted_data = sorted_entry_point_nodes(document)

        with Path(f"{filename}.{self.file_format}").open(
                "w", encoding="utf-8", newline="\n") as file:
            wt = self._writer
            wt.reset()

            code_doc_nodes = find_children(document, CodeDocumentNode)
            doc_writer = CodeWriter()
            visitor = CodeDocumentNodeTranslator(document, doc_writer)
            for node in code_doc_nodes:
                node.walkabout(visitor)
            wt.addln(doc_writer.get_data_as_string())

            # import external depended modules
            wt.addln("import typing")
            wt.addln("import collections.abc")
            wt.addln("import typing_extensions")
            wt.addln("import numpy.typing as npt")

            # import depended modules
            dep_list_node = get_first_child(document, DependencyListNode)
            dependencies = []
            if dep_list_node is not None:
                dep_nodes = find_children(dep_list_node, DependencyNode)
                dependencies = [node.astext() for node in dep_nodes]
                for dep in sorted(dependencies):
                    wt.addln(f"import {dep}")
            if len(dependencies) > 0:
                wt.new_line()

            # import child module to search child modules
            child_list_node = get_first_child(document, ChildModuleListNode)
            children = []
            if child_list_node is not None:
                child_nodes = find_children(child_list_node, ChildModuleNode)
                children = [node.astext() for node in child_nodes]
                module_name = get_first_child(
                    get_first_child(document, ModuleNode), NameNode).astext()

                # Skip typing module as it is not available at runtime
                with contextlib.suppress(ValueError):
                    children.remove("stub_internal")
                # Skip import layout from bl_ui_utils module
                with contextlib.suppress(ValueError):
                    if module_name == "bl_ui_utils":
                        children.remove("layout")

                for child in sorted(children):
                    wt.addln(f"from . import {child} as {child}")
            if len(children) > 0:
                wt.new_line()

            if (len(dependencies) > 0) or (len(children) > 0):
                wt.new_line()

            # for generic type
            wt.new_line()

            for node in sorted_data:
                if isinstance(node, FunctionNode):
                    self._write_function_code(node)
                elif isinstance(node, ClassNode):
                    self._write_class_code(node)
                elif isinstance(node, DataNode):
                    self._write_constant_code(node)
                elif isinstance(node, EnumNode):
                    self._write_enum_code(node)

            wt.format(style_config, self.file_format)
            wt.write(file)


class PyCodeWriter(PyCodeWriterBase):
    def __init__(self) -> None:
        super().__init__()

        self.ellipsis_strings = {
            "constant": " = None",
            "function": "pass",
            "attribute": " = None",
            "method": "pass",
            "class": "pass"
        }
        self.file_format = "py"


class PyInterfaceWriter(PyCodeWriterBase):
    def __init__(self) -> None:
        super().__init__()

        self.ellipsis_strings = {
            "constant": "",
            "function": "...",
            "attribute": "",
            "method": "...",
            "class": "..."
        }
        self.file_format = "pyi"


class JsonWriter(BaseWriter):
    def __init__(self) -> None:
        super().__init__()

        self.file_format = "json"

    def _clean_node_attributes(self, attributes: dict) -> dict:
        cleaned = copy.deepcopy(attributes)

        keys_to_remove = ("ids", "classes", "names", "dupnames", "backrefs")
        for key in keys_to_remove:
            if key in cleaned:
                del cleaned[key]

        return cleaned

    def _create_function_json_data(self, func_node: FunctionNode) -> dict:
        func_data = {
            "type": "function",
            "name": func_node.element(NameNode).astext(),
            "description": func_node.element(DescriptionNode).astext(),
            "arguments": [],
            "return": {},
            "options": self._clean_node_attributes(func_node.attributes),
        }

        arg_nodes = find_children(func_node.element(ArgumentListNode),
                                  ArgumentNode)
        for arg_node in arg_nodes:
            arg_data = {
                "name": arg_node.element(NameNode).astext(),
                "description": arg_node.element(DescriptionNode).astext(),
                "data_types": [],
                "default_value": arg_node.element(DefaultValueNode).astext()
            }
            dtype_nodes = find_children(arg_node.element(DataTypeListNode),
                                        DataTypeNode)
            for dtype_node in dtype_nodes:
                dtype_data = {
                    "data_type": dtype_node.to_string(),
                    "options": self._clean_node_attributes(
                        dtype_node.attributes),
                }
                arg_data["data_types"].append(dtype_data)
            func_data["arguments"].append(arg_data)

        ret_node = func_node.element(FunctionReturnNode)
        func_data["return"] = {
            "description": ret_node.element(DescriptionNode).astext(),
            "data_types": [],
        }
        dtype_nodes = find_children(ret_node.element(DataTypeListNode),
                                    DataTypeNode)
        for dtype_node in dtype_nodes:
            dtype_data = {
                "data_type": dtype_node.to_string(),
                "options": self._clean_node_attributes(dtype_node.attributes),
            }
            func_data["return"]["data_types"].append(dtype_data)

        return func_data

    def _create_constant_json_data(self, data_node: DataNode) -> dict:
        data_data = {
            "type": "data",
            "name": data_node.element(NameNode).astext(),
            "description": data_node.element(DescriptionNode).astext(),
            "data_types": [],
            "options": self._clean_node_attributes(data_node.attributes),
        }

        dtype_nodes = find_children(data_node.element(DataTypeListNode),
                                    DataTypeNode)
        for dtype_node in dtype_nodes:
            dtype_data = {
                "data_type": dtype_node.to_string(),
                "options": self._clean_node_attributes(dtype_node.attributes),
            }
            data_data["data_types"].append(dtype_data)

        return data_data

    def _create_enum_json_data(self, enum_node: EnumNode) -> dict:
        enum_data = {
            "type": "enum",
            "name": enum_node.element(NameNode).astext(),
            "description": enum_node.element(DescriptionNode).astext(),
            "enum_items": [],
            "options": self._clean_node_attributes(enum_node.attributes),
        }

        enum_item_nodes = find_children(enum_node.element(EnumItemListNode),
                                        EnumItemNode)
        for enum_item_node in enum_item_nodes:
            enum_item_data = {
                "name": enum_item_node.element(NameNode).astext(),
                "description": enum_item_node.element(DescriptionNode).astext(),
                "options": self._clean_node_attributes(
                    enum_item_node.attributes),
            }
            enum_data["enum_items"].append(enum_item_data)

        return enum_data

    def _create_class_json_data(self, class_node: ClassNode) -> dict:
        class_data = {
            "type": "class",
            "name": class_node.element(NameNode).astext(),
            "description": class_node.element(DescriptionNode).astext(),
            "base_classes": [],
            "attributes": [],
            "methods": [],
            "options": self._clean_node_attributes(class_node.attributes),
        }

        base_class_nodes = find_children(class_node.element(BaseClassListNode),
                                         BaseClassNode)
        for base_class_node in base_class_nodes:
            base_class_data = {
                "data_types": [],
            }
            dtype_nodes = find_children(
                base_class_node.element(DataTypeListNode), DataTypeNode)
            for dtype_node in dtype_nodes:
                dtype_data = {
                    "data_type": dtype_node.to_string(),
                    "options": self._clean_node_attributes(
                        dtype_node.attributes),
                }
                base_class_data["data_types"].append(dtype_data)
            class_data["base_classes"].append(base_class_data)

        attr_nodes = find_children(class_node.element(AttributeListNode),
                                   AttributeNode)
        for attr_node in attr_nodes:
            attr_data = self._create_constant_json_data(attr_node)
            del attr_data["type"]
            class_data["attributes"].append(attr_data)

        method_nodes = find_children(class_node.element(FunctionListNode),
                                     FunctionNode)
        for method_node in method_nodes:
            method_data = self._create_function_json_data(method_node)
            del method_data["type"]
            class_data["methods"].append(method_data)

        return class_data

    def write(self, filename: str, document: nodes.document,
              style_config: str = 'none') -> None:  # noqa: ARG002
        sorted_data = sorted_entry_point_nodes(document)

        json_data = []

        code_doc_nodes = find_children(document, CodeDocumentNode)
        doc_writer = CodeWriter()
        visitor = CodeDocumentNodeTranslator(document, doc_writer)
        for node in code_doc_nodes:
            node.walkabout(visitor)
        json_data.append({
            "type": "code-document",
            "contents": doc_writer.get_data_as_string(),
        })

        # import external depended modules
        json_data.append({
            "type": "external-depended-modules",
            "contents": [
                "typing",
                "collections.abc",
                "typing_extensions",
                "numpy.typing",
            ],
        })

        # import depended modules
        dep_list_node = get_first_child(document, DependencyListNode)
        dependencies = []
        if dep_list_node is not None:
            dep_nodes = find_children(dep_list_node, DependencyNode)
            dependencies = [node.astext() for node in dep_nodes]
        json_data.append({
            "type": "internal-depended-modules",
            "contents": dependencies,
        })

        # import child module to search child modules
        child_list_node = get_first_child(document, ChildModuleListNode)
        children = []
        if child_list_node is not None:
            child_nodes = find_children(child_list_node, ChildModuleNode)
            children = [node.astext() for node in child_nodes]
        json_data.append({
            "type": "child-modules",
            "contents": children,
        })

        # for generic type
        json_data.append({
            "type": "code",
            "contents": []
        })

        for node in sorted_data:
            if isinstance(node, ClassNode):
                json_data.append(self._create_class_json_data(node))
            elif isinstance(node, FunctionNode):
                json_data.append(self._create_function_json_data(node))
            elif isinstance(node, DataNode):
                json_data.append(self._create_constant_json_data(node))
            elif isinstance(node, EnumNode):
                json_data.append(self._create_enum_json_data(node))

        with Path(f"{filename}.{self.file_format}").open(
                "w", newline="\n", encoding="utf-8") as f:
            json.dump(json_data, f, indent=4)
