import json
import re
import pathlib
import abc
import io
import typing
from typing import List, Dict
from collections import OrderedDict
import subprocess
from yapf.yapflib.yapf_api import FormatCode
from docutils import nodes

from .docutils_based.analyzer.nodes import (
    ModuleNode,
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
)
from .docutils_based.analyzer.roles import (
    ClassRef,
)
from .docutils_based.common import get_first_child, find_children

from .analyzer import (
    BaseAnalyzer,
)
from .common import (
    ModuleStructure,
    DataTypeRefiner,
    EntryPoint,
)
from .utils import (
    remove_unencodable,
)
from .dag import (
    DAG,
    topological_sort
)

INDENT = "    "


class CodeWriterIndent:
    indent_stack: List[int] = [0]

    def __init__(self, indent: int = 0):
        self._indent: int = indent

    def __enter__(self):
        cls = self.__class__
        cls.indent_stack.append(self._indent)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        cls = self.__class__
        cls.indent_stack.pop()

    @classmethod
    def current_indent(cls) -> int:
        return cls.indent_stack[-1]


class CodeWriter:
    def __init__(self):
        self._code_data: io.StringIO = io.StringIO()
        self._buffer: io.StringIO = io.StringIO()

    def add(self, code: str, new_line: bool = False):
        self._buffer.write(code)
        if new_line:
            indent = CodeWriterIndent.current_indent()
            self._code_data.write(INDENT * indent)
            self._code_data.write(self._buffer.getvalue())
            self._code_data.write("\n")
            self._buffer = io.StringIO()

    def addln(self, code: str):
        self.add(code, True)

    def new_line(self, num: int = 1):
        if self._buffer.tell() > 0:
            indent = CodeWriterIndent.current_indent()
            self._code_data.write(INDENT * indent)
            self._code_data.write(self._buffer.getvalue())
            self._buffer = io.StringIO()
        self._code_data.write("\n" * num)

    def write(self, file: io.TextIOWrapper):
        file.write(self._code_data.getvalue())

    def reset(self):
        self._code_data = io.StringIO()
        self._buffer = io.StringIO()

    def format(self, style_config: str, file_format: str):
        if style_config == "yapf":
            self._code_data = io.StringIO(FormatCode(
                self._code_data.getvalue(), style_config="pep8")[0])
        elif style_config == "ruff":
            self._code_data = io.StringIO(subprocess.check_output(
                [
                    "ruff",
                    "format",
                    "--isolated",
                    f"--stdin-filename=_.{file_format}",
                ],
                input=self._code_data.getvalue().encode(),
            ).decode())
        elif style_config == "none":
            pass
        else:
            raise ValueError(f"Invalid style config: {style_config}")


class BaseGenerator(metaclass=abc.ABCMeta):
    def __init__(self):
        self._writer: 'CodeWriter' = CodeWriter()

    @abc.abstractmethod
    def _gen_function_code(self, func_node: FunctionNode):
        raise NotImplementedError()

    @abc.abstractmethod
    def _gen_class_code(self, class_node: ClassNode):
        raise NotImplementedError()

    @abc.abstractmethod
    def _gen_constant_code(self, data_node: DataNode):
        raise NotImplementedError()

    def _is_relative_import(self, mod_name: str):
        return mod_name[0] == "."

    def _sorted_generation_info(
            self, data: 'GenerationInfoByTarget') -> List[NodeBase]:
        all_class_nodes: List[ClassNode] = []
        all_function_nodes: List[FunctionNode] = []
        all_data_nodes: List[DataNode] = []
        all_high_priority_class_nodes: List[ClassNode] = []
        for document in data.data:
            class_nodes = find_children(document, ClassNode)
            for class_node in class_nodes:
                class_name = class_node.element(NameNode).astext()
                if class_name in ("bpy_prop_collection", "bpy_prop_array",
                                  "bpy_struct"):
                    all_high_priority_class_nodes.append(class_node)
                else:
                    all_class_nodes.append(class_node)
            all_function_nodes.extend(find_children(document, FunctionNode))
            all_data_nodes.extend(find_children(document, DataNode))

        all_class_nodes = all_high_priority_class_nodes \
            + sorted(all_class_nodes, key=lambda n: n.element(NameNode).astext())

        # Sort class data (with class inheritance dependencies)
        graph = DAG()
        class_name_to_nodes = OrderedDict()
        for class_node in all_class_nodes:
            class_name = class_node.element(NameNode).astext()
            class_name_to_nodes[class_name] = graph.make_node(class_node)
        for class_node in all_class_nodes:
            class_name = class_node.element(NameNode).astext()
            src_node = class_name_to_nodes[class_name]

            base_class_list_node = class_node.element(BaseClassListNode)
            base_class_nodes = find_children(base_class_list_node, BaseClassNode)
            for base_class_node in base_class_nodes:
                dtype_list_node = base_class_node.element(DataTypeListNode)
                dtype_nodes = find_children(dtype_list_node, DataTypeNode)
                dtypes = [dt.astext().replace("`", "") for dt in dtype_nodes]

                for dtype in dtypes:
                    dst_node = class_name_to_nodes.get(dtype)
                    if dst_node:
                        graph.make_edge(src_node, dst_node)

        sorted_nodes = topological_sort(graph)
        sorted_class_nodes = [node.data() for node in sorted_nodes]

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

    def print_header(self, file):
        pass

    def pre_process(self, _: str, gen_info: 'GenerationInfoByTarget'):
        processed = GenerationInfoByTarget()
        processed.name = gen_info.name
        processed.child_modules = gen_info.child_modules
        processed.dependencies = gen_info.dependencies
        processed.external_modules = gen_info.external_modules

        for d in gen_info.data:
            processed.data.append(d)

        return processed

    def dump_json(self, filename: str, data: 'GenerationInfoByTarget'):
        json_data = [info.to_dict() for info in data.data]
        with open(filename, "w", newline="\n", encoding="utf-8") as f:
            json.dump(json_data, f, indent=4)

    @abc.abstractmethod
    def generate(self,
                 filename: str,
                 data: 'GenerationInfoByTarget',
                 style_config: str = 'ruff'):
        raise NotImplementedError()


