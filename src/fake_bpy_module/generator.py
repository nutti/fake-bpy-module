import pathlib
import abc
import io
from typing import List
from collections import OrderedDict
import subprocess
from yapf.yapflib.yapf_api import FormatCode
from docutils import nodes

from .docutils_based.analyzer.nodes import (
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
    TargetFileNode,
    ChildModuleListNode,
    ChildModuleNode,
    DependencyListNode,
    DependencyNode,
)
from .docutils_based.transformer import transformer
from .docutils_based.common import find_children, get_first_child

from .analyzer import (
    BaseAnalyzer,
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
            self, document: nodes.document) -> List[NodeBase]:
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

    # def dump_json(self, filename: str, document: nodes.document):
    #     json_data = [info.to_dict() for info in data.data]
    #     with open(filename, "w", newline="\n", encoding="utf-8") as f:
    #         json.dump(json_data, f, indent=4)

    @abc.abstractmethod
    def generate(self,
                 filename: str,
                 document: nodes.document,
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
                 document: nodes.document,
                 style_config: str = 'ruff'):
        # At first, sort data to avoid generating large diff.
        # Note: Base class must be located above derived class
        sorted_data = self._sorted_generation_info(document)

        with open(f"{filename}.{self.file_format}", "w",
                  encoding="utf-8", newline="\n") as file:
            wt = self._writer
            wt.reset()

            # import external depended modules
            wt.addln("import typing")

            # import depended modules
            dep_list_node = get_first_child(document, DependencyListNode)
            dep_nodes = find_children(dep_list_node, DependencyNode)
            dependencies = [node.astext() for node in dep_nodes]
            for dep in sorted(dependencies):
                wt.addln(f"import {dep}")

            if len(dependencies) > 0:
                wt.new_line()

            # import child module to search child modules
            child_list_node = get_first_child(document, ChildModuleListNode)
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

    def _analyze(self) -> List[nodes.document]:
        result: List[nodes.document] = []
        for rule in self._rules:
            result.extend(self._analyze_by_rule(rule))

        return result

    def _apply_pre_transform(self, documents: List[nodes.document],
                             mod_files: List[str]) -> List[nodes.document]:
        t = transformer.Transformer([
            "base_class_fixture",
            "rst_specific_node_cleaner",
            "module_level_attribute_fixture",
            "bpy_app_handlers_data_type_adder",
            "bpy_ops_override_parameters_adder",
            "bpy_types_class_base_class_rebaser",
            "bpy_context_variable_converter",
            "mod_applier",
            "format_validator"
        ], {
            "mod_applier": {
                "mod_files": mod_files
            }
        })
        documents = t.transform(documents)

        return documents

    def _analyze_by_rule(
            self, rule: 'PackageGenerationRule') -> List[nodes.document]:
        # replace windows path separator
        target_files = [f.replace("\\", "/") for f in rule.target_files()]
        # analyze all .rst files
        rule.analyzer().set_target(self._config.target)
        rule.analyzer().set_target_version(self._config.target_version)
        documents = rule.analyzer().analyze(target_files)
        documents = self._apply_pre_transform(documents, rule.analyzer().mod_files)

        return documents

    def _apply_post_transform(
            self, documents: List[nodes.document]) -> List[nodes.document]:
        t = transformer.Transformer([
            "target_file_combiner",
            "data_type_refiner",
            "cannonical_data_type_rewriter",
            "dependency_builder",
        ])
        documents = t.transform(documents)

        return documents

    def analyze(self):
        documents = self._analyze()
        self._apply_post_transform(documents)

        return documents


class PackageGenerator:
    def __init__(self, config: 'PackageGeneratorConfig'):
        self._config: 'PackageGeneratorConfig' = config
        self._rules: List['PackageGenerationRule'] = []

    # create module directories/files
    def _create_empty_modules(self, documents: List[nodes.document]):
        for doc in documents:
            target_filename = get_first_child(doc, TargetFileNode).astext()
            dir_path = self._config.output_dir + "/" + target_filename[:target_filename.rfind("/")]
            pathlib.Path(dir_path).mkdir(parents=True, exist_ok=True)
            self._create_py_typed_file(dir_path)

    def _generate_by_rule(self,
                          rule: 'PackageGenerationRule',
                          documents: List[nodes.document]):
        for doc in documents:
            target_filename = get_first_child(doc, TargetFileNode).astext()

            # dump if necessary
            # if self._config.dump:
            #     rule.generator().dump_json(
            #         f"{self._config.output_dir}/{target_filename}-dump.json", info)
            # generate python code
            rule.generator().generate(
                f"{self._config.output_dir}/{target_filename}", doc,
                self._config.style_format)

    def _generate(
            self, rule: 'PackageGenerationRule',
            documents: List[nodes.document]):
        self._generate_by_rule(rule, documents)

    def _create_py_typed_file(self, directory: str):
        filename = f"{directory}/py.typed"
        with open(filename, "w", encoding="utf-8", newline="\n") as file:
            file.write("")

    def add_rule(self, rule: 'PackageGenerationRule'):
        self._rules.append(rule)

    def generate(self):
        analyzer = PackageAnalyzer(self._config, self._rules)
        documents = analyzer.analyze()

        self._create_empty_modules(documents)
        self._generate(self._rules[0], documents)
