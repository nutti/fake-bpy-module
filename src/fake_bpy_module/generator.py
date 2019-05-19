import json
import re
import pathlib
from yapf.yapflib.yapf_api import FormatCode
from typing import List, Dict

from .info import (
    Info,
)
from .analyzer import (
    DataTypeRefiner,
    BaseAnalyzer,
)
from .utils import (
    remove_unencodable,
)

INDENT = "    "


class CodeWriterIndent:
    indent_stack: List[int] = [0]

    def __init__(self, indent: int=0):
        self._indent: int = indent

    def __enter__(self):
        self.indent_stack.append(self._indent)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.indent_stack.pop()

    @classmethod
    def current_indent(self) -> int:
        return self.indent_stack[-1]


class CodeWriter:
    def __init__(self):
        self.reset()

    def add(self, code: str, new_line: bool=False):
        self._buffer += code
        if new_line:
            indent = CodeWriterIndent.current_indent()
            self._code_data += "{}{}\n".format(INDENT * indent, self._buffer)
            self._buffer = ""

    def addln(self, code: str):
        self.add(code, True)

    def new_line(self, num: int=1):
        indent = CodeWriterIndent.current_indent()
        if self._buffer != "":
            self._code_data += "{}{}{}".format(INDENT * indent, self._buffer, "\n" * num)
        else:
            self._code_data += "\n" * num
        self._buffer = ""

    def write(self, file):
        file.write(self._code_data)

    def reset(self):
        self._code_data: str = ""
        self._buffer: str = ""

    def format(self, style_config):
        self._code_data = FormatCode(self._code_data, style_config=style_config)[0]


