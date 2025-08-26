##############################################################################
#
# gen_external_modules_modfile.py
#
# Description:
#   gen_external_modules_modfile.py generates python classes and functions
#   definition from python modules in blender's 'modules' directory.
#   The definitions are output as a modfile format.
#
# Note:
#   This script needs to run from blender.
#   So, you need to download blender binary from blender's official website.
#
# Usage:
#   blender -noaudio --factory-startup --background --python \
#     gen_external_modules_modfile.py -- -m <first_import_module_name>
#     -o <output_dir> -f <output_format>
#
#     first_import_module_name:
#       Module name to import first.
#       This is used for finding blender's 'modules' directory.
#       [Ex] addon_utils
#
#     output_dir:
#       Generated definitions are output to files which will be located to
#       specified directory.
#       [Ex] gen_modules_modfile.generated
#
#     output_format:
#       Output format. Supported formats are "rst" and "json".
#
##############################################################################

# ruff: noqa: UP006, UP032, UP035, PTH103, PTH113, PTH118, PTH120,
# ruff: noqa: PTH123, SIM115

import argparse
import importlib
import inspect
import json
import os
import re
import sys
from typing import Dict, List, TextIO

import bpy  # pylint: disable=E0401

EXCLUDE_MODULE_LIST = {
    "bl_i18n_utils.settings_user",
    "bl_i18n_utils.utils_spell_check",
    "bl_app_templates_system.2D_Animation",
    "bl_app_templates_system.Sculpting",
    "bl_app_templates_system.VFX",
    "bl_app_templates_system.Video_Editing",
    "bgui.bgui_utils",
    "_bpy_internal.http.downloader",
}

IGNORE_DOC_REGEX_LIST = {
    re.compile(r"^animsys_refactor.update_data_paths$"),
    re.compile(r"^bl_i18n_utils.utils.I18n.parse_from_po$"),
    re.compile(r"^bl_i18n_utils.utils.I18nMessages.find_best_messages_matches$"),
    re.compile(r"^bl_i18n_utils.utils.I18nMessages.merge$"),
    re.compile(r"^bl_i18n_utils.utils.I18nMessages.parse_messages_from_po$"),
    re.compile(r"^bpy_extras.wm_utils.progress_report.ProgressReport$"),
    re.compile(r"^bpy_types.RNAMeta$"),
    re.compile(r"^bpy_types.RNAMetaPropGroup$"),
    re.compile(r"^bpy_types.OrderedDictMini.*"),
    re.compile(r"^bl_operators.presets.AddPresetBase$"),
    re.compile(r"^bl_ui.UI_UL_list*"),
    re.compile(r"^bl_ui.space_toolsystem_common.*"),
    re.compile(r"^bl_ui.space_toolsystem_toolbar.*"),
    re.compile(r"^progress_report.ProgressReport$"),
    re.compile(r"^_bpy_internal.grease_pencil.stroke.BezierHandle$"),
    re.compile(r"^_bpy_types._RNAMeta$"),
    re.compile(r"^_bpy_types._RNAMetaPropGroup$"),
}

CLASS_DEFAULT_VALUE_REGEX = re.compile(r"<(.+)[^<]*>")


def separator() -> str:
    if os.name == "nt":
        return "\\"
    return "/"


class GenerationConfig:
    first_import_module_name = None
    output_dir = None
    output_alias = False
    output_format = "rst"


def get_module_name_list(config: 'GenerationConfig') -> List[str]:
    first_module = importlib.import_module(config.first_import_module_name)

    # Get modules to import.
    modules_dir = os.path.dirname(first_module.__file__)
    module_name_list = []
    for cur_dir, _, files in os.walk(modules_dir):
        for f in files:
            if not f.endswith(".py"):
                continue
            module_name = os.path.join(cur_dir, f).replace(
                modules_dir + separator(), "")
            module_name = module_name[:-3].replace(separator(), ".")
            module_name = module_name.replace(".__init__", "")
            module_name_list.append(module_name)

    return list(set(module_name_list) - EXCLUDE_MODULE_LIST)


def import_modules(module_name_list: List[str]) -> List:
    imported_modules = []
    for name in module_name_list:
        mod = {}
        mod["module"] = importlib.import_module(name)
        mod["module_name"] = name
        imported_modules.append(mod)

    return imported_modules


