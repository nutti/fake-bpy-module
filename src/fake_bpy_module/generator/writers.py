import abc
import copy
import graphlib
import json
from typing import List
from collections import OrderedDict
from docutils import nodes

from ..analyzer.nodes import (
    NameNode,
    ClassNode,
    FunctionListNode,
    FunctionNode,
    DataNode,
    DataTypeListNode,
    DataTypeNode,
    ArgumentListNode,
    ArgumentNode,
    FunctionReturnNode,
    AttributeListNode,
    AttributeNode,
    BaseClassListNode,
    BaseClassNode,
    NodeBase,
    DefaultValueNode,
    DescriptionNode,
    ChildModuleListNode,
    ChildModuleNode,
    DependencyListNode,
    DependencyNode,
    CodeDocumentNode,
)
from .code_writer import CodeWriter, CodeWriterIndent
from .translator import CodeDocumentNodeTranslator
from ..utils import find_children, get_first_child, remove_unencodable


def sorted_entry_point_nodes(document: nodes.document) -> List[NodeBase]:
    all_class_nodes: List[ClassNode] = []
    all_function_nodes: List[FunctionNode] = []
    all_data_nodes: List[DataNode] = []
    all_high_priority_class_nodes: List[ClassNode] = []

    class_nodes = find_children(document, ClassNode)
    for class_node in class_nodes:
        class_name = class_node.element(NameNode).astext()
        if class_name in ("bpy_prop_collection", "bpy_prop_array", "bpy_struct"):
            all_high_priority_class_nodes.append(class_node)
        else:
            all_class_nodes.append(class_node)
    all_function_nodes.extend(find_children(document, FunctionNode))
    all_data_nodes.extend(find_children(document, DataNode))

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

            for dtype in dtypes:
                if dtype in class_name_to_node:
                    dst_names.append(dtype)
        graph[src_name] = dst_names

    sorter = graphlib.TopologicalSorter(graph)
    sorted_class_names = list(sorter.static_order())
    sorted_class_nodes = [class_name_to_node[name] for name in sorted_class_names]

    # Sort function data
    sorted_function_nodes = sorted(
        all_function_nodes, key=lambda n: n.element(NameNode).astext())

    # Sort constant data
    sorted_constant_nodes = sorted(
        all_data_nodes, key=lambda n: n.element(NameNode).astext())

    # Merge
    sorted_nodes = sorted_class_nodes
    sorted_nodes.extend(sorted_function_nodes)
    sorted_nodes.extend(sorted_constant_nodes)

    return sorted_nodes


def make_union(dtype_nodes: List[DataTypeNode]) -> str:
    return ' | '.join(sorted({n.to_string() for n in set(dtype_nodes)}))


class BaseWriter(metaclass=abc.ABCMeta):
    def __init__(self):
        self.file_format = ""

    @abc.abstractmethod
    def write(self, filename: str, document: nodes.document, style_config: str = 'ruff'):
        raise NotImplementedError()