class PyCodeGeneratorBase(BaseGenerator):
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

    # pylint: disable=R0912
    def _gen_function_code(self, func_node: FunctionNode):
        func_name = func_node.element(NameNode).astext()
        arg_nodes = find_children(func_node.element(ArgumentListNode), ArgumentNode)
        return_node = func_node.element(FunctionReturnNode)

        wt = self._writer

        wt.add("def " + func_name + "(")
        for i, arg_node in enumerate(arg_nodes):
            arg_name = arg_node.element(NameNode).astext()
            dtype_list_node = arg_node.element(DataTypeListNode)
            default_value_node = arg_node.element(DefaultValueNode)

            if not dtype_list_node.empty():
                dtype_nodes = find_children(dtype_list_node, DataTypeNode)
                if len(dtype_nodes) >= 2:
                    dtype = f"typing.Union[{', '.join([n.to_string() for n in dtype_nodes])}]"
                else:
                    dtype = dtype_nodes[0].to_string()
                if not default_value_node.empty():
                    wt.add(f"{arg_name}: {dtype}={default_value_node.astext()}")
                else:
                    wt.add(f"{arg_name}: {dtype}")
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
                if len(dtype_nodes) >= 2:
                    dtype = f"typing.Union[{', '.join([n.to_string() for n in dtype_nodes])}]"
                else:
                    dtype = dtype_nodes[0].to_string()
                wt.addln(f") -> {dtype}:")
            else:
                wt.addln("):")

        desc_node = func_node.element(DescriptionNode)

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
                        if len(dtype_nodes) >= 2:
                            dtype_str = ", ".join([n.to_string() for n in dtype_nodes])
                            dtype = f"typing.Union[{dtype_str}]"
                        else:
                            dtype = dtype_nodes[0].to_string()
                        wt.addln(f":type {name_node.astext()}: {dtype}")
                if not return_node.empty():
                    desc_node = return_node.element(DescriptionNode)
                    dtype_list_node = return_node.element(DataTypeListNode)
                    if not desc_node.empty():
                        wt.addln(f":return: {desc_node.astext()}")
                    if not dtype_list_node.empty():
                        dtype_nodes = find_children(dtype_list_node, DataTypeNode)
                        if len(dtype_nodes) >= 2:
                            dtype_str = ", ".join([n.to_string() for n in dtype_nodes])
                            dtype = f"typing.Union[{dtype_str}]"
                        else:
                            dtype = dtype_nodes[0].to_string()
                        wt.addln(f":rtype: {dtype}")
                wt.addln("'''")
                wt.new_line(1)
            wt.addln(self.ellipsis_strings["function"])
            wt.new_line(2)

    def _gen_class_code(self, class_node: ClassNode):
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
                        dtype = f"typing.Union[{', '.join([n.to_string() for n in dtype_nodes])}]"
                    else:
                        dtype = dtype_nodes[0].to_string()
                    dtypes.append(dtype)
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

                if not dtype_list_node.empty():
                    dtype_nodes = find_children(dtype_list_node, DataTypeNode)
                    if len(dtype_nodes) >= 2:
                        dtype = f"typing.Union[{', '.join([n.to_string() for n in dtype_nodes])}]"
                    else:
                        dtype = dtype_nodes[0].to_string()
                    wt.addln(f"{name_node.astext()}: {dtype}"
                             f"{self.ellipsis_strings['attribute']}")
                else:
                    wt.addln(f"{name_node.astext()}: typing.Any"
                             f"{self.ellipsis_strings['attribute']}")

                if not desc_node.empty() or not dtype_list_node.empty():
                    wt.add("''' ")
                    if not desc_node.empty():
                        wt.add(f"{desc_node.astext()}")
                    if not dtype_list_node.empty():
                        dtype_nodes = find_children(dtype_list_node, DataTypeNode)
                        if len(dtype_nodes) >= 2:
                            dtype_str = ", ".join([n.to_string() for n in dtype_nodes])
                            dtype = f"typing.Union[{dtype_str}]"
                        else:
                            dtype = dtype_nodes[0].to_string()
                        wt.new_line(2)
                        wt.addln(f":type: {dtype}")
                    wt.addln("'''")
                    wt.new_line(1)
            if len(attr_nodes) > 0:
                wt.new_line(1)

            for method_node in method_nodes:
                func_type = method_node.attributes["function_type"]
                arg_list_node = method_node.element(ArgumentListNode)
                name_node = method_node.element(NameNode)

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
                for i, arg_node in enumerate(arg_nodes):
                    name_node = arg_node.element(NameNode)
                    dtype_list_node = arg_node.element(DataTypeListNode)
                    default_value_node = arg_node.element(DefaultValueNode)

                    if not dtype_list_node.empty():
                        dtype_nodes = find_children(dtype_list_node, DataTypeNode)
                        if len(dtype_nodes) >= 2:
                            dtype_str = ", ".join([n.to_string() for n in dtype_nodes])
                            dtype = f"typing.Union[{dtype_str}]"
                        else:
                            dtype = dtype_nodes[0].to_string()

                        if not default_value_node.empty():
                            wt.add(f"{name_node.astext()}: {dtype}="
                                   f"{default_value_node.astext()}")
                        else:
                            wt.add(f"{name_node.astext()}: {dtype}")
                    else:
                        if not default_value_node.empty():
                            wt.add(f"{name_node.astext()}="
                                   f"{default_value_node.astext()}")
                        else:
                            wt.add(name_node.astext())

                    if i != len(arg_nodes) - 1:
                        wt.add(", ")

                return_node = method_node.element(FunctionReturnNode)
                if return_node.empty():
                    wt.addln("):")
                else:
                    if not dtype_list_node.empty():
                        dtype_nodes = find_children(dtype_list_node, DataTypeNode)
                        if len(dtype_nodes) >= 2:
                            dtype_str = ", ".join([n.to_string() for n in dtype_nodes])
                            dtype = f"typing.Union[{dtype_str}]"
                        else:
                            dtype = dtype_nodes[0].to_string()
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
                                if len(dtype_nodes) >= 2:
                                    dtype_str = ", ".join([n.to_string() for n in dtype_nodes])
                                    dtype = f"typing.Union[{dtype_str}]"
                                else:
                                    dtype = dtype_nodes[0].to_string()
                                wt.addln(f":type {name_node.astext()}: {dtype}")

                        if not return_node.empty():
                            desc_node = return_node.element(DescriptionNode)
                            dtype_list_node = return_node.element(DataTypeListNode)

                            wt.addln(f":return: {desc_node.astext()}")

                            if not dtype_list_node.empty():
                                dtype_nodes = find_children(dtype_list_node, DataTypeNode)
                                if len(dtype_nodes) >= 2:
                                    dtype_str = ", ".join([n.to_string() for n in dtype_nodes])
                                    dtype = f"typing.Union[{dtype_str}]"
                                else:
                                    dtype = dtype_nodes[0].to_string()
                                wt.addln(f":rtype: {dtype}")
                        wt.addln("'''")

                    wt.addln(self.ellipsis_strings["method"])
                    wt.new_line()

            if len(attr_nodes) == 0 and len(method_nodes) == 0:
                wt.addln(self.ellipsis_strings["class"])
                wt.new_line(2)

    def _gen_constant_code(self, data_node: DataNode):
        wt = self._writer

        name_node = data_node.element(NameNode)
        dtype_list_node = data_node.element(DataTypeListNode)
        desc_node = data_node.element(DescriptionNode)

        if not dtype_list_node.empty():
            dtype_nodes = find_children(dtype_list_node, DataTypeNode)
            if len(dtype_nodes) >= 2:
                dtype = f"typing.Union[{', '.join([n.to_string() for n in dtype_nodes])}]"
            else:
                dtype = dtype_nodes[0].to_string()
            wt.addln(f"{name_node.astext()}: {dtype}"
                     f"{self.ellipsis_strings['constant']}")
        else:
            wt.addln(f"{name_node.astext()}: typing.Any"
                     f"{self.ellipsis_strings['constant']}")
        if not desc_node.empty():
            wt.addln(f"''' {remove_unencodable(desc_node.astext())}")
            wt.addln("'''")
        wt.new_line(2)

    def generate(self,
                 filename: str,
                 data: 'GenerationInfoByTarget',
                 style_config: str = 'ruff'):
        # At first, sort data to avoid generating large diff.
        # Note: Base class must be located above derived class
        sorted_data = self._sorted_generation_info(data)

        with open(f"{filename}.{self.file_format}", "w",
                  encoding="utf-8", newline="\n") as file:
            self.print_header(file)

            wt = self._writer
            wt.reset()

            # import external depended modules
            for ext in sorted(data.external_modules):
                wt.addln(f"import {ext}")

            # import depended modules
            for dep in sorted(data.dependencies,
                              key=lambda x: (self._is_relative_import(x.mod_name), x.mod_name)):
                mod_name = dep.mod_name
                if self._is_relative_import(mod_name):
                    wt.add(f"from {mod_name} import (")
                    for i, type_ in enumerate(sorted(dep.type_lists)):
                        wt.add(type_)
                        if i == len(dep.type_lists) - 1:
                            wt.addln(")")
                        else:
                            wt.add(", ")
                else:
                    wt.addln(f"import {dep.mod_name}")

            if len(data.dependencies) > 0:
                wt.new_line()

            # import child module to search child modules
            for mod in sorted(data.child_modules):
                wt.addln(f"from . import {mod}")
            if len(data.child_modules) > 0:
                wt.new_line()

            if (len(data.dependencies) > 0) or (len(data.child_modules) > 0):
                wt.new_line()

            # for generic type
            wt.new_line()
            wt.addln('GenericType = typing.TypeVar("GenericType")')

            for node in sorted_data:
                if isinstance(node, FunctionNode):
                    self._gen_function_code(node)
                elif isinstance(node, ClassNode):
                    self._gen_class_code(node)
                elif isinstance(node, DataNode):
                    self._gen_constant_code(node)

            wt.format(style_config, self.file_format)
            wt.write(file)