class BaseGenerator:
    def __init__(self):
        self.mod_name: str = None
        self.data_type_refiner: DataTypeRefiner = None
        self._writer: CodeWriter = CodeWriter()

    def _rewrite_data_type(self, data_type):
        result = data_type
        if self.data_type_refiner is not None:
            # TODO: should not to use fake
            result = self.data_type_refiner.get_generation_data_type(
                result, self.mod_name + ".fake")
            result = self.data_type_refiner.make_annotate_data_type(result)
        return result

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
                raise RuntimeError("Invalid format of parameter '{}'".format(p))
            pd_matched = None
            for pd in data["parameter_details"]:
                if (pd["name"] == name) and (pd["data_type"] is not None) and (pd["data_type"] != ""):
                    pd_matched = pd
                    break
            if pd_matched is not None:
                if default_value is not None:
                    wt.add("{}: {}={}"
                           .format(pd_matched["name"],
                                   self._rewrite_data_type(pd_matched["data_type"]),
                                   default_value))
                else:
                    wt.add("{}: {}"
                           .format(pd_matched["name"],
                                   self._rewrite_data_type(pd_matched["data_type"])))
            else:
                wt.add(p)

            if i != len(data["parameters"]) - 1:
                wt.add(", ")
        if data["return"]["data_type"] == "":
            wt.addln("):")
        else:
            wt.addln(") -> {}:"
                     .format(self._rewrite_data_type(data["return"]["data_type"])))

        with CodeWriterIndent(1):
            # documentation
            wt.add("'''{}".format(data["description"]))
            wt.new_line(2)
            for p in data["parameter_details"]:
                if p["description"] != "":
                    wt.addln(":param {}: {}".format(p["name"], p["description"]))
                if p["data_type"] != "":
                    wt.addln(":type {}: {}".format(p["name"], p["data_type"]))
            if data["return"]["description"] != "":
                wt.addln(":return: {}".format(data["return"]["description"]))
            wt.addln("'''")
            wt.new_line(1)
            wt.addln("pass")
            wt.new_line(2)

    def _gen_class_code(self, info: Info):
        data = info.to_dict()
        # if data["name"] is None:
        #     output_log(
        #         LOG_LEVEL_WARN, "Invalid data name. (data={})".format(data)
        #     )
        #     return
        wt = self._writer

        wt.addln("class {}:".format(data["name"]))

        with CodeWriterIndent(1):
            if data["description"] != "":
                wt.addln("'''{}'''".format(data["description"]))
                wt.new_line(1)

            for a in data["attributes"]:
                if a["data_type"] != "":
                    wt.addln("{}: {} = None"
                             .format(a["name"], self._rewrite_data_type(a["data_type"])))
                else:
                    wt.addln("{} = None".format(a["name"]))
                wt.add("'''")
                if a["description"] != "":
                    wt.add("{}".format(a["description"]))
                if a["data_type"] != "":
                    wt.new_line(2)
                    wt.addln(":type: {}".format(a["data_type"]))
                wt.addln("'''")
                wt.new_line(1)
            if len(data["attributes"]) > 0:
                wt.new_line(1)

            for m in data["methods"]:
                if len(m["parameters"]) > 0:
                    wt.add("def {}(self, ".format(m["name"]))
                else:
                    wt.add("def {}(self".format(m["name"]))
                for i, p in enumerate(m["parameters"]):
                    sp = p.split("=")
                    default_value = None
                    if len(sp) == 2:
                        name = sp[0]
                        default_value = sp[1]
                    elif len(sp) == 1:
                        name = sp[0]
                    else:
                        raise RuntimeError("Invalid format of parameter '{}'".format(p))
                    pd_matched = None
                    for pd in m["parameter_details"]:
                        if (pd["name"] == name) and ((pd["data_type"] is not None) and (pd["data_type"] != "")):
                            pd_matched = pd
                            break
                    if pd_matched is not None:
                        if default_value is not None:
                            wt.add("{}: {}={}"
                                   .format(pd_matched["name"],
                                           self._rewrite_data_type(pd_matched["data_type"]),
                                           default_value))
                        else:
                            wt.add("{}: {}"
                                   .format(pd_matched["name"],
                                           self._rewrite_data_type(pd_matched["data_type"])))
                    else:
                        wt.add(p)

                    if i != len(m["parameters"]) - 1:
                        wt.add(", ")
                if m["return"]["data_type"] == "":
                    wt.addln("):")
                else:
                    wt.addln(") -> {}:"
                             .format(self._rewrite_data_type(m["return"]["data_type"])))

                with CodeWriterIndent(2):
                # documentation
                    wt.addln("'''{}".format(m["description"]))
                    wt.new_line(1)
                    for p in m["parameter_details"]:
                        wt.addln(":param {}: {}"
                                 .format(p["name"], p["description"]))
                        wt.addln(":type {}: {}"
                                 .format(p["name"], p["data_type"]))
                    if m["return"]["data_type"] != "":
                        wt.addln(":rtype: {}"
                                 .format(m["return"]["data_type"]))
                    if m["return"]["description"] != "":
                        wt.addln(":return: {}"
                                 .format(m["return"]["description"]))
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
            wt.addln("{}: {} = None"
                     .format(data["name"], self._rewrite_data_type(data["data_type"])))
        else:
            wt.addln("{} = None".format(data["name"]))
        if data["description"] != "":
            wt.add("'''{}'''"
                   .format(remove_unencodable(data["description"])))
        wt.new_line(2)

    def print_header(self, file):
        pass

    def _is_relative_import(self, mod_name):
        return mod_name[0] == "."

    def set_data_type_refiner(self, refiner: DataTypeRefiner):
        self.data_type_refiner = refiner

    def generate(self,
                 filename: str,
                 data: 'GenerationInfoByTarget',
                 style_config: str='pep8'):
        self.mod_name = data.name

        # at first, sort data to avoid generating large diff
        sorted_data = sorted(
            data.data,
            key=lambda x : (x.type(), x.name())
        )

        with open(filename, "w", encoding="utf-8") as file:
            self.print_header(file)

            wt = self._writer
            wt.reset()

            # import external depended modules
            for ext in data.external_modules:
                wt.addln("import {}".format(ext))

            # import depended modules
            for dep in data.dependencies:
                mod_name = dep.mod_name
                if self._is_relative_import(mod_name):
                    wt.add("from {} import (".format(mod_name))
                    for i, type in enumerate(dep.type_lists):
                        wt.add(type)
                        if i == len(dep.type_lists) - 1:
                            wt.addln(")")
                        else:
                            wt.add(", ")
                else:
                    wt.addln("import {}".format(dep.mod_name))

            if len(data.dependencies) > 0:
                wt.new_line()

            # import child module to search child modules
            for mod in data.child_modules:
                wt.addln("from . import {}".format(mod))
            if len(data.child_modules) >= 1:
                wt.new_line(2)

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
        with open(filename, "w") as f:
            json.dump(json_data, f, indent=4)