class PyCodeWriterBase(BaseWriter):
    def __init__(self):
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

    # pylint: disable=R0912
    def _write_function_code(self, func_node: FunctionNode):
        func_name = func_node.element(NameNode).astext()
        arg_nodes = find_children(func_node.element(ArgumentListNode), ArgumentNode)
        return_node = func_node.element(FunctionReturnNode)

        wt = self._writer

        wt.add("def " + func_name + "(")
        start_kwarg = False
        for i, arg_node in enumerate(arg_nodes):
            arg_name = arg_node.element(NameNode).astext()
            dtype_list_node = arg_node.element(DataTypeListNode)
            default_value_node = arg_node.element(DefaultValueNode)

            is_kwonlyarg = arg_node.attributes["argument_type"] == "kwonlyarg"
            if not start_kwarg and is_kwonlyarg:
                wt.add("*, ")
                start_kwarg = True

            if arg_node.attributes["argument_type"] == "vararg":
                arg_name = f"*{arg_name}"
            elif arg_node.attributes["argument_type"] == "kwarg":
                arg_name = f"**{arg_name}"

            if not dtype_list_node.empty():
                dtype_nodes = find_children(dtype_list_node, DataTypeNode)
                dtype_str = make_union(dtype_nodes)
                for dtype_node in dtype_nodes:
                    if "option" not in dtype_node.attributes:
                        continue
                    if "never none" not in dtype_node.attributes["option"]:
                        dtype_str = f"{dtype_str} | None"
                        break

                if not default_value_node.empty():
                    wt.add(f"{arg_name}: {dtype_str}={default_value_node.astext()}")
                else:
                    wt.add(f"{arg_name}: {dtype_str}")
            else:
                if not default_value_node.empty():
                    wt.add(f"{arg_name}={default_value_node.astext()}")
                else:
                    wt.add(f"{arg_name}")

            if i != len(arg_nodes) - 1:
                wt.add(", ")
        if return_node.empty():
            wt.addln("):")
        else:
            dtype_list_node = return_node.element(DataTypeListNode)
            if not dtype_list_node.empty():
                dtype_nodes = find_children(dtype_list_node, DataTypeNode)
                dtype = make_union(dtype_nodes)
                for dtype_node in dtype_nodes:
                    if "option" not in dtype_node.attributes:
                        continue
                    if "accept none" in dtype_node.attributes["option"]:
                        dtype = f"{dtype} | None"
                        break
                wt.addln(f") -> {dtype}:")
            else:
                wt.addln("):")

        desc_node = func_node.element(DescriptionNode)
        if "deprecated" in func_node.attributes:
            desc_node.insert(0, nodes.Text(func_node.attributes["deprecated"]))

        with CodeWriterIndent(1):
            # documentation
            if (
                not desc_node.empty()
                or any(
                    not n.element(DescriptionNode).empty() != ""
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
                        wt.addln(f":param {name_node.astext()}: {desc_node.astext()}")
                    if not dtype_list_node.empty():
                        dtype_nodes = find_children(dtype_list_node, DataTypeNode)
                        dtype_str = make_union(dtype_nodes)
                        for dtype_node in dtype_nodes:
                            if "option" not in dtype_node.attributes:
                                continue
                            if "never none" not in dtype_node.attributes["option"]:
                                dtype_str = f"{dtype_str} | None"
                                break
                        wt.addln(f":type {name_node.astext()}: {dtype_str}")
                if not return_node.empty():
                    desc_node = return_node.element(DescriptionNode)
                    dtype_list_node = return_node.element(DataTypeListNode)
                    if not desc_node.empty():
                        wt.addln(f":return: {desc_node.astext()}")
                    if not dtype_list_node.empty():
                        dtype_nodes = find_children(dtype_list_node, DataTypeNode)
                        dtype = make_union(dtype_nodes)
                        for dtype_node in dtype_nodes:
                            if "option" not in dtype_node.attributes:
                                continue
                            if "accept none" in dtype_node.attributes["option"]:
                                dtype = f"{dtype} | None"
                                break
                        wt.addln(f":rtype: {dtype}")
                wt.addln("'''")
                wt.new_line(1)
            wt.addln(self.ellipsis_strings["function"])
            wt.new_line(2)

    # pylint: disable=R0914,R0915
    def _write_class_code(self, class_node: ClassNode):
        wt = self._writer

        base_class_list_node = class_node.element(BaseClassListNode)
        name_node = class_node.element(NameNode)
        desc_node = class_node.element(DescriptionNode)
        attr_nodes = find_children(class_node.element(AttributeListNode), AttributeNode)
        method_nodes = find_children(class_node.element(FunctionListNode), FunctionNode)

        if base_class_list_node.empty():
            wt.addln(f"class {name_node.astext()}:")
        else:
            base_class_nodes = find_children(base_class_list_node, BaseClassNode)
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
            wt.addln(f"class {name_node.astext()}({', '.join(dtypes)}):")

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
                    desc_node.insert(0, nodes.Text(attr_node.attributes["deprecated"]))

                dtype_str = None
                if not dtype_list_node.empty():
                    dtype_nodes = find_children(dtype_list_node, DataTypeNode)
                    dtype_str = make_union(dtype_nodes)
                    for dtype_node in dtype_nodes:
                        if "option" not in dtype_node.attributes:
                            continue
                        if "accept none" in dtype_node.attributes["option"]:
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
                if func_type in ("function", "method"):
                    if not arg_list_node.empty():
                        wt.add(f"def {name_node.astext()}(self, ")
                    else:
                        wt.add(f"def {name_node.astext()}(self")
                elif func_type == "classmethod":
                    if not arg_list_node.empty():
                        wt.addln("@classmethod")
                        wt.add(f"def {name_node.astext()}(cls, ")
                    else:
                        wt.addln("@classmethod")
                        wt.add(f"def {name_node.astext()}(cls")
                elif func_type == "staticmethod":
                    if not arg_list_node.empty():
                        wt.addln("@staticmethod")
                        wt.add(f"def {name_node.astext()}(")
                    else:
                        wt.addln("@staticmethod")
                        wt.add(f"def {name_node.astext()}(")
                else:
                    raise NotImplementedError(f"func_type={func_type} is not supported")

                arg_nodes = find_children(arg_list_node, ArgumentNode)
                start_kwarg = False
                for i, arg_node in enumerate(arg_nodes):
                    arg_name = arg_node.element(NameNode).astext()
                    dtype_list_node = arg_node.element(DataTypeListNode)
                    default_value_node = arg_node.element(DefaultValueNode)

                    is_kwonlyarg = arg_node.attributes["argument_type"] == "kwonlyarg"
                    if not start_kwarg and is_kwonlyarg:
                        wt.add("*, ")
                        start_kwarg = True

                    if arg_node.attributes["argument_type"] == "vararg":
                        arg_name = f"*{arg_name}"
                    elif arg_node.attributes["argument_type"] == "kwarg":
                        arg_name = f"**{arg_name}"

                    if not dtype_list_node.empty():
                        dtype_nodes = find_children(dtype_list_node, DataTypeNode)
                        dtype_str = make_union(dtype_nodes)
                        for dtype_node in dtype_nodes:
                            if "option" not in dtype_node.attributes:
                                continue
                            if "never none" not in dtype_node.attributes["option"]:
                                dtype_str = f"{dtype_str} | None"
                                break

                        if not default_value_node.empty():
                            wt.add(f"{arg_name}: {dtype_str}="
                                   f"{default_value_node.astext()}")
                        else:
                            wt.add(f"{arg_name}: {dtype_str}")
                    else:
                        if not default_value_node.empty():
                            wt.add(f"{arg_name}="
                                   f"{default_value_node.astext()}")
                        else:
                            wt.add(arg_name)

                    if i != len(arg_nodes) - 1:
                        wt.add(", ")

                return_node = method_node.element(FunctionReturnNode)
                if return_node.empty():
                    wt.addln("):")
                else:
                    dtype_list_node = return_node.element(DataTypeListNode)
                    if not dtype_list_node.empty():
                        dtype_nodes = find_children(dtype_list_node, DataTypeNode)
                        dtype = make_union(dtype_nodes)
                        for dtype_node in dtype_nodes:
                            if "option" not in dtype_node.attributes:
                                continue
                            if "accept none" in dtype_node.attributes["option"]:
                                dtype = f"{dtype} | None"
                                break
                        wt.addln(f") -> {dtype}:")
                    else:
                        wt.addln("):")

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
                            wt.addln(f":param {name_node.astext()}: {desc_node.astext()}")
                            if not dtype_list_node.empty():
                                dtype_nodes = find_children(dtype_list_node, DataTypeNode)
                                dtype_str = make_union(dtype_nodes)
                                for dtype_node in dtype_nodes:
                                    if "option" not in dtype_node.attributes:
                                        continue
                                    if "never none" not in dtype_node.attributes["option"]:
                                        dtype_str = f"{dtype_str} | None"
                                        break
                                wt.addln(f":type {name_node.astext()}: {dtype_str}")

                        if not return_node.empty():
                            desc_node = return_node.element(DescriptionNode)
                            dtype_list_node = return_node.element(DataTypeListNode)

                            wt.addln(f":return: {desc_node.astext()}")

                            if not dtype_list_node.empty():
                                dtype_nodes = find_children(dtype_list_node, DataTypeNode)
                                dtype = make_union(dtype_nodes)
                                for dtype_node in dtype_nodes:
                                    if "option" not in dtype_node.attributes:
                                        continue
                                    if "accept none" in dtype_node.attributes["option"]:
                                        dtype = f"{dtype} | None"
                                        break
                                wt.addln(f":rtype: {dtype}")
                        wt.addln("'''")

                    wt.addln(self.ellipsis_strings["method"])
                    wt.new_line()

            if len(attr_nodes) == 0 and len(method_nodes) == 0:
                wt.addln(self.ellipsis_strings["class"])
                wt.new_line(2)

    def _write_constant_code(self, data_node: DataNode):
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
                if "option" not in dtype_node.attributes:
                    continue
                if "accept none" in dtype_node.attributes["option"]:
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

    def write(self, filename: str, document: nodes.document, style_config: str = 'ruff'):
        # At first, sort data to avoid generating large diff.
        # Note: Base class must be located above derived class
        sorted_data = sorted_entry_point_nodes(document)

        with open(f"{filename}.{self.file_format}", "w",
                  encoding="utf-8", newline="\n") as file:
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
                for child in sorted(children):
                    wt.addln(f"from . import {child}")
            if len(children) > 0:
                wt.new_line()

            if (len(dependencies) > 0) or (len(children) > 0):
                wt.new_line()

            # for generic type
            wt.new_line()
            wt.addln('GenericType1 = typing.TypeVar("GenericType1")')
            wt.addln('GenericType2 = typing.TypeVar("GenericType2")')

            for node in sorted_data:
                if isinstance(node, FunctionNode):
                    self._write_function_code(node)
                elif isinstance(node, ClassNode):
                    self._write_class_code(node)
                elif isinstance(node, DataNode):
                    self._write_constant_code(node)

            wt.format(style_config, self.file_format)
            wt.write(file)


class PyCodeWriter(PyCodeWriterBase):
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
        super().__init__()

        self.file_format = "json"

    def _clean_node_attributes(self, attributes: dict) -> dict:
        cleaned = copy.deepcopy(attributes)

        keys_to_remove = ("ids", "classes", "names", "dupnames", "backrefs")
        for key in keys_to_remove:
            if key in cleaned:
                del cleaned[key]

        return cleaned

    def _create_function_json_data(self, func_node: FunctionNode):
        func_data = {
            "type": "function",
            "name": func_node.element(NameNode).astext(),
            "description": func_node.element(DescriptionNode).astext(),
            "arguments": [],
            "return": {},
            "options": self._clean_node_attributes(func_node.attributes),
        }

        arg_nodes = find_children(func_node.element(ArgumentListNode), ArgumentNode)
        for arg_node in arg_nodes:
            arg_data = {
                "name": arg_node.element(NameNode).astext(),
                "description": arg_node.element(DescriptionNode).astext(),
                "data_types": [],
                "default_value": arg_node.element(DefaultValueNode).astext()
            }
            dtype_nodes = find_children(arg_node.element(DataTypeListNode), DataTypeNode)
            for dtype_node in dtype_nodes:
                dtype_data = {
                    "data_type": dtype_node.to_string(),
                    "options": self._clean_node_attributes(dtype_node.attributes),
                }
                arg_data["data_types"].append(dtype_data)
            func_data["arguments"].append(arg_data)

        ret_node = func_node.element(FunctionReturnNode)
        func_data["return"] = {
            "description": ret_node.element(DescriptionNode).astext(),
            "data_types": [],
        }
        dtype_nodes = find_children(ret_node.element(DataTypeListNode), DataTypeNode)
        for dtype_node in dtype_nodes:
            dtype_data = {
                "data_type": dtype_node.to_string(),
                "options": self._clean_node_attributes(dtype_node.attributes),
            }
            func_data["return"]["data_types"].append(dtype_data)

        return func_data

    def _create_constant_json_data(self, data_node: DataNode):
        data_data = {
            "type": "data",
            "name": data_node.element(NameNode).astext(),
            "description": data_node.element(DescriptionNode).astext(),
            "data_types": [],
            "options": self._clean_node_attributes(data_node.attributes),
        }

        dtype_nodes = find_children(data_node.element(DataTypeListNode), DataTypeNode)
        for dtype_node in dtype_nodes:
            dtype_data = {
                "data_type": dtype_node.to_string(),
                "options": self._clean_node_attributes(dtype_node.attributes),
            }
            data_data["data_types"].append(dtype_data)

        return data_data

    def _create_class_json_data(self, class_node: ClassNode):
        class_data = {
            "type": "class",
            "name": class_node.element(NameNode).astext(),
            "description": class_node.element(DescriptionNode).astext(),
            "base_classes": [],
            "attributes": [],
            "methods": [],
            "options": self._clean_node_attributes(class_node.attributes),
        }

        base_class_nodes = find_children(class_node.element(BaseClassListNode), BaseClassNode)
        for base_class_node in base_class_nodes:
            base_class_data = {
                "data_types": [],
            }
            dtype_nodes = find_children(base_class_node.element(DataTypeListNode), DataTypeNode)
            for dtype_node in dtype_nodes:
                dtype_data = {
                    "data_type": dtype_node.to_string(),
                    "options": self._clean_node_attributes(dtype_node.attributes),
                }
                base_class_data["data_types"].append(dtype_data)
            class_data["base_classes"].append(base_class_data)

        attr_nodes = find_children(class_node.element(AttributeListNode), AttributeNode)
        for attr_node in attr_nodes:
            attr_data = self._create_constant_json_data(attr_node)
            del attr_data["type"]
            class_data["attributes"].append(attr_data)

        method_nodes = find_children(class_node.element(FunctionListNode), FunctionNode)
        for method_node in method_nodes:
            method_data = self._create_function_json_data(method_node)
            del method_data["type"]
            class_data["methods"].append(method_data)

        return class_data

    def write(self, filename: str, document: nodes.document, style_config: str = 'none'):
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
            "contents": ["typing", "collections.abc"],
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
            "contents": [
                'GenericType1 = typing.TypeVar("GenericType1")',
                'GenericType2 = typing.TypeVar("GenericType2")',
            ]
        })

        for node in sorted_data:
            if isinstance(node, ClassNode):
                json_data.append(self._create_class_json_data(node))
            elif isinstance(node, FunctionNode):
                json_data.append(self._create_function_json_data(node))
            elif isinstance(node, DataNode):
                json_data.append(self._create_constant_json_data(node))

        with open(f"{filename}.{self.file_format}", "w", newline="\n", encoding="utf-8") as f:
            json.dump(json_data, f, indent=4)