def get_method_type(class_: object, function: object) -> str:
    if not hasattr(function, "__name__"):
        return "method"

    func = class_.__dict__.get(function.__name__)
    if isinstance(func, staticmethod):
        return "staticmethod"
    if isinstance(func, classmethod):
        return "classmethod"
    return "method"


# pylint: disable=C0209
def analyze_function(module_name: str, function: tuple,
                     is_method: bool = False, class_: object = None) -> Dict:
    function_def = {
        "name": function[0],
        "description": None,
        "type": "method" if is_method else "function",
        "return": {
            "type": "return",
        }
    }

    if is_method:
        function_def["type"] = get_method_type(class_, function[1])
    else:
        function_def["module"] = module_name

        function_full_name = "{}.{}".format(module_name, function_def["name"])
        for regex in IGNORE_DOC_REGEX_LIST:
            if regex.match(function_full_name):
                break
        else:
            function_def["description"] = inspect.getdoc(function[1])

    if not inspect.isbuiltin(function[1]):
        try:
            function_def["parameters"] = []
            params = inspect.signature(function[1]).parameters
            start_kwonlyarg = False
            for k, v in params.items():
                param_type = str(v.kind)

                if not start_kwonlyarg and param_type == 'KEYWORD_ONLY':
                    function_def["parameters"].append("*")
                    start_kwonlyarg = True

                arg_str = ""
                if v.default == inspect.Parameter.empty:
                    arg_str = k
                else:
                    arg_str = CLASS_DEFAULT_VALUE_REGEX.sub("None", str(v))
                if param_type == 'VAR_POSITIONAL':
                    arg_str = "*{}".format(arg_str)
                elif param_type == 'VAR_KEYWORD':
                    arg_str = "**{}".format(arg_str)

                function_def["parameters"].append(arg_str)

        except ValueError:
            function_def["parameters"] = []
    else:
        function_def["parameters"] = []

    if len(function_def["parameters"]) >= 1:
        if function_def["parameters"][0] == "self":
            if function_def["type"] == "method":
                function_def["parameters"].remove("self")
            else:
                function_def["parameters"][0] = "self_"

    return function_def


def is_inherited_method(class_: type, method_name: str) -> bool:
    method = getattr(class_, method_name)
    if not hasattr(method, "__qualname__"):
        return False

    class_name = class_.__name__
    qual_name = method.__qualname__

    return not qual_name.startswith("{}.".format(class_name))


# pylint: disable=C0209
def analyze_class(module_name: str, class_: tuple) -> Dict:
    class_def = {
        "name": class_[0],
        "description": None,
        "type": "class",
        "module": module_name,
        "methods": [],
        "attributes": [],
    }

    class_full_name = "{}.{}".format(module_name, class_def["name"])
    for regex in IGNORE_DOC_REGEX_LIST:
        if regex.match(class_full_name):
            break
    else:
        class_def["description"] = inspect.getdoc(class_[1])

    # Get base classes
    class_def["base_classes"] = []
    base_class_fullnames = {"{}{}".format(c.__module__, c.__name__)
                            for c in class_[1].__bases__}
    for c in inspect.getmro(class_[1]):
        if c.__name__ == class_[1].__name__:
            continue

        # Skip parent classes which are not directly inherited.
        fullname = "{}{}".format(c.__module__, c.__name__)
        if fullname not in base_class_fullnames:
            continue

        if c.__module__ == "bpy_types" and c.__name__ != "_GenericUI":
            class_def["base_classes"].append("bpy.types.{}".format(c.__name__))
        elif c.__module__ == "builtins":
            if c.__name__ in ("dict"):
                class_def["base_classes"].append(c.__name__)
            else:
                continue
        else:
            class_def["base_classes"].append(
                "{}.{}".format(c.__module__, c.__name__))
        # This avoids "E0240: Inconsistent method resolution order" error on
        # pylint_cycles.sh
        class_def["base_classes"].reverse()

    for x in inspect.getmembers(class_[1]):
        if x[0].startswith("_"):
            continue        # Skip private methods and attributes.

        # Get all class method definitions.
        if callable(x[1]):
            if is_inherited_method(class_[1], x[0]):
                continue        # Skip inherited methods.

            func_def = analyze_function(module_name, x, True, class_[1])

            function_full_name = "{}.{}.{}".format(
                module_name, class_def["name"], func_def["name"])
            for regex in IGNORE_DOC_REGEX_LIST:
                if regex.match(function_full_name):
                    break
            else:
                func_def["description"] = inspect.getdoc(x[1])

            class_def["methods"].append(func_def)
        # Get all class parameter definitions.
        else:
            attribute_def = {
                "type": "attribute",
                "name": x[0],
                "description": None,
                "class": class_[0],
                "module": module_name,
            }
            class_def["attributes"].append(attribute_def)

    return class_def


