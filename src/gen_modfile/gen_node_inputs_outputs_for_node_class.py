##############################################################################
#
# gen_node_inputs_outputs_for_node_class.py
#
# Description:
#   gen_node_inputs_outputs_for_node_class.py generates
#   definition to add inputs and outputs argument and their class
#   as a modfile format.
#
# Note:
#   This script needs to run from blender.
#   So, you need to download blender binary from blender's official website.
#
# Usage:
#   blender -noaudio --factory-startup --background --python \
#     gen_node_inputs_outputs_for_node_class.py --
#     -o <output_dir> -f <output_format>
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

# ruff: noqa: UP006, UP032, UP035, PTH103
# ruff: noqa: PTH123

import argparse
import json
import os
import sys
from typing import Dict, TextIO

import bpy  # pylint: disable=E0401


class GenerationConfig:
    first_import_module_name = None
    output_dir = None
    output_alias = False
    output_format = "rst"


# pylint: disable=C0209
def analyze() -> Dict:
    results = {
        "new": [],
        "append": [],
    }

    for node_base_class in bpy.types.NodeInternal.__subclasses__():
        node_baseclass_name = node_base_class.__name__
        nodetree_class_name = "{}Tree".format(node_baseclass_name)

        try:
            node_group = bpy.data.node_groups.new(
                nodetree_class_name, nodetree_class_name)
        except TypeError:
            continue

        for node_class_name in dir(bpy.types):
            if not node_class_name.startswith(node_baseclass_name):
                continue

            try:
                node = node_group.nodes.new(node_class_name)
            except RuntimeError:
                continue

            append_class_def = {
                "name": node_class_name,
                "base_classes": [],
                "description": None,
                "type": "class",
                "module": "bpy.types",
                "methods": [],
                "attributes": [],
            }

            if node.inputs:
                # Add fake class for node inputs.
                fake_class_name = "_{}_NodeInputs".format(node_class_name)
                new_class_def = {
                    "name": fake_class_name,
                    "base_classes": ["bpy.types.NodeInputs"],
                    "description": None,
                    "type": "class",
                    "module": "bpy.types",
                    "methods": [],
                    "attributes": [],
                }

                for i, node_input in enumerate(node.inputs):
                    new_func_def = {
                        "name": "__getitem__",
                        "description": None,
                        "type": "method",
                        "parameters": ["key"],
                        "parameter_details": [],
                        "return": {},
                        "options": ["overload"],
                    }
                    new_func_def["parameter_details"].append({
                        "name": "key",
                        "description": None,
                        "data_type": (
                            'typing.Literal[{}] | typing.Literal["{}"]'
                            .format(i, node_input.name)
                        ),
                        "mod_option": "skip-refine",
                    })
                    new_func_def["return"] = {
                        "type": "return",
                        "description": None,
                        "data_type": (
                            ":class:`bpy.types.{}`"
                            .format(node_input.__class__.__name__)
                        ),
                    }
                    new_class_def["methods"].append(new_func_def)

                results["new"].append(new_class_def)

                # Add attribute for input.
                new_attribute = {
                    "type": "attribute",
                    "name": "inputs",
                    "description": None,
                    "class": node_class_name,
                    "module": "bpy.types",
                    "data_type": (
                        ":class:`bpy.types.{}`"
                        .format(fake_class_name)
                    ),
                    "mod_option": "skip-refine",
                }
                append_class_def["attributes"].append(new_attribute)
                results["append"].append(append_class_def)

            if node.outputs:
                # Add fake class for node outputs.
                fake_class_name = "_{}_NodeOutputs".format(node_class_name)
                new_class_def = {
                    "name": fake_class_name,
                    "base_classes": ["bpy.types.NodeOutputs"],
                    "description": None,
                    "type": "class",
                    "module": "bpy.types",
                    "methods": [],
                    "attributes": [],
                }

                for i, node_output in enumerate(node.outputs):
                    new_func_def = {
                        "name": "__getitem__",
                        "description": None,
                        "type": "method",
                        "parameters": ["key"],
                        "parameter_details": [],
                        "return": {},
                        "options": ["overload"],
                    }
                    new_func_def["parameter_details"].append({
                        "name": "key",
                        "description": None,
                        "data_type": (
                            'typing.Literal[{}] | typing.Literal["{}"]'
                            .format(i, node_output.name)
                        ),
                        "mod_option": "skip-refine",
                    })
                    new_func_def["return"] = {
                        "type": "return",
                        "description": None,
                        "data_type": (
                            ":class:`bpy.types.{}`"
                            .format(node_output.__class__.__name__)
                        ),
                    }
                    new_class_def["methods"].append(new_func_def)

                results["new"].append(new_class_def)

                # Add attribute for output.
                new_attribute_def = {
                    "type": "attribute",
                    "name": "outputs",
                    "description": None,
                    "class": node_class_name,
                    "module": "bpy.types",
                    "data_type": (
                        ":class:`bpy.types.{}`"
                        .format(fake_class_name)
                    ),
                }
                append_class_def["attributes"].append(new_attribute_def)
                results["append"].append(append_class_def)

    return results


