################################################################################
#
# gen_module_modfile.py
#
# Description:
#   gen_module_modfile.py generates python classes and functions definition
#   from python modules in blender's 'modules' directory.
#   The definitions are output as a modfile format (JSON).
#
# Note:
#   This script needs to run from blender.
#   So, you need to download blender binary from blender's official website.
#
# Usage:
#   blender -noaudio --factory-startup --background --python \
#     gen_module_modfile.py -- -m <first_import_module_name> -o <output_dir>
#
#     first_import_module_name:
#       Module name to import first.
#       This is used for finding blender's 'modules' directory.
#       (ex. addon_utils)
#
#     output_dir:
#       Generated definitions are output to files which will be located to
#       specified directory.
#       (ex. gen_modules_modfile.generated)
#
################################################################################

import sys
import inspect
import os
import importlib
import json
import argparse
from typing import List, Dict
import bpy


EXCLUDE_MODULE_LIST = {
    "bl_i18n_utils.settings_user",
    "bl_i18n_utils.utils_spell_check",
    "bl_app_templates_system.2D_Animation",
    "bl_app_templates_system.Sculpting",
    "bl_app_templates_system.VFX",
    "bl_app_templates_system.Video_Editing",
}


def separator():
    if os.name == "nt":
        return "\\"
    return "/"


class GenerationConfig:
    first_import_module_name = None
    output_dir = None
    output_alias = False


def get_module_name_list(config: 'GenerationConfig') -> List[str]:
    first_module = importlib.import_module(config.first_import_module_name)

    # Get modules to import.
    modules_dir = os.path.dirname(first_module.__file__)
    module_name_list = []
    for cur_dir, _, files in os.walk(modules_dir):
        for f in files:
            if not f.endswith(".py"):
                continue
            module_name = os.path.join(cur_dir, f).replace(modules_dir + separator(), "")
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

def analyze_function(module_name: str, function, is_method=False) -> Dict:
    function_def = {
        "name": function[0],
        "type": "method" if is_method else "function",
        "return": {
            "type": "return",
        }
    }
    if not is_method:
        function_def["module"] = module_name

    if not inspect.isbuiltin(function[1]):
        try:
            function_def["parameters"] = list(inspect.signature(function[1]).parameters.keys())
        except ValueError:
            function_def["parameters"] = []
    
    return function_def


def analyze_class(module_name: str, class_) -> Dict:
    class_def = {
        "name": class_[0],
        "type": "class",
        "module": module_name,
        "methods": [],
        "attributes": [],
    }

    # Get base classes
    class_def["base_classes"] = []
    for c in inspect.getmro(class_[1]):
        if c.__name__ == class_[1].__name__:
            continue
        if c.__module__ == "builtins":
            continue
        class_def["base_classes"].append("{}.{}".format(c.__module__, c.__name__))

    for x in [x for x in inspect.getmembers(class_[1])]:
        if x[0].startswith("_"):
            continue        # Skip private methods and attributes.

        # Get all class method definitions.
        if callable(x[1]):
            class_def["methods"].append(analyze_function(module_name, x, True))
        # Get all class parameter definitions.
        else:
            attribute_def = {
                "type": "attribute",
                "name": x[0],
                "class": class_[0],
                "module": module_name,
            }
            class_def["attributes"].append(attribute_def)
    
    return class_def


def analyze_module(module_name: str, module) -> Dict:
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

        # To avoid circular dependency, we remove classes whose base class is defined in bpy.types module.
        has_bpy_types_base_class = False
        for bc in class_def["base_classes"]:
            if bc.find("bpy.types.") != -1:
                has_bpy_types_base_class = True
                break
        if has_bpy_types_base_class:
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
        results[m["module_name"]] = analyze_module(m["module_name"], m["module"])

    return results


def write_to_modfile(info: Dict, config: 'GenerationConfig'):
    data = {}

    for module_name, module_info in info.items():
        package_name = module_name
        index = package_name.find(".")
        if index != -1:
            package_name = package_name[:index]

        if package_name not in data.keys():
            data[package_name] = {
                "new": []
            }
        for class_info in module_info["classes"]:
            data[package_name]["new"].append(class_info)
        for function_info in module_info["functions"]:
            data[package_name]["new"].append(function_info)
        for constant_info in module_info["constants"]:
            data[package_name]["new"].append(constant_info)

    os.makedirs(config.output_dir, exist_ok=True)
    for pkg, d in data.items():
        with open("{}/{}.json".format(config.output_dir, pkg), "w") as f:
            json.dump(d, f, indent=4, sort_keys=True, separators=(",", ": "))


def get_alias_to_bpy_types(results):
    bpy_types = dir(bpy.types)

    alias = {
        "classes": [],
        "functions": [],
        "constants": [],
    }

    for mod_name in results.keys():
        for c in results[mod_name]["classes"]:
            if c["name"] in bpy_types:
                constant_def = {
                    "type": "constant",
                    "name": c["name"],
                    "module": "bpy.types",
                    "data_type": "{}.{}".format(c["module"], c["name"]),
                }
                alias["constants"].append(constant_def)

    return alias


def parse_options() -> 'GenerationConfig':
    # Start after "--" option if we run this script from blender binary.
    argv = sys.argv
    try:
        index = argv.index("--") + 1
    except:
        index = len(argv)
    argv = argv[index:]

    usage = """Usage: blender -noaudio --factory-startup --background --python
               {} -- [-m <first_import_module_name>] [-a] [-o <output_dir>]"""\
        .format(__file__)
    parser = argparse.ArgumentParser(usage)
    parser.add_argument(
        "-m", dest="first_import_module_name", type=str,
        help="""Module name to import first.
        This is used for finding blender's 'modules' directory.
        """,
        required=True
    )
    parser.add_argument(
        "-o", dest="output_dir", type=str, help="Output directory.", required=True
    )
    parser.add_argument("-a", dest="output_alias", action="store_true")
    args = parser.parse_args(argv)

    config = GenerationConfig()
    config.first_import_module_name = args.first_import_module_name
    config.output_dir = args.output_dir
    config.output_alias = args.output_alias

    return config


def main():
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