class PyCodeGenerator(PyCodeGeneratorBase):
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


class PyInterfaceGenerator(PyCodeGeneratorBase):
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


class Dependency:
    def __init__(self):
        self._mod_name: str = None
        self._type_lists: List[str] = []

    @property
    def mod_name(self) -> str:
        if self._mod_name is None:
            raise RuntimeError("Must specify module name")
        return self._mod_name

    @mod_name.setter
    def mod_name(self, value: str):
        self._mod_name = value

    @property
    def type_lists(self) -> List[str]:
        if not self._type_lists:
            raise RuntimeError(
                "At least 1 element must be added to type lists")
        return self._type_lists

    def add_type(self, type_: str):
        self._type_lists.append(type_)


class GenerationInfoByTarget:
    def __init__(self):
        self.name: str = None       # Module name
        self.data: List[nodes.document] = []
        self.child_modules: List[str] = []
        self.dependencies: List['Dependency'] = []
        self.external_modules: List[str] = ["typing"]


class GenerationInfoByRule:
    def __init__(self):
        # Key: Output file name
        self._info: Dict[str, 'GenerationInfoByTarget'] = {}

    def get_target(self, target: str) -> 'GenerationInfoByTarget':
        if target not in self._info:
            raise RuntimeError("Could not find target in GenerationInfoByRule "
                               f"(target: {target})")
        return self._info[target]

    def create_target(self, target: str) -> 'GenerationInfoByTarget':
        self._info[target] = GenerationInfoByTarget()
        return self._info[target]

    def get_or_create_target(self, target: str):
        info = None
        try:
            info = self.get_target(target)
        except RuntimeError:
            pass
        if info is None:
            info = self.create_target(target)
        return info

    def targets(self):
        return self._info.keys()

    def update_target(self, target: str, info: 'GenerationInfoByTarget'):
        self._info[target] = info