def analyze_module(module_name: str, module: object) -> Dict:
    result = {
        "classes": [],
        "functions": [],
        "constants": [],
    }

    # Get all class definitions.
    classes = inspect.getmembers(module, inspect.isclass)
    for c in classes:
        if inspect.isbuiltin(c[1]):
            continue
        if inspect.getmodule(c[1]) != module:
            continue    # Remove indirect classes. (ex. from XXX import ZZZ)
        class_def = analyze_class(module_name, c)

        # Only class _GenericUI is allowd in bpy_types module.
        if module_name == "bpy_types":
            if class_def["name"] != "_GenericUI":
                continue

        result["classes"].append(class_def)

    # Get all function definitions.
    functions = inspect.getmembers(module, inspect.isfunction)
    for f in functions:
        if f[0].startswith("_"):
            continue    # Skip private functions.
        if inspect.getmodule(f[1]) != module:
            continue    # Remove indirect functions. (ex. from XXX import ZZZ)

        result["functions"].append(analyze_function(module_name, f))

    return result


def analyze(modules: List) -> Dict:
    results = {}
    for m in modules:
        results[m["module_name"]] = analyze_module(
            m["module_name"], m["module"])

    return results


def write_description(f: TextIO, description: str, indent: str) -> None:
    lines = description.split("\n")
    for line in lines:
        f.write("{}{}\n".format(indent, line))
    f.write("\n")


# pylint: disable=C0209
def write_to_rst_modfile(data: Dict, config: 'GenerationConfig') -> None:
    os.makedirs(config.output_dir, exist_ok=True)
    for module, d in data.items():
        for info in d["new"]:
            if info["type"] == "class":
                class_info = info
                mod_filename = "{}/{}.{}.mod.rst".format(
                    config.output_dir, module, class_info["name"])
                with open(mod_filename, "w", encoding="utf-8") as f:
                    f.write(".. mod-type:: new\n\n")
                    f.write(".. module:: {}\n\n".format(module))
                    if len(class_info["base_classes"]) != 0:
                        f.write("base classes --- {}\n\n".format(
                            ', '.join(class_info["base_classes"])))
                    f.write(".. class:: {}\n\n".format(class_info["name"]))
                    if class_info["description"] is not None:
                        write_description(f, class_info["description"], "   ")
                    for attr_info in class_info["attributes"]:
                        f.write("   .. attribute:: {}\n\n".format(
                            attr_info["name"]))
                        if attr_info["description"] is not None:
                            write_description(f, attr_info["description"],
                                              "      ")
                    for func_info in class_info["methods"]:
                        f.write("   .. {}:: {}({})\n\n".format(
                            func_info["type"],
                            func_info["name"],
                            ", ".join(func_info["parameters"])))
                        if func_info["description"] is not None:
                            write_description(f, func_info["description"],
                                              "      ")
                        if len(func_info["parameters"]) >= 1:
                            for param in func_info["parameters"]:
                                sp = param.split("=")
                                if sp[0].startswith("*"):
                                    continue
                                if len(sp) >= 2 and sp[1] == "None":
                                    continue
                                f.write("      :option arg {}".format(sp[0]))
                                f.write(": never none\n")
                        f.write("\n")
            elif info["type"] == "function":
                func_info = info
                mod_filename = "{}/{}.mod.rst".format(config.output_dir, module)
                if os.path.isfile(mod_filename):
                    f = open(mod_filename, "a", encoding="utf-8")
                else:
                    f = open(mod_filename, "w", encoding="utf-8")
                    f.write(".. mod-type:: new\n\n")
                    f.write(".. module:: {}\n\n".format(module))
                f.write(".. function:: {}({})\n\n".format(
                    func_info["name"], ", ".join(func_info["parameters"])))
                if func_info["description"] is not None:
                    write_description(f, func_info["description"], "   ")
                if len(func_info["parameters"]) >= 1:
                    for param in func_info["parameters"]:
                        sp = param.split("=")
                        if sp[0].startswith("*"):
                            continue
                        if len(sp) >= 2 and sp[1] == "None":
                            continue
                        f.write("   :option arg {}: ".format(sp[0]))
                        f.write("never none\n")
                f.write("\n")
                f.close()
            elif info["type"] == "constant":
                constant_info = info
                mod_filename = "{}/{}.mod.rst".format(
                    config.output_dir, module)
                if os.path.isfile(mod_filename):
                    f = open(mod_filename, "a", encoding="utf-8")
                else:
                    # pylint: disable=R1732
                    f = open(mod_filename, "w", encoding="utf-8")
                    f.write(".. mod-type:: new\n\n")
                    f.write(".. module:: {}\n\n".format(module))
                f.write(".. data:: {}\n\n".format(constant_info["name"]))
                if constant_info["description"] is not None:
                    write_description(f, constant_info["description"], "   ")
                if "data_type" in constant_info:
                    f.write("   :type: {}\n\n".format(
                        constant_info["data_type"]))
                f.close()