# pylint: disable=C0209
def write_class_info(f: TextIO, mod_kind: str, class_info: Dict) -> None:
    f.write(".. mod-type:: {}\n\n".format(mod_kind))
    f.write(".. module:: {}\n\n".format(class_info["module"]))
    if len(class_info["base_classes"]) != 0:
        f.write("base classes --- {}\n\n".format(
            ', '.join(class_info["base_classes"])))
    f.write(".. class:: {}\n\n".format(class_info["name"]))
    for attr_info in class_info["attributes"]:
        f.write("   .. attribute:: {}\n\n".format(attr_info["name"]))
        f.write("      :type: {}\n\n".format(attr_info["data_type"]))
    for func_info in class_info["methods"]:
        f.write("   .. {}:: {}({})\n\n".format(
            func_info["type"], func_info["name"],
            ", ".join(func_info["parameters"])))
        if "overload" in func_info["options"]:
            f.write("      :option function: overload\n")
        for param_info in func_info["parameter_details"]:
            f.write("      :type {}: {}\n"
                    .format(param_info["name"], param_info["data_type"]))
            f.write("      :mod-option arg {}: {}\n"
                    .format(param_info["name"], param_info["mod_option"]))
        ret_info = func_info["return"]
        f.write("      :rtype: {}\n\n".format(ret_info["data_type"]))
        f.write("\n")


# pylint: disable=C0209
def write_to_rst_modfile(data: Dict, config: 'GenerationConfig') -> None:
    os.makedirs(config.output_dir, exist_ok=True)

    for info in data["new"]:
        assert info["type"] == "class"

        output_dir = "{}/new".format(config.output_dir)
        os.makedirs(output_dir, exist_ok=True)

        mod_filename = "{}/{}.{}.mod.rst".format(
            output_dir, info["module"], info["name"])
        with open(mod_filename, "w", encoding="utf-8") as f:
            write_class_info(f, "new", info)
    for info in data["append"]:
        assert info["type"] == "class"

        output_dir = "{}/append".format(config.output_dir)
        os.makedirs(output_dir, exist_ok=True)

        mod_filename = "{}/{}.{}.mod.rst".format(
            output_dir, info["module"], info["name"])
        with open(mod_filename, "w", encoding="utf-8") as f:
            write_class_info(f, "append", info)


# pylint: disable=C0209
def write_to_json_modfile(data: Dict, config: 'GenerationConfig') -> None:
    os.makedirs(config.output_dir, exist_ok=True)

    for info in data["new"]:
        output_dir = "{}/new".format(config.output_dir)
        os.makedirs(output_dir, exist_ok=True)
        mod_filename = "{}/{}.{}.mod.json".format(
            output_dir, info["module"], info["name"])
        with open(mod_filename, "w", encoding="utf-8") as f:
            json.dump(info, f, indent=4, sort_keys=True, separators=(",", ": "))

    for info in data["append"]:
        output_dir = "{}/append".format(config.output_dir)
        os.makedirs(output_dir, exist_ok=True)
        mod_filename = "{}/{}.{}.mod.json".format(
            output_dir, info["module"], info["name"])
        with open(mod_filename, "w", encoding="utf-8") as f:
            json.dump(info, f, indent=4, sort_keys=True, separators=(",", ": "))


def write_to_modfile(data: Dict, config: 'GenerationConfig') -> None:
    if config.output_format == "rst":
        write_to_rst_modfile(data, config)
    elif config.output_format == "json":
        write_to_json_modfile(data, config)


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
        "--python {} -- [-f <output_format>] "
        "[-o <output_dir>]".format(__file__)
    )
    parser = argparse.ArgumentParser(usage)
    parser.add_argument(
        "-o", dest="output_dir", type=str, help="Output directory.",
        required=True
    )
    parser.add_argument("-f", dest="output_format", type=str,
                        help="Output format (rst, json).", required=True)
    args = parser.parse_args(argv)

    config = GenerationConfig()
    config.output_dir = args.output_dir
    config.output_format = args.output_format

    if config.output_format not in ["rst", "json"]:
        raise ValueError(
            "Unsupported output format: {}".format(config.output_format))

    return config


def main() -> None:
    config = parse_options()

    # Analyze modules.
    results = analyze()

    # Write module info to file.
    write_to_modfile(results, config)


if __name__ == "__main__":
    main()