class PackageGeneratorConfig:
    def __init__(self):
        self.output_dir: str = "./out"
        self.os: str = "Linux"
        self.style_format: str = "ruff"
        self.dump: bool = False
        self.target: str = "blender"
        self.target_version: str = None
        self.mod_version: str = None
        self.output_format: str = "pyi"


class PackageGenerationRule:
    def __init__(self, name: str, target_files: List[str],
                 analyzer: BaseAnalyzer, generator: 'BaseGenerator'):
        self._name: str = name      # Rule
        self._target_files: List[str] = target_files
        self._analyzer: BaseAnalyzer = analyzer
        self._generator: 'BaseGenerator' = generator

    def name(self) -> str:
        return self._name

    def target_files(self) -> List[str]:
        return self._target_files

    def analyzer(self) -> BaseAnalyzer:
        return self._analyzer

    def generator(self) -> 'BaseGenerator':
        return self._generator


class PackageAnalyzer:
    def __init__(
            self, config: 'PackageGeneratorConfig',
            rules: List['PackageGenerationRule']):
        self._config: 'PackageGeneratorConfig' = config
        self._rules: List['PackageGenerationRule'] = rules
        self._package_structure: 'ModuleStructure' = None
        self._generation_info: 'GenerationInfoByRule' = None
        self._entry_points: List['EntryPoint'] = []

        self._analyze_result_cache: List[nodes.document] = []

    # build package structure
    def _build_package_structure(self) -> 'ModuleStructure':
        documents = self._analyze()
        module_list = self._collect_module_list(documents)
        return self._build_module_structure(module_list)

    def _analyze(self) -> List[nodes.document]:
        if len(self._analyze_result_cache) == 0:
            for rule in self._rules:
                self._analyze_result_cache.extend(self._analyze_by_rule(rule))
        return self._analyze_result_cache

    def _analyze_by_rule(
            self, rule: 'PackageGenerationRule') -> List[nodes.document]:
        # replace windows path separator
        target_files = [f.replace("\\", "/") for f in rule.target_files()]
        # analyze all .rst files
        rule.analyzer().set_target(self._config.target)
        rule.analyzer().set_target_version(self._config.target_version)
        documents = rule.analyzer().analyze(target_files)

        return documents

    # build module structure
    def _build_module_structure(self, modules: List[str]) -> 'ModuleStructure':
        def build(mod_name: str, structure_: 'ModuleStructure'):
            sp = mod_name.split(".")
            for i in structure_.children():
                if i.name == sp[0]:
                    item = i
                    break
            else:
                item = ModuleStructure()
                item.name = sp[0]
                structure_.add_child(item)
            if len(sp) >= 2:
                s = ".".join(sp[1:])
                build(s, item)

        structure = ModuleStructure()
        for m in modules:
            build(m, structure)

        return structure

    # collect module list
    def _collect_module_list(self, documents: List[nodes.document]) -> List[str]:
        module_list = []
        for document in documents:
            module_node = get_first_child(document, ModuleNode)
            if module_node is None:
                continue
            module_name_node = module_node.element(NameNode)
            module_list.append(module_name_node.astext())

        return module_list

    def _build_entry_points(self) -> List['EntryPoint']:
        # at first analyze without DataTypeRefiner
        documents = self._analyze()
        module_structure = self._build_module_structure(
            self._collect_module_list(documents))
        generation_info = self._build_generation_info_internal(
            documents, module_structure)

        # build entry points
        entry_points: List['EntryPoint'] = []
        for target in generation_info.targets():
            info = generation_info.get_target(target)
            for document in info.data:
                class_nodes = find_children(document, ClassNode)
                for class_node in class_nodes:
                    class_name = class_node.element(NameNode).astext()
                    entry = EntryPoint(info.name, class_name, "class")
                    entry_points.append(entry)

                func_nodes = find_children(document, FunctionNode)
                for func_node in func_nodes:
                    func_name = func_node.element(NameNode).astext()
                    entry = EntryPoint(info.name, func_name, "function")
                    entry_points.append(entry)

                data_nodes = find_children(document, DataNode)
                for data_node in data_nodes:
                    data_name = data_node.element(NameNode).astext()
                    entry = EntryPoint(info.name, data_name, "constant")
                    entry_points.append(entry)

        return entry_points

    def _build_generation_info_internal(
            self, documents: List[nodes.document],
            module_structure: 'ModuleStructure') -> 'GenerationInfoByRule':
        def find_target_file(
                name: str, structure: 'ModuleStructure', target: str,
                module_level: int) -> str:
            for m in structure.children():
                mod_name = name + m.name
                if mod_name == target:
                    return mod_name + "/__init__"

                if len(m.children()) > 0:
                    ret = find_target_file(
                        mod_name + "/", m, target, module_level+1)
                    if ret:
                        return ret
            return None

        def build_child_modules(
                gen_info: 'GenerationInfoByRule', name: str,
                structure: 'ModuleStructure', module_level: int):
            for m in structure.children():
                mod_name = name + m.name
                if len(m.children()) == 0:
                    filename = \
                        re.sub(r"\.", "/", mod_name) + "/__init__"
                    info = gen_info.create_target(filename)
                    info.data = []
                    info.child_modules = []
                    info.name = mod_name
                else:
                    filename = re.sub(r"\.", "/", mod_name) + "/__init__"
                    info = gen_info.create_target(filename)
                    info.data = []
                    info.child_modules = [child.name for child in m.children()]
                    info.name = mod_name
                    build_child_modules(
                        gen_info, mod_name + ".", m, module_level+1)

        # build child modules
        generator_info = GenerationInfoByRule()
        build_child_modules(generator_info, "", module_structure, 0)

        # build data
        for document in documents:
            module_node = get_first_child(document, ModuleNode)
            if module_node is None:
                continue
            module_name = module_node.element(NameNode).astext()
            target = find_target_file("", module_structure,
                                      re.sub(r"\.", "/", module_name), 0)
            if target is None:
                raise RuntimeError("Could not find target file to "
                                   f"generate (target: {module_name})")
            gen_info = generator_info.get_target(target)
            gen_info.data.append(document)

        return generator_info

    def _get_import_module_path(self, refiner: 'DataTypeRefiner',
                                data_type_1: str, data_type_2: str):
        mod_names_full_1 = refiner.get_module_name(data_type_1)
        mod_names_full_2 = refiner.get_module_name(data_type_2)
        if mod_names_full_1 is None or mod_names_full_2 is None:
            return None

        mod_names_1 = mod_names_full_1.split(".")
        mod_names_2 = mod_names_full_2.split(".")

        for i, (m1, m2) in enumerate(zip(mod_names_1, mod_names_2)):
            if m1 != m2:
                match_level = i
                break
        else:
            if len(mod_names_1) >= len(mod_names_2):
                match_level = len(mod_names_2)
            else:
                match_level = len(mod_names_1)

        # [Case 1] No match => Need to import top level module
        #   data_type_1: bpy.types.Mesh
        #   data_type_2: bgl.glCallLists()
        #       => bpy.types
        if match_level == 0:
            module_path = ".".join(mod_names_1)
        else:
            rest_level_1 = len(mod_names_1) - match_level
            rest_level_2 = len(mod_names_2) - match_level

            # [Case 2] Match exactly => No need to import any modules
            #   data_type_1: bgl.Buffer
            #   data_type_2: bgl.glCallLists()
            #       => None
            if rest_level_1 == 0 and rest_level_2 == 0:
                module_path = None
            # [Case 3] Match partially (Same level)
            #               => Need to import top level
            #   data_type_1: bpy.types.Mesh
            #   data_type_2: bpy.ops.automerge()
            #       => bpy.types
            elif rest_level_1 >= 1 and rest_level_2 >= 1:
                module_path = ".".join(mod_names_1)
            # [Case 4] Match partially (Upper level)
            #               => Need to import top level
            #   data_type_1: mathutils.Vector
            #   data_type_2: mathutils.noise.cell
            #       => mathutils
            elif rest_level_1 == 0 and rest_level_2 >= 1:
                module_path = ".".join(mod_names_1)
            # [Case 5] Match partially (Lower level)
            #               => Need to import top level
            #   data_type_1: mathutils.noise.cell
            #   data_type_2: mathutils.Vector
            #       => mathutils.noise
            elif rest_level_1 >= 1 and rest_level_2 == 0:
                module_path = ".".join(mod_names_1)
            else:
                raise RuntimeError("Should not reach this condition.")

        return module_path

    def _add_dependency(self, dependencies: List['Dependency'],
                        refiner: 'DataTypeRefiner',
                        data_type_1: str, data_type_2: str):

        mod = self._get_import_module_path(refiner, data_type_1, data_type_2)
        base = refiner.get_base_name(data_type_1)
        if mod is None:
            return

        target_dep = None
        for dep in dependencies:
            if dep.mod_name == mod:
                target_dep = dep
                break
        if target_dep is None:
            target_dep = Dependency()
            target_dep.mod_name = mod
            target_dep.add_type(base)
            dependencies.append(target_dep)
        else:
            if base not in target_dep.type_lists:
                target_dep.add_type(base)

    def _build_dependencies(
            self, package_structure: 'ModuleStructure',
            entry_points: List['EntryPoint'],
            info: 'GenerationInfoByTarget') -> List['Dependency']:
        refiner = DataTypeRefiner(package_structure, entry_points)

        dependencies = []
        for document in info.data:
            module_node = get_first_child(document, ModuleNode)
            if module_node is None:
                continue
            module_name = module_node.element(NameNode).astext()

            class_nodes = find_children(document, ClassNode)
            for class_node in class_nodes:
                class_name = class_node.element(NameNode).astext()
                class_refs = class_node.traverse(ClassRef)
                for class_ref in class_refs:
                    self._add_dependency(
                        dependencies, refiner, class_ref.to_string(),
                        f"{module_name}.{class_name}")

            func_nodes = find_children(document, FunctionNode)
            for func_node in func_nodes:
                func_name = func_node.element(NameNode).astext()
                class_refs = func_node.traverse(ClassRef)
                for class_ref in class_refs:
                    self._add_dependency(
                        dependencies, refiner, class_ref.to_string(),
                        f"{module_name}.{func_name}")

            data_nodes = find_children(document, DataNode)
            for data_node in data_nodes:
                data_name = data_node.element(NameNode).astext()
                class_refs = data_node.traverse(ClassRef)
                for class_ref in class_refs:
                    self._add_dependency(
                        dependencies, refiner, class_ref.to_string(),
                        f"{module_name}.{data_name}")

        return dependencies

    def _refine_data_type(
            self, refiner: 'DataTypeRefiner', documents: List[nodes.document]):

        def refine(dtype_list_node: DataTypeListNode, module_name: str,
                   variable_kind: str, parameter_str: str = None,
                   additional_info: Dict[str, typing.Any] = None):
            dtype_nodes = find_children(dtype_list_node, DataTypeNode)
            new_dtype_nodes = []
            for dtype_node in dtype_nodes:
                mod_options = []
                skip_refine = False
                if "mod-option" in dtype_node.attributes:
                    mod_options = [
                        sp.strip()
                        for sp in dtype_node.attributes["mod-option"].split(",")
                    ]
                    skip_refine = "skip-refine" in mod_options
                if skip_refine:
                    continue
                new_dtype_nodes.extend(refiner.get_refined_data_type(
                    dtype_node.astext(), module_name, variable_kind,
                    parameter_str=parameter_str, additional_info=additional_info))
                dtype_list_node.remove(dtype_node)
            for node in new_dtype_nodes:
                dtype_list_node.append_child(node)

        for document in documents:
            module_node = get_first_child(document, ModuleNode)
            if module_node is None:
                continue
            module_name = module_node.element(NameNode).astext()

            class_nodes = find_children(document, ClassNode)
            for class_node in class_nodes:
                class_name = class_node.element(NameNode).astext()

                func_list_node = class_node.element(FunctionListNode)
                func_nodes = find_children(func_list_node, FunctionNode)
                for func_node in func_nodes:
                    arg_list_node = func_node.element(ArgumentListNode)
                    arg_nodes = find_children(arg_list_node, ArgumentNode)
                    for arg_node in arg_nodes:
                        arg_name = arg_node.element(NameNode).astext()
                        dtype_list_node = arg_node.element(DataTypeListNode)
                        refine(dtype_list_node, module_name, 'FUNC_ARG',
                               parameter_str=arg_name,
                               additional_info={"self_class": f"{module_name}.{class_name}"})

                    return_node = func_node.element(FunctionReturnNode)
                    dtype_list_node = return_node.element(DataTypeListNode)
                    refine(dtype_list_node, module_name, 'FUNC_RET',
                           additional_info={"self_class": f"{module_name}.{class_name}"})

                attr_list_node = class_node.element(AttributeListNode)
                attr_nodes = find_children(attr_list_node, AttributeNode)
                for attr_node in attr_nodes:
                    dtype_list_node = attr_node.element(DataTypeListNode)
                    refine(dtype_list_node, module_name, 'CONST')

                base_class_list_node = class_node.element(BaseClassListNode)
                base_class_nodes = find_children(base_class_list_node, BaseClassNode)
                for base_class_node in base_class_nodes:
                    dtype_list_node = base_class_node.element(DataTypeListNode)
                    refine(dtype_list_node, module_name, 'CLS_BASE')

            func_nodes = find_children(document, FunctionNode)
            for func_node in func_nodes:
                arg_list_node = func_node.element(ArgumentListNode)
                arg_nodes = find_children(arg_list_node, ArgumentNode)
                for arg_node in arg_nodes:
                    arg_name = arg_node.element(NameNode).astext()
                    dtype_list_node = arg_node.element(DataTypeListNode)
                    refine(dtype_list_node, module_name, 'FUNC_ARG',
                           parameter_str=arg_name)

                return_node = func_node.element(FunctionReturnNode)
                dtype_list_node = return_node.element(DataTypeListNode)
                refine(dtype_list_node, module_name, 'FUNC_RET')

            data_nodes = find_children(document, DataNode)
            for data_node in data_nodes:
                dtype_list_node = data_node.element(DataTypeListNode)
                refine(dtype_list_node, module_name, 'CONST')

    def _rewrite_data_type(
            self, refiner: 'DataTypeRefiner',
            gen_info: 'GenerationInfoByTarget') -> 'GenerationInfoByTarget':
        processed_info = GenerationInfoByTarget()
        processed_info.name = gen_info.name
        processed_info.external_modules = gen_info.external_modules
        processed_info.dependencies = gen_info.dependencies
        processed_info.child_modules = gen_info.child_modules

        def rewrite(class_ref: ClassRef, module_name: str) -> ClassRef:
            class_name = class_ref.to_string()
            new_class_name = refiner.get_generation_data_type(
                class_name, module_name)
            new_class_ref = ClassRef(text=new_class_name)
            return new_class_ref

        def replace(from_node: nodes.Node, to_node: nodes.Node):
            parent = from_node.parent
            index = from_node.parent.index(from_node)
            parent.remove(from_node)
            parent.insert(index, to_node)

        for document in gen_info.data:
            module_node = get_first_child(document, ModuleNode)
            if module_node is None:
                continue
            module_name = module_node.element(NameNode).astext()

            class_nodes = find_children(document, ClassNode)
            for class_node in class_nodes:
                class_refs = class_node.traverse(ClassRef)
                for class_ref in class_refs:
                    new_class_ref = rewrite(class_ref, module_name)
                    replace(class_ref, new_class_ref)

            func_nodes = find_children(document, FunctionNode)
            for func_node in func_nodes:
                class_refs = func_node.traverse(ClassRef)
                for class_ref in class_refs:
                    new_class_ref = rewrite(class_ref, module_name)
                    replace(class_ref, new_class_ref)

            data_nodes = find_children(document, DataNode)
            for data_node in data_nodes:
                class_refs = data_node.traverse(ClassRef)
                for class_ref in class_refs:
                    new_class_ref = rewrite(class_ref, module_name)
                    replace(class_ref, new_class_ref)

            processed_info.data.append(document)

        return processed_info

    # map between result of analyze and module structure
    def _build_generation_info(
            self, package_structure: 'ModuleStructure',
            entry_points: List['EntryPoint']) -> 'GenerationInfoByRule':
        refiner = DataTypeRefiner(package_structure, entry_points)
        documents = self._analyze()
        self._refine_data_type(refiner, documents)
        module_structure = self._build_module_structure(
            self._collect_module_list(documents))
        generation_info = self._build_generation_info_internal(
            documents, module_structure)

        for target in generation_info.targets():
            info = generation_info.get_target(target)
            info = self._rewrite_data_type(refiner, info)
            generation_info.update_target(target, info)

        return generation_info

    def package_structure(self) -> 'ModuleStructure':
        return self._package_structure

    def entry_points(self) -> List['EntryPoint']:
        return self._entry_points

    def generation_info(self) -> 'GenerationInfoByRule':
        return self._generation_info

    def analyze(self):
        self._package_structure = self._build_package_structure()
        self._entry_points = self._build_entry_points()

        self._generation_info = self._build_generation_info(
            self._package_structure, self._entry_points)
        for target in self._generation_info.targets():
            info = self._generation_info.get_target(target)
            info.dependencies = self._build_dependencies(
                self._package_structure, self._entry_points, info)