# class BpyGenerator(BaseGenerator):
#     def print_header(self, file):
#         if self.mod_name == "bpy":
#             file.write("from .context import Context as context\n")
#             file.write("\n")

# def gen_bpy_context_skelton():
#     filename = "{}/bpy/context.py".format(OUTPUT_DIR)
#     with open(filename, "w", encoding="utf-8") as file:
#         file.write("class Context:\n")
#         file.write(INDENT + "# pylint: dynamic-attributes = .*\n")
#         file.write(INDENT + "def __init__(self, **kwargs):\n")
#         file.write(INDENT * 2 + "pass\n")


# build module structure
def build_module_structure(modules):
    def build(mod_name: str, structure_):
        sp = mod_name.split(".")
        for i in structure_:
            if i["name"] == sp[0]:
                item = i
                break
        else:
            item = {"name": sp[0], "children": []}
            structure_.append(item)
        if len(sp) >= 2:
            s = ".".join(sp[1:])
            build(s, item["children"])

    structure = []
    for m in modules:
        build(m, structure)

    return structure


def make_module_dirs(base_path: str, structure):
    def make_dir(path, structure_):
        for item in structure_:
            if len(item["children"]) >= 1:
                dir_path = path + "/" + item["name"]
                pathlib.Path(dir_path).mkdir(parents=True, exist_ok=True)
                if dir_path == base_path:
                    continue
                make_dir(dir_path, item["children"])

    make_dir(base_path, structure)


def find_mod(modules, xml_file):
    modname_raw = re.sub("\.", "/", xml_file.module())

    def find(name, mods, raw):
        for m in mods:
            mod_name = name + m["name"]
            if mod_name == raw:
                if len(m["children"]) == 0:
                    return mod_name + ".py"
                else:
                    return mod_name + "/__init__.py"
            if len(m["children"]) > 0:
                ret = find(mod_name + "/", m["children"], raw)
                if ret:
                    return ret

    return find("", modules, modname_raw)


def build_generation_info(analyze_results, module_structure) -> 'GenerationInfoByRule':
    def find_target_file(name, structure, target):
        for m in structure:
            mod_name = name + m["name"]
            if mod_name == target:
                if len(m["children"]) == 0:
                    return mod_name + ".py"
                else:
                    return mod_name + "/__init__.py"

            if len(m["children"]) > 0:
                ret = find_target_file(mod_name + "/", m["children"], target)
                if ret:
                    return ret
        return None

    def build_child_modules(gen_info: 'GenerationInfoByRule', name, structure):
        for m in structure:
            mod_name = name + m["name"]
            if len(m["children"]) == 0:
                filename = re.sub("\.", "/", mod_name) + ".py"
                info = gen_info.create_target(filename)
                info.data = []
                info.child_modules = []
                info.name = mod_name
            else:
                filename = re.sub("\.", "/", mod_name) + "/__init__.py"
                info = gen_info.create_target(filename)
                info.data = []
                info.child_modules = [child["name"] for child in m["children"]]
                info.name = mod_name
                build_child_modules(gen_info, mod_name + ".", m["children"])

    # build child modules
    generator_info = GenerationInfoByRule()
    build_child_modules(generator_info, "", module_structure)

    # build data
    for r in analyze_results:
        for sections in r:
            for s in sections:
                target = find_target_file("", module_structure,
                                          re.sub("\.", "/", s.module()))
                if target is None:
                    raise RuntimeError("Could not find target file to generate "
                                       "(target: {})".format(s.module()))
                info = generator_info.get_target(target)
                info.data.append(s)

    return generator_info


class PackageGenerationRule:
    def __init__(self, name: str, target_files: List[str],
                 analyzer: BaseAnalyzer, generator: BaseGenerator):
        self._name: str = name
        self._target_files: List[str] = target_files
        self._analyzer: BaseAnalyzer = analyzer
        self._generator: BaseGenerator = generator

    def name(self) -> str:
        return self._name

    def target_files(self) -> List[str]:
        return self._target_files

    def analyzer(self) -> BaseAnalyzer:
        return self._analyzer

    def generator(self) -> BaseGenerator:
        return self._generator


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
            raise RuntimeError("At least 1 element must be added to type lists")
        return self._type_lists

    def add_type(self, type: str):
        self._type_lists.append(type)


