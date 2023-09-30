import json
import re
import pathlib
from typing import List, Dict
from collections import OrderedDict
from yapf.yapflib.yapf_api import FormatCode
from tqdm import tqdm

from .analyzer import (
    BaseAnalyzer,
    AnalysisResult,
)
from .common import (
    Info,
    ParameterDetailInfo,
    VariableInfo,
    FunctionInfo,
    ClassInfo,
    DataType,
    CustomDataType,
    ModuleStructure,
    DataTypeRefiner,
    EntryPoint,
)
from .utils import (
    LOG_LEVEL_DEBUG,
    remove_unencodable,
    output_log,
    LOG_LEVEL_WARN,
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
        self._code_data: str = ""
        self._buffer: str = ""

    def add(self, code: str, new_line: bool = False):
        self._buffer += code
        if new_line:
            indent = CodeWriterIndent.current_indent()
            self._code_data += f"{INDENT * indent}{self._buffer}\n"
            self._buffer = ""

    def addln(self, code: str):
        self.add(code, True)

    def new_line(self, num: int = 1):
        indent = CodeWriterIndent.current_indent()
        if self._buffer != "":
            line_break = "\n" * num
            self._code_data += f"{INDENT * indent}{self._buffer}{line_break}"
        else:
            self._code_data += "\n" * num
        self._buffer = ""

    def write(self, file):
        file.write(self._code_data)

    def reset(self):
        self._code_data: str = ""
        self._buffer: str = ""

    def format(self, style_config: str):
        self._code_data = FormatCode(
            self._code_data, style_config=style_config)[0]


class BaseGenerator:
    def __init__(self):
        self._writer: 'CodeWriter' = CodeWriter()

    def _gen_function_code(self, info: Info):
        data = info.to_dict()
        wt = self._writer

        wt.add("def " + data["name"] + "(")
        for i, p in enumerate(data["parameters"]):
            sp = p.split("=")
            default_value = None
            if len(sp) == 2:
                name = sp[0]
                default_value = sp[1]
            elif len(sp) == 1:
                name = sp[0]
            else:
                raise RuntimeError(f"Invalid format of parameter '{p}'")
            pd_matched = None
            for pd in data["parameter_details"]:
                if (pd["name"] == name) and (pd["data_type"] is not None) and \
                        (pd["data_type"] != ""):
                    pd_matched = pd
                    break
            if pd_matched is not None:
                if default_value is not None:
                    wt.add(f"{pd_matched['name']}: "
                           f"{pd_matched['data_type']}="
                           f"{pd_matched['default_value']}")
                else:
                    wt.add(f"{pd_matched['name']}: {pd_matched['data_type']}")
            else:
                wt.add(p)

            if i != len(data["parameters"]) - 1:
                wt.add(", ")
        if data["return"]["data_type"] == "":
            wt.addln("):")
        else:
            wt.addln(f") -> {data['return']['data_type']}:")

        with CodeWriterIndent(1):
            # documentation
            wt.add(f"''' {data['description']}")
            wt.new_line(2)
            for p in data["parameter_details"]:
                if p["description"] != "":
                    wt.addln(f":param {p['name']}: {p['description']}")
                if p["data_type"] != "":
                    wt.addln(f":type {p['name']}: {p['data_type']}")
            if data["return"]["data_type"] != "":
                wt.addln(f":rtype: {data['return']['data_type']}")
            if data["return"]["description"] != "":
                wt.addln(f":return: {data['return']['description']}")
            wt.addln("'''")
            wt.new_line(1)
            wt.addln("pass")
            wt.new_line(2)

    def _gen_class_code(self, info: Info):
        data = info.to_dict()
        wt = self._writer

        if len(data["base_classes"]) == 0:
            wt.addln(f"class {data['name']}:")
        else:
            base_classes = ", ".join(data["base_classes"]).replace("'", "")
            wt.addln(f"class {data['name']}({base_classes}):")

        with CodeWriterIndent(1):
            if data["description"] != "":
                wt.addln(f"''' {data['description']}")
                wt.addln("'''")
                wt.new_line(1)

            for a in data["attributes"]:
                if a["data_type"] != "":
                    wt.addln(f"{a['name']}: {a['data_type']} = None")
                else:
                    wt.addln(f"{a['name']} = None")
                wt.add("''' ")
                if a["description"] != "":
                    wt.add(f"{a['description']}")
                if a["data_type"] != "":
                    wt.new_line(2)
                    wt.addln(f":type: {a['data_type']}")
                wt.addln("'''")
                wt.new_line(1)
            if len(data["attributes"]) > 0:
                wt.new_line(1)

            for m in data["methods"]:
                if m["type"] == "method":
                    if len(m["parameters"]) > 0:
                        wt.add(f"def {m['name']}(self, ")
                    else:
                        wt.add(f"def {m['name']}(self")
                elif m["type"] == "classmethod":
                    if len(m["parameters"]) > 0:
                        wt.addln("@classmethod")
                        wt.add(f"def {m['name']}(cls, ")
                    else:
                        wt.addln("@classmethod")
                        wt.add(f"def {m['name']}(cls")
                elif m["type"] == "staticmethod":
                    if len(m["parameters"]) > 0:
                        wt.addln("@staticmethod")
                        wt.add(f"def {m['name']}(")
                    else:
                        wt.addln("@staticmethod")
                        wt.add(f"def {m['name']}(")
                for i, p in enumerate(m["parameters"]):
                    sp = p.split("=")
                    default_value = None
                    if len(sp) == 2:
                        name = sp[0]
                        default_value = sp[1]
                    elif len(sp) == 1:
                        name = sp[0]
                    else:
                        raise RuntimeError(
                            f"Invalid format of parameter '{p}'")
                    pd_matched = None
                    for pd in m["parameter_details"]:
                        if (pd["name"] == name) and \
                                (pd["data_type"] is not None) and \
                                (pd["data_type"] != ""):
                            pd_matched = pd
                            break
                    if pd_matched is not None:
                        if default_value is not None:
                            wt.add(
                                f"{pd_matched['name']}: "
                                f"{pd_matched['data_type']}="
                                f"{pd_matched['default_value']}")
                        else:
                            wt.add(f"{pd_matched['name']}: "
                                   f"{pd_matched['data_type']}")
                    else:
                        wt.add(p)

                    if i != len(m["parameters"]) - 1:
                        wt.add(", ")
                if m["return"]["data_type"] == "":
                    wt.addln("):")
                else:
                    wt.addln(f") -> {m['return']['data_type']}:")

                with CodeWriterIndent(2):
                    # documentation
                    wt.addln(f"''' {m['description']}")
                    wt.new_line(1)
                    for p in m["parameter_details"]:
                        wt.addln(f":param {p['name']}: {p['description']}")
                        wt.addln(f":type {p['name']}: {p['data_type']}")
                    if m["return"]["data_type"] != "":
                        wt.addln(f":rtype: {m['return']['data_type']}")
                    if m["return"]["description"] != "":
                        wt.addln(f":return: {m['return']['description']}")
                    wt.addln("'''")

                    wt.addln("pass")
                    wt.new_line()

            if len(data["attributes"]) == 0 and len(data["methods"]) == 0:
                wt.addln("pass")
                wt.new_line(2)

    def _gen_constant_code(self, info: Info):
        data = info.to_dict()
        wt = self._writer

        if data["data_type"] != "":
            wt.addln(f"{data['name']}: {data['data_type']} = None")
        else:
            wt.addln(f"{data['name']} = None")
        if data["description"] != "":
            wt.addln(f"''' {remove_unencodable(data['description'])}")
            wt.addln("'''")
        wt.new_line(2)

    def print_header(self, file):
        pass

    def _is_relative_import(self, mod_name: str):
        return mod_name[0] == "."

    def pre_process(self, _: str, gen_info: 'GenerationInfoByTarget'):
        processed = GenerationInfoByTarget()
        processed.name = gen_info.name
        processed.child_modules = gen_info.child_modules
        processed.dependencies = gen_info.dependencies
        processed.external_modules = gen_info.external_modules

        for d in gen_info.data:
            processed.data.append(d)

        return processed

    def _sorted_generation_info(
            self, data: 'GenerationInfoByTarget') -> List[Info]:
        class_data: List[ClassInfo] = []
        function_data: List[FunctionInfo] = []
        constant_data: List[VariableInfo] = []
        high_priority_class_data: List[ClassInfo] = []
        for d in data.data:
            # TODO: use class variable instead of "class", "function",
            #       "constant"
            if d.type() == "class":
                if d.name() in ("bpy_prop_collection", "bpy_prop_array",
                                "bpy_struct"):
                    high_priority_class_data.append(d)
                else:
                    class_data.append(d)
            elif d.type() == "function":
                function_data.append(d)
            elif d.type() == "constant":
                constant_data.append(d)
            else:
                raise ValueError(f"Invalid data type. ({d.type})")
        class_data = high_priority_class_data \
            + sorted(class_data, key=lambda x: x.name())

        # Sort class data (with class inheritance dependencies)
        graph = DAG()
        class_name_to_nodes = OrderedDict()
        for class_ in class_data:
            class_name_to_nodes[class_.name()] = graph.make_node(class_)
        for class_ in class_data:
            class_node = class_name_to_nodes[class_.name()]
            for base_class in class_.base_classes():
                if base_class.type() == 'MIXIN':
                    raise ValueError(
                        "DataType of base class must not be MixinDataType.")
                if base_class.type() == 'UNKNOWN':
                    continue

                if base_class.data_type() == class_.name():
                    output_log(
                        LOG_LEVEL_DEBUG,
                        f"Self dependency {base_class.data_type()} is found.")
                    continue

                base_class_node = class_name_to_nodes.get(
                    base_class.data_type())
                if base_class_node:
                    graph.make_edge(base_class_node, class_node)
                else:
                    output_log(
                        LOG_LEVEL_WARN,
                        f"Base class node (type={base_class.data_type()}) is "
                        "not found")
        sorted_nodes = topological_sort(graph)
        sorted_class_data = [node.data() for node in sorted_nodes]

        # Sort base classes
        order = {}
        for i, class_ in enumerate(sorted_class_data):
            order[class_.name()] = i
        for class_ in sorted_class_data:
            def sort_func(x):
                if x.type() == 'UNKNOWN':
                    return 0
                if x.data_type() not in order:
                    return 0
                return -order[x.data_type()]

            new_base_classes = sorted(class_.base_classes(), key=sort_func)
            for i, c in enumerate(new_base_classes):
                class_.set_base_class(i, c)

        # Sort function data
        sorted_function_data = sorted(function_data, key=lambda x: x.name())

        # Sort constant data
        sorted_constant_data = sorted(constant_data, key=lambda x: x.name())

        # Merge
        sorted_data = sorted_class_data
        sorted_data.extend(sorted_function_data)
        sorted_data.extend(sorted_constant_data)

        return sorted_data

    def generate(self,
                 filename: str,
                 data: 'GenerationInfoByTarget',
                 style_config: str = 'pep8'):
        # At first, sort data to avoid generating large diff.
        # Note: Base class must be located above derived class
        sorted_data = self._sorted_generation_info(data)

        with open(filename, "w", encoding="utf-8", newline="\n") as file:
            self.print_header(file)

            wt = self._writer
            wt.reset()

            # import external depended modules
            for ext in data.external_modules:
                wt.addln(f"import {ext}")

            # import depended modules
            for dep in data.dependencies:
                mod_name = dep.mod_name
                if self._is_relative_import(mod_name):
                    wt.add(f"from {mod_name} import (")
                    for i, type_ in enumerate(dep.type_lists):
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
            for mod in data.child_modules:
                wt.addln(f"from . import {mod}")
            if len(data.child_modules) > 0:
                wt.new_line()

            if (len(data.dependencies) > 0) or (len(data.child_modules) > 0):
                wt.new_line()

            # for generic type
            wt.new_line()
            wt.addln('GenericType = typing.TypeVar("GenericType")')

            for info in sorted_data:
                if info.type() == "function":
                    self._gen_function_code(info)
                elif info.type() == "class":
                    self._gen_class_code(info)
                elif info.type() == "constant":
                    self._gen_constant_code(info)

            if style_config != "none":
                wt.format(style_config)
                wt.write(file)
            else:
                wt.write(file)

    def dump_json(self, filename: str, data: 'GenerationInfoByTarget'):
        json_data = [info.to_dict() for info in data.data]
        with open(filename, "w", newline="\n", encoding="utf-8") as f:
            json.dump(json_data, f, indent=4)


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
        self.data: List[Info] = []
        self.child_modules: List[str] = []
        self.dependencies: List['Dependency'] = []
        self.external_modules: List[str] = ["sys", "typing"]


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
        self.style_format: str = "pep8"
        self.dump: bool = False
        self.target: str = "blender"
        self.target_version: str = None
        self.mod_version: str = None


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
        self._generation_info: Dict['PackageGenerationRule', 'GenerationInfoByRule'] = {}   # noqa # pylint: disable=C0301
        self._entry_points: List['EntryPoint'] = []

    # build package structure
    def _build_package_structure(self):
        analyze_result = self._analyze()

        # collect module list
        module_list = []
        for result in analyze_result.values():
            module_list.extend(self._collect_module_list(result))
        return self._build_module_structure(module_list)

    def _analyze(self) -> Dict['PackageGenerationRule', AnalysisResult]:
        result = {}
        for rule in self._rules:
            result[rule] = self._analyze_by_rule(rule)

        return result

    def _analyze_by_rule(
            self, rule: 'PackageGenerationRule') -> AnalysisResult:
        # replace windows path separator
        target_files = [f.replace("\\", "/") for f in rule.target_files()]
        # analyze all .rst files
        rule.analyzer().set_target(self._config.target)
        rule.analyzer().set_target_version(self._config.target_version)
        result = rule.analyzer().analyze(target_files)

        return result

    # build module structure
    def _build_module_structure(self, modules) -> 'ModuleStructure':
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
    def _collect_module_list(
            self, analyze_result: AnalysisResult) -> List[str]:
        module_list = []
        for section in analyze_result.section_info:
            for info in section.info_list:
                if info.module() is None:
                    output_log(
                        LOG_LEVEL_WARN, f"{info.name()}'s module is None")
                    continue
                if info.module() not in module_list:
                    module_list.append(info.module())

        return module_list

    def _build_entry_points(self) -> List['EntryPoint']:
        # at first analyze without DataTypeRefiner
        generation_info: Dict['PackageGenerationRule', 'GenerationInfoByRule'] = {}     # noqa # pylint: disable=C0301
        for rule in self._rules:
            analyze_result = self._analyze_by_rule(rule)
            module_structure = self._build_module_structure(
                self._collect_module_list(analyze_result))
            generation_info[rule] = self._build_generation_info_internal(
                analyze_result, module_structure)

        # build entry points
        entry_points = []
        for gen_info in generation_info.values():
            for target in gen_info.targets():
                info = gen_info.get_target(target)
                for data in info.data:
                    if data.type() not in ["class", "constant", "function"]:
                        continue
                    entry = EntryPoint()
                    entry.type = data.type()
                    entry.module = info.name
                    entry.name = data.name()
                    entry_points.append(entry)
        return entry_points

    def _build_generation_info_internal(
            self, analyze_result: AnalysisResult,
            module_structure: 'ModuleStructure') -> 'GenerationInfoByRule':
        def find_target_file(
                name: str, structure: 'ModuleStructure', target: str) -> str:
            for m in structure.children():
                mod_name = name + m.name
                if mod_name == target:
                    if len(m.children()) == 0:
                        return mod_name + ".py"
                    return mod_name + "/__init__.py"

                if len(m.children()) > 0:
                    ret = find_target_file(mod_name + "/", m, target)
                    if ret:
                        return ret
            return None

        def build_child_modules(
                gen_info: 'GenerationInfoByRule', name: str,
                structure: 'ModuleStructure'):
            for m in structure.children():
                mod_name = name + m.name
                if len(m.children()) == 0:
                    filename = re.sub(r"\.", "/", mod_name) + ".py"
                    info = gen_info.create_target(filename)
                    info.data = []
                    info.child_modules = []
                    info.name = mod_name
                else:
                    filename = re.sub(r"\.", "/", mod_name) + "/__init__.py"
                    info = gen_info.create_target(filename)
                    info.data = []
                    info.child_modules = [child.name for child in m.children()]
                    info.name = mod_name
                    build_child_modules(gen_info, mod_name + ".", m)

        # build child modules
        generator_info = GenerationInfoByRule()
        build_child_modules(generator_info, "", module_structure)

        # build data
        for section in analyze_result.section_info:
            for info in section.info_list:
                target = find_target_file("", module_structure,
                                          re.sub(r"\.", "/", info.module()))
                if target is None:
                    raise RuntimeError("Could not find target file to "
                                       f"generate (target: {info.module()})")
                gen_info = generator_info.get_target(target)
                gen_info.data.append(info)

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
                        data_type_1: DataType, data_type_2: str):
        if data_type_1.type() == 'UNKNOWN':
            return
        if data_type_1.type() == 'BUILTIN':
            return
        if data_type_1.type() == 'MODIFIER':
            return

        def register_dependency(dtype: str):
            mod = self._get_import_module_path(refiner, dtype, data_type_2)
            base = refiner.get_base_name(dtype)
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

        if data_type_1.type() == 'MIXIN':
            for d in data_type_1.data_types():
                self._add_dependency(dependencies, refiner, d, data_type_2)
        else:
            if data_type_1.has_modifier() and \
                    data_type_1.modifier().type() == 'CUSTOM_MODIFIER':
                register_dependency(
                    data_type_1.modifier().modifier_data_type())
            register_dependency(data_type_1.data_type())

    def _build_dependencies(
            self, package_structure: 'ModuleStructure',
            entry_points: List['EntryPoint'],
            info: 'GenerationInfoByTarget') -> List['Dependency']:
        refiner = DataTypeRefiner(package_structure, entry_points)

        dependencies = []
        for data in info.data:
            if data.type() == "function":
                for p in data.parameter_details():
                    self._add_dependency(
                        dependencies, refiner, p.data_type(),
                        data.module() + "." + data.name())
                r = data.return_()
                if r is not None:
                    self._add_dependency(
                        dependencies, refiner, r.data_type(),
                        data.module() + "." + data.name())
            elif data.type() == "constant":
                self._add_dependency(
                    dependencies, refiner, data.data_type(),
                    data.module() + "." + data.name())
            elif data.type() == "class":
                for m in data.methods():
                    for p in m.parameter_details():
                        self._add_dependency(
                            dependencies, refiner, p.data_type(),
                            data.module() + "." + data.name())
                    r = m.return_()
                    if r is not None:
                        self._add_dependency(
                            dependencies, refiner, r.data_type(),
                            data.module() + "." + data.name())
                for a in data.attributes():
                    self._add_dependency(
                        dependencies, refiner, a.data_type(),
                        data.module() + "." + data.name())
                for c in data.base_classes():
                    self._add_dependency(
                        dependencies, refiner, c,
                        data.module() + "." + data.name())

        return dependencies

    def _refine_data_type(
            self, refiner: 'DataTypeRefiner',
            analysis_result: AnalysisResult):

        def get_parameter_from_parameter_detail(
                parameters: List[str],
                parameter_detail: ParameterDetailInfo) -> str:

            for param in parameters:
                param_str = param
                m = re.match(r"^([a-zA-Z0-9_]+?)[=:]", param_str)
                if m:
                    param_str = m.group(1)
                if param_str == parameter_detail.name():
                    return param

            return None

        data_to_refine: List[Info] = []
        for section in analysis_result.section_info:
            data_to_refine.extend(list(section.info_list))
        for info in tqdm(data_to_refine):
            # refine function parameters and return value
            if info.type() == "function":
                p: ParameterDetailInfo
                for p in info.parameter_details():
                    parameter = get_parameter_from_parameter_detail(
                        info.parameters(), p)
                    refined_type = refiner.get_refined_data_type(
                        p.data_type(), info.module(), 'FUNC_ARG',
                        parameter_str=parameter)
                    p.set_data_type(refined_type)

                return_ = info.return_()
                if return_ is not None:
                    refined_type = refiner.get_refined_data_type(
                        return_.data_type(), info.module(), 'FUNC_RET')
                    return_.set_data_type(refined_type)
            # refine constant
            elif info.type() == "constant":
                refined_type = refiner.get_refined_data_type(
                    info.data_type(), info.module(), 'CONST')
                info.set_data_type(refined_type)
            # refine class attributes and method parameters and return value
            elif info.type() == "class":
                for a in info.attributes():
                    refined_type = refiner.get_refined_data_type(
                        a.data_type(), info.module(), 'CLS_ATTR',
                        additional_info={
                            "self_class": f"{info.module()}.{info.name()}"
                        })
                    a.set_data_type(refined_type)
                for m in info.methods():
                    p: ParameterDetailInfo
                    for p in m.parameter_details():
                        parameter = get_parameter_from_parameter_detail(
                            m.parameters(), p)
                        refined_type = refiner.get_refined_data_type(
                            p.data_type(), info.module(), 'FUNC_ARG',
                            parameter_str=parameter,
                            additional_info={
                                "self_class": f"{info.module()}.{info.name()}"
                            })
                        p.set_data_type(refined_type)

                    return_ = m.return_()
                    if return_ is not None:
                        refined_type = refiner.get_refined_data_type(
                            return_.data_type(), info.module(), 'FUNC_RET',
                            additional_info={
                                "self_class": f"{info.module()}.{info.name()}"
                            })
                        return_.set_data_type(refined_type)
                for i, c in enumerate(info.base_classes()):
                    refined_type = refiner.get_refined_data_type(
                        c, info.module(), 'CLS_BASE',
                        additional_info={
                            "self_class": f"{info.module()}.{info.name()}"
                        })
                    info.set_base_class(i, refined_type)

    def _remove_duplicate(
            self,
            gen_info: 'GenerationInfoByTarget') -> 'GenerationInfoByTarget':
        processed_info = GenerationInfoByTarget()
        processed_info.name = gen_info.name
        processed_info.external_modules = gen_info.external_modules
        processed_info.dependencies = gen_info.dependencies
        processed_info.child_modules = gen_info.child_modules

        # remove duplicate constant
        for d1 in gen_info.data:
            if d1.type() != "constant":
                processed_info.data.append(d1)
                continue

            found = False
            for d2 in processed_info.data:
                if (d1.type() == d2.type()) and (d1.name() == d2.name()):
                    found = True
                    break
            if not found:
                processed_info.data.append(d1)

        # remove duplicate attributes of class
        for d in processed_info.data:
            if d.type() != "class":
                continue

            new_attributes: List[VariableInfo] = []
            for a1 in d.attributes():
                found = False
                for a2 in new_attributes:
                    if (a1.type() == a2.type()) and (a1.name() == a2.name()):
                        found = True
                        break
                if not found:
                    new_attributes.append(a1)
            d.set_attributes(new_attributes)

        # TODO: check class-method/function as well. But be careful to remove
        # duplicate because of override method is allowed

        return processed_info

    def _rewrite_data_type(
            self, refiner: 'DataTypeRefiner',
            gen_info: 'GenerationInfoByTarget') -> 'GenerationInfoByTarget':
        processed_info = GenerationInfoByTarget()
        processed_info.name = gen_info.name
        processed_info.external_modules = gen_info.external_modules
        processed_info.dependencies = gen_info.dependencies
        processed_info.child_modules = gen_info.child_modules

        def rewrite_for_custom(data_type: 'CustomDataType'):
            new_data_type = refiner.get_generation_data_type(
                data_type.data_type(), gen_info.name)
            dt = CustomDataType(
                new_data_type, data_type.modifier(),
                data_type.modifier_add_info())
            dt.set_is_optional(data_type.is_optional())
            dt.set_metadata(data_type.get_metadata())
            return dt

        def rewrite_for_custom_modifier(data_type: 'CustomDataType'):
            new_modifier_name = refiner.get_generation_data_type(
                data_type.modifier().output_modifier_name(), gen_info.name)
            dt = data_type
            dt.modifier().set_output_modifier_name(new_modifier_name)
            return dt

        def rewrite_for_tuple_elms(data_type: 'CustomDataType'):
            dt = data_type
            if dt.modifier().modifier_data_type() == 'tuple':
                add_info = dt.modifier_add_info()
                elms_old = add_info["tuple_elms"]
                elms_new = []
                for elm_old in elms_old:
                    if elm_old.type() == 'CUSTOM':
                        elm_new = rewrite_for_custom(elm_old)
                        elms_new.append(elm_new)
                    else:
                        elms_new.append(elm_old)
                add_info["tuple_elms"] = elms_new
            return dt

        def rewrite(info_to_rewrite: Info):
            dtype_to_rewrite = info_to_rewrite.data_type()
            if dtype_to_rewrite.type() == 'BUILTIN':
                if dtype_to_rewrite.has_modifier():
                    modifier = dtype_to_rewrite.modifier()
                    if modifier.type() == 'MODIFIER':
                        rewrite_for_tuple_elms(dtype_to_rewrite)
                    elif modifier.type() == 'CUSTOM_MODIFIER':
                        info_to_rewrite.set_data_type(
                            rewrite_for_custom_modifier(dtype_to_rewrite))
            elif dtype_to_rewrite.type() == 'CUSTOM':
                dt = rewrite_for_custom(dtype_to_rewrite)
                if dt.has_modifier():
                    if dt.modifier().type() == 'MODIFIER':
                        dt = rewrite_for_tuple_elms(dt)
                    elif dt.modifier().type() == 'CUSTOM_MODIFIER':
                        dt = rewrite_for_custom_modifier(dt)
                info_to_rewrite.set_data_type(dt)
            elif dtype_to_rewrite.type() == 'MIXIN':
                mixin_dt = dtype_to_rewrite
                for i, d in enumerate(mixin_dt.data_types()):
                    if d.type() == 'BUILTIN':
                        if d.has_modifier():
                            if d.modifier().type() == 'MODIFIER':
                                rewrite_for_tuple_elms(d)
                            elif d.modifier().type() == 'CUSTOM_MODIFIER':
                                mixin_dt.set_data_type(
                                    i, rewrite_for_custom_modifier(d))
                    elif d.type() == 'CUSTOM':
                        dt = rewrite_for_custom(d)
                        if dt.has_modifier():
                            if dt.modifier().type() == 'MODIFIER':
                                rewrite_for_tuple_elms(dt)
                            elif dt.modifier().type() == 'CUSTOM_MODIFIER':
                                dt = rewrite_for_custom_modifier(dt)
                        mixin_dt.set_data_type(i, dt)

        for info in gen_info.data:
            # rewrite function parameters and return value
            if info.type() == "function":
                for p in info.parameter_details():
                    rewrite(p)

                return_ = info.return_()
                if return_ is not None:
                    rewrite(return_)

            # rewrite constant
            elif info.type() == "constant":
                rewrite(info)

            # rewrite class attributes and method parameters and return value
            elif info.type() == "class":
                for a in info.attributes():
                    rewrite(a)

                for m in info.methods():
                    for p in m.parameter_details():
                        rewrite(p)

                    return_ = m.return_()
                    if return_ is not None:
                        rewrite(return_)

                for i, c in enumerate(info.base_classes()):
                    if c.type() == 'CUSTOM':
                        dt = rewrite_for_custom(c)
                        if dt.has_modifier() and \
                                dt.modifier().type() == 'CUSTOM_MODIFIER':
                            dt = rewrite_for_custom_modifier(dt)
                        info.set_base_class(i, dt)
                    elif c.type() == 'MIXIN':
                        raise ValueError(
                            "Base classes must not be MixinDataType (Class: "
                            f"{info.module()}.{info.name()}, "
                            f"Data type: {c.to_string()})")

            processed_info.data.append(info)

        return processed_info

    def _add_keyword_only_argument(
            self,
            gen_info: 'GenerationInfoByTarget') -> 'GenerationInfoByTarget':
        processed_info = GenerationInfoByTarget()
        processed_info.name = gen_info.name
        processed_info.external_modules = gen_info.external_modules
        processed_info.dependencies = gen_info.dependencies
        processed_info.child_modules = gen_info.child_modules

        def fix(params: List[str]) -> List[str]:
            found_default_arg = False
            keyword_only_arg_position = -1
            for i, p in enumerate(params):
                if "=" in p:
                    found_default_arg = True
                else:
                    if found_default_arg and keyword_only_arg_position == -1:
                        keyword_only_arg_position = i - 1

            fixed_params = []
            for i, p in enumerate(params):
                fixed_params.append(p)
                if i == keyword_only_arg_position:
                    fixed_params.append("*")

            return fixed_params

        for info in gen_info.data:
            if info.type() == "function":
                info.set_parameters(fix(info.parameters()))

            elif info.type() == "class":
                for m in info.methods():
                    m.set_parameters(fix(m.parameters()))

            processed_info.data.append(info)

        return processed_info

    def _remove_type_hint(
            self,
            gen_info: 'GenerationInfoByTarget') -> 'GenerationInfoByTarget':
        processed_info = GenerationInfoByTarget()
        processed_info.name = gen_info.name
        processed_info.external_modules = gen_info.external_modules
        processed_info.dependencies = gen_info.dependencies
        processed_info.child_modules = gen_info.child_modules

        def fix(params: List[str]) -> List[str]:
            fixed_params = []
            for p in params:
                m = re.search(r"[a-zA-Z0-9]+: [a-zA-Z0-9]", p)
                if m:
                    fixed_params.append(p[:m.start()+1])
                else:
                    fixed_params.append(p)

            return fixed_params

        for info in gen_info.data:
            if info.type() == "function":
                info.set_parameters(fix(info.parameters()))

            elif info.type() == "class":
                for m in info.methods():
                    m.set_parameters(fix(m.parameters()))

            processed_info.data.append(info)

        return processed_info

    # map between result of analyze and module structure
    def _build_generation_info(
            self, package_structure: 'ModuleStructure',
            entry_points: List['EntryPoint']) -> Dict[
                'PackageGenerationRule', 'GenerationInfoByRule']:
        generation_info: Dict['PackageGenerationRule', 'GenerationInfoByRule'] = {}     # noqa # pylint: disable=C0301
        for rule in self._rules:
            refiner = DataTypeRefiner(package_structure, entry_points)
            analyze_result = self._analyze_by_rule(rule)
            self._refine_data_type(refiner, analyze_result)

            module_structure = self._build_module_structure(
                self._collect_module_list(analyze_result))
            generation_info[rule] = self._build_generation_info_internal(
                analyze_result, module_structure)

            for target in generation_info[rule].targets():
                info = self._remove_duplicate(
                    generation_info[rule].get_target(target))
                info = self._rewrite_data_type(refiner, info)
                info = self._add_keyword_only_argument(info)
                info = self._remove_type_hint(info)
                generation_info[rule].update_target(target, info)

        return generation_info

    def package_structure(self) -> 'ModuleStructure':
        return self._package_structure

    def entry_points(self) -> List['EntryPoint']:
        return self._entry_points

    def generation_info(self) -> Dict['PackageGenerationRule', 'GenerationInfoByRule']:     # noqa # pylint: disable=C0301
        return self._generation_info

    def analyze(self):
        self._package_structure = self._build_package_structure()
        self._entry_points = self._build_entry_points()

        self._generation_info = self._build_generation_info(
            self._package_structure, self._entry_points)
        for gen_info in self._generation_info.values():
            for target in gen_info.targets():
                info = gen_info.get_target(target)
                info.dependencies = self._build_dependencies(
                    self._package_structure, self._entry_points, info)


class PackageGenerator:
    def __init__(self, config: 'PackageGeneratorConfig'):
        self._config: 'PackageGeneratorConfig' = config
        self._rules: List['PackageGenerationRule'] = []

    # create module directories/files
    def _create_empty_modules(self, package_structure: 'ModuleStructure'):
        def make_module_dirs(base_path: str, structure: 'ModuleStructure'):
            def make_dir(path, structure_: 'ModuleStructure'):
                for item in structure_.children():
                    if len(item.children()) >= 1:
                        dir_path = path + "/" + item.name
                        pathlib.Path(dir_path).mkdir(
                            parents=True, exist_ok=True)
                        self._create_py_typed_file(dir_path)
                        if dir_path == base_path:
                            continue
                        make_dir(dir_path, item)

            make_dir(base_path, structure)

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
            self, package_strcuture: 'ModuleStructure',
            generation_info: Dict['PackageGenerationRule', 'GenerationInfoByRule']):    # noqa # pylint: disable=C0301
        for rule in generation_info.keys():
            self._generate_by_rule(
                rule, package_strcuture, generation_info[rule])

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
        self._generate(
            analyzer.package_structure(), analyzer.generation_info())