class PackageGenerator:
    def __init__(self, config: 'PackageGeneratorConfig'):
        self._config: 'PackageGeneratorConfig' = config
        self._rules: List['PackageGenerationRule'] = []

    # create module directories/files
    def _create_empty_modules(self, package_structure: 'ModuleStructure'):
        def make_module_dirs(base_path: str, structure: 'ModuleStructure'):
            def make_dir(path, structure_: 'ModuleStructure',
                         module_level: int):
                for item in structure_.children():
                    if len(item.children()) == 0:
                        dir_path = path + "/" + item.name
                        pathlib.Path(dir_path).mkdir(
                            parents=True, exist_ok=True)
                        if module_level == 0:
                            self._create_py_typed_file(dir_path)
                    elif len(item.children()) >= 1:
                        dir_path = path + "/" + item.name
                        pathlib.Path(dir_path).mkdir(
                            parents=True, exist_ok=True)
                        if module_level == 0:
                            self._create_py_typed_file(dir_path)
                        if dir_path == base_path:
                            continue
                        make_dir(dir_path, item, module_level+1)

            make_dir(base_path, structure, 0)

        make_module_dirs(self._config.output_dir, package_structure)

    def _generate_by_rule(self,
                          rule: 'PackageGenerationRule',
                          _: 'ModuleStructure',
                          gen_info: 'GenerationInfoByRule'):
        for target in gen_info.targets():
            info = gen_info.get_target(target)
            # pre process
            info = rule.generator().pre_process(target, info)
            # dump if necessary
            if self._config.dump:
                rule.generator().dump_json(
                    f"{self._config.output_dir}/{target}-dump.json", info)
            # generate python code
            rule.generator().generate(
                f"{self._config.output_dir}/{target}", info,
                self._config.style_format)

    def _generate(
            self, rule: 'PackageGenerationRule',
            package_strcuture: 'ModuleStructure',
            generation_info: 'GenerationInfoByRule'):
        self._generate_by_rule(rule, package_strcuture, generation_info)

    def _create_py_typed_file(self, directory: str):
        filename = f"{directory}/py.typed"
        with open(filename, "w", encoding="utf-8", newline="\n") as file:
            file.write("")

    def add_rule(self, rule: 'PackageGenerationRule'):
        self._rules.append(rule)

    def generate(self):
        analyzer = PackageAnalyzer(self._config, self._rules)
        analyzer.analyze()

        self._create_empty_modules(analyzer.package_structure())
        self._generate(self._rules[0],
                       analyzer.package_structure(), analyzer.generation_info())