class DependencyBuilder:
    BUILTIN_DATA_TYPE: List[str] = [
        "bool", "str", "list", "bytes", "float", "dict", "int", "set"
    ]

    def __init__(self, refiner: DataTypeRefiner,
                 generation_info: Dict['PackageGenerationRule', 'GenerationInfoByRule']):
        self._dependencies: List[Dependency] = []
        self._refiner: DataTypeRefiner = refiner
        self._generation_info: Dict['PackageGenerationRule', 'GenerationInfoByRule'] = generation_info

    def _get_import_module_path(self, data_type_1: str, data_type_2: str):
        mod_names_full_1 = self._refiner.get_module_name(data_type_1)
        mod_names_full_2 = self._refiner.get_module_name(data_type_2)
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
        #       => bpy
        if match_level == 0:
            module_path = mod_names_1[0]
        else:
            rest_level_1 = len(mod_names_1) - match_level
            rest_level_2 = len(mod_names_2) - match_level

            # [Case 2] Match exactly => No need to import any modules
            #   data_type_1: bgl.Buffer
            #   data_type_2: bgl.glCallLists()
            #       => None
            if rest_level_1 == 0 and rest_level_2 == 0:
                module_path = None
            # [Case 3] Match partially (Same level) => Need to import top level
            #   data_type_1: bpy.types.Mesh
            #   data_type_2: bpy.ops.automerge()
            #       => bpy
            elif rest_level_1 >= 1 and rest_level_2 >= 1:
                module_path = mod_names_1[0]
            # [Case 4] Match partially (Upper level) => Need to import top level
            #   data_type_1: mathutils.Vector
            #   data_type_2: mathutils.noise.cell
            #       => mathutils
            elif rest_level_1 == 0 and rest_level_2 >= 1:
                module_path = mod_names_1[0]
            # [Case 5] Match partially (Lower level) => Need to import same level
            #   data_type_1: mathutils.noise.cell
            #   data_type_2: mathutils.Vector
            #       => .noise
            elif rest_level_1 >= 1 and rest_level_2 == 0:
                module_path = "." + mod_names_1[match_level]
            else:
                raise RuntimeError("Should not reach this condition.")

        return module_path

    def _add_dependency(self, dependencies: List['Dependency'],
                        data_type_1: str, data_type_2: str):
        if self._refiner.is_builtin_data_type(data_type_1):
            return

        mod = self._get_import_module_path(data_type_1, data_type_2)
        base = self._refiner.get_base_name(data_type_1)
        if mod is None:
            return

        target_dep: Dependency = None
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
            target_dep.add_type(base)


    def _build_dependencies(self):
        for rule in self._generation_info.keys():
            for target in self._generation_info[rule].targets():
                info = self._generation_info[rule].get_target(target)
                info.dependencies = []
                for data in info.data:
                    if data.type() == "function":
                        for p in data.parameter_details():
                            self._add_dependency(info.dependencies,
                                                 p.data_type(),
                                                 data.module() + "." + data.name())
                    elif data.type() == "constant":
                        self._add_dependency(info.dependencies,
                                             data.data_type(),
                                             data.module() + "." + data.name())
                    elif data.type() == "class":
                        for m in data.methods():
                            for p in m.parameter_details():
                                self._add_dependency(info.dependencies,
                                                     p.data_type(),
                                                     data.module() + "." + data.name())
                        for a in data.attributes():
                            self._add_dependency(info.dependencies,
                                                 a.data_type(),
                                                 data.module() + "." + data.name())

    def dependencies(self) -> List['Dependency']:
        return self._dependencies

    def build(self):
        self._build_dependencies()


class GenerationInfoByTarget:
    def __init__(self):
        self.name: str = None
        self.data: List[Info] = []
        self.child_modules: List[str] = []
        self.dependencies: List['Dependency'] = []
        self.external_modules: List[str] = ["sys"]


class GenerationInfoByRule:
    def __init__(self):
        self._info: Dict[str, 'GenerationInfoByTarget'] = {}

    def get_target(self, target: str) -> 'GenerationInfoByTarget':
        if target not in self._info.keys():
            raise RuntimeError("Could not find target in GenerationInfoByRule "
                               "(target: {})".format(target))
        return self._info[target]

    def create_target(self, target: str) -> 'GenerationInfoByTarget':
        self._info[target] = GenerationInfoByTarget()
        return self._info[target]

    def get_or_create_target(self, target: str):
        info = self.get_target(target)
        if info is None:
            info = self.create_target(target)
        return info

    def targets(self):
        return self._info.keys()