# pylint: disable=C0209
def write_to_json_modfile(data: Dict, config: 'GenerationConfig') -> None:
    os.makedirs(config.output_dir, exist_ok=True)
    for module, d in data.items():
        mod_filename = "{}/{}.json".format(config.output_dir, module)
        with open(mod_filename, "w", encoding="utf-8") as f:
            json.dump(d, f, indent=4, sort_keys=True, separators=(",", ": "))


def write_to_modfile(info: Dict, config: 'GenerationConfig') -> None:
    data = {}

    for module_name, module_info in info.items():
        if module_name not in data:
            data[module_name] = {
                "new": []
            }
        for class_info in module_info["classes"]:
            data[module_name]["new"].append(class_info)
        for function_info in module_info["functions"]:
            data[module_name]["new"].append(function_info)
        for constant_info in module_info["constants"]:
            data[module_name]["new"].append(constant_info)

    if config.output_format == "rst":
        write_to_rst_modfile(data, config)
    elif config.output_format == "json":
        write_to_json_modfile(data, config)


# pylint: disable=C0209
def get_alias_to_bpy_types(results: dict) -> dict:
    bpy_types = dir(bpy.types)

    alias = {
        "classes": [],
        "functions": [],
        "constants": [],
    }

    for mod_name in results:
        for c in results[mod_name]["classes"]:
            if c["name"] in bpy_types:
                constant_def = {
                    "type": "constant",
                    "description": None,
                    "name": c["name"],
                    "module": "bpy.types",
                    "data_type": ":class:`{}.{}`".format(
                        c["module"], c["name"]),
                }
                alias["constants"].append(constant_def)

    return alias


# pylint: disable=C0209
def parse_options() -> 'GenerationConfig':
    # Start after "--" option if we run this script from blender binary.
    argv = sys.argv
    try:
        index = argv.index("--") + 1
    except:     # noqa: E722 # pylint: disable=W0702
        index = len(argv)
    argv = argv[index:]

    usage = (
        "Usage: blender -noaudio --factory-startup --background "
        "--python {} -- [-m <first_import_module_name>] [-a] "
        "[-o <output_dir>]".format(__file__)
    )
    parser = argparse.ArgumentParser(usage)
    parser.add_argument(
        "-m", dest="first_import_module_name", type=str,
        help="""Module name to import first.
        This is used for finding blender's 'modules' directory.
        """,
        required=True
    )
    parser.add_argument(
        "-o", dest="output_dir", type=str, help="Output directory.",
        required=True
    )
    parser.add_argument("-a", dest="output_alias", action="store_true")
    parser.add_argument("-f", dest="output_format", type=str,
                        help="Output format (rst, json).", required=True)
    args = parser.parse_args(argv)

    config = GenerationConfig()
    config.first_import_module_name = args.first_import_module_name
    config.output_dir = args.output_dir
    config.output_alias = args.output_alias
    config.output_format = args.output_format

    if config.output_format not in ["rst", "json"]:
        raise ValueError(
            "Unsupported output format: {}".format(config.output_format))

    return config


def main() -> None:
    config = parse_options()

    # Get modules to import.
    module_name_list = get_module_name_list(config)

    # Import modules.
    imported_modules = import_modules(module_name_list)

    # Analyze modules.
    results = analyze(imported_modules)

    # Get alias to bpy.types
    if config.output_alias:
        alias = get_alias_to_bpy_types(results)
        results["bpy.types"] = alias

    # Write module info to file.
    write_to_modfile(results, config)


if __name__ == "__main__":
    main()