class PackageGeneratorConfig:
    def __init__(self):
        self.output_dir: str = "./out"
        self.os: str = "Linux"
        self.style_format: str = "pep8"
        self.dump: bool = False


class PackageGenerator:
    def __init__(self, config: PackageGeneratorConfig):
        self._config: PackageGeneratorConfig = config
        self._rules: List[PackageGenerationRule] = []
        self._package_structure = []
        self._generation_info: Dict['PackageGenerationRule', 'GenerationInfoByRule'] = {}
        self._entry_points = []

    def _analyze_by_rule(self, rule: PackageGenerationRule,
                         data_type_refiner: DataTypeRefiner=None):
        result = []
        # replace windows path separator
        target_files = [f.replace("\\", "/") for f in rule.target_files()]
        # analyze all .xml files
        for f in target_files:
            result.append(rule.analyzer().analyze(f, data_type_refiner))

        return result

    def _analyze(self, data_type_refiner: DataTypeRefiner=None):
        results = {}        # { PackageGenerationRule, result }
        for rule in self._rules:
            results[rule] = self._analyze_by_rule(rule, data_type_refiner)

        return results

    # collect module list
    def _collect_module_list(self, analyze_results):
        module_list = []
        for r in analyze_results:
            for sections in r:
                for s in sections:
                    if s.module() not in module_list:
                        module_list.append(s.module())

        return module_list

    # build package structure
    def _build_package_strucutre(self):
        analyze_results = self._analyze()

        # collect module list
        module_list = []
        for results in analyze_results.values():
            module_list.extend(self._collect_module_list(results))
        self._package_structure = build_module_structure(module_list)

        # at first analyze without DataTypeRefiner
        generation_info: Dict['PackageGenerationRule', 'GenerationInfoByRule'] = {}
        for rule in self._rules:
            analyze_results = self._analyze_by_rule(rule)
            module_structure = build_module_structure(
                self._collect_module_list(analyze_results))
            generation_info[rule] = build_generation_info(
                analyze_results, module_structure)

        # build entry points
        for rule in generation_info.keys():
            for target in generation_info[rule].targets():
                info = generation_info[rule].get_target(target)
                for data in info.data:
                    if data.type() not in ["class", "constant", "function"]:
                        continue
                    self._entry_points.append({
                        "mod_name": info.name,
                        "type": data.type(),
                        "name": data.name(),
                        "full_name": "{}.{}".format(info.name, data.name())
                    })

    # create module directories/files
    def _create_empty_modules(self):
        make_module_dirs(self._config.output_dir, self._package_structure)

    # map between result of analyze and module structure
    def _build_generation_info(self):
        self._generation_info = {}
        for rule in self._rules:
            data_type_refiner = DataTypeRefiner(
                self._package_structure, self._entry_points)
            analyze_results = self._analyze_by_rule(rule, data_type_refiner)
            module_structure = build_module_structure(
                self._collect_module_list(analyze_results))
            self._generation_info[rule] = build_generation_info(
                analyze_results, module_structure)

    def _build_dependency(self):
        refiner = DataTypeRefiner(self._package_structure, self._entry_points)
        builder = DependencyBuilder(refiner, self._generation_info)
        builder.build()

    def _generate_by_rule(self, rule):
        for target in self._generation_info[rule].targets():
            info = self._generation_info[rule].get_target(target)
            refiner = DataTypeRefiner(self._package_structure, self._generation_info)
            rule.generator().set_data_type_refiner(refiner)
            # dump if necessary
            if self._config.dump:
                rule.generator().dump_json(self._config.output_dir + "/" + target + "-dump.json", info)
            # generate python code
            rule.generator().generate(self._config.output_dir + "/" + target, info, self._config.style_format)

    def _generate(self):
        for rule in self._generation_info.keys():
            self._generate_by_rule(rule)

    def add_rule(self, rule):
        self._rules.append(rule)

    def generate(self):
        self._build_package_strucutre()
        self._create_empty_modules()
        self._build_generation_info()
        self._build_dependency()

        # with open("temp.log", "w") as f:
        #     for rule in self._rules:
        #         for key, info in self._generation_info[rule].items():
        #             f.write("### " + key)
        #             f.write(repr(info["deps"]))
        self._generate()
