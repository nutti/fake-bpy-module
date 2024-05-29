##############################################################################
#
# gen_bgl_modfile.py
#
# Description:
#   gen_bgl_modfile.py generates python constant and function definitions
#   which are defined by bgl.cc.
#   The definitions are output as a modfile format.
#
# Note:
#   You need to download blender source code for passing 'bgl.cc' file to
#   this script.
#
# Usage:
#   python gen_bgl_modfile.py -i <bgl_c_file> -o <output_file>
#     -f <output_format>
#
#     bgl_c_file:
#       Path to bgl.cc.
#
#     output_file:
#       Generated definitions are output to specified file.
#
#     output_format:
#       Output format. Supported formats are "rst" and "json".
#
##############################################################################

import argparse
import re
from typing import List, Dict
import json


class GenerationConfig:
    bgl_c_file = None
    output_file = None
    output_format = "rst"


def get_function_name(line: str) -> str:
    regex = r"^\s*PY_MOD_ADD_METHOD\(([A-Za-z0-9]+)\);$"
    pattern = re.compile(regex)
    match = re.match(pattern, line)
    if match:
        return f"gl{match.group(1)}"

    return None


def get_const_name(line: str) -> str:
    regex = r"^\s*PY_DICT_ADD_INT\(([A-Za-z0-9_]+)\);$"
    pattern = re.compile(regex)
    match = re.match(pattern, line)
    if match:
        return match.group(1)

    regex = r"^\s*PY_DICT_ADD_INT64\(([A-Za-z0-9_]+)\);$"
    pattern = re.compile(regex)
    match = re.match(pattern, line)
    if match:
        return match.group(1)

    return None


def get_function_info(line: str) -> Dict:
    regex = r"^BGL_Wrap\(([A-Za-z0-9]+),([A-Za-z]+),(\([A-Za-z0-9,]+\))\);$"
    pattern = re.compile(regex)
    match = re.match(pattern, line)
    if match:
        func_name = match.group(1)
        return_type = match.group(2)
        args_list = match.group(3)
        return {
            "func_name": f"gl{func_name}",
            "return_type": return_type,
            "arg_types": args_list[1:-1].split(",")
        }

    return None


def create_constant_def(const_name: str) -> Dict:
    constant_def = {
        "name": const_name,
        "type": "constant",
        "module": "bgl",
        "data_type": "float",
    }
    return constant_def


def gltype_to_pytype(gltype: str) -> str:
    type_map = {
        "void": "",
        "GLvoidP": "",
        "GLubyte": "int",
        "GLubyteP": "int",
        "GLbyteP": "int",
        "GLcharP": "int",
        "GLushortP": "int",
        "GLshort": "int",
        "GLshortP": "int",
        "GLuint": "int",
        "GLuintP": "int",
        "GLint": "int",
        "GLintptr": "int",
        "GLintP": "int",
        "GLint64P": "int",
        "GLfloat": "float",
        "GLfloatP": "float",
        "GLdouble": "float",
        "GLdoubleP": "float",
        "GLboolean": "bool",
        "GLbooleanP": "bool",
        "GLsizei": "int",
        "GLsizeiP": "int",
        "GLsizeiptr": "int",
        "GLenum": "int",
        "GLenumP": "int",
        "GLbitfield": "int",
        "GLstring": "str",
    }
    return type_map[gltype]


def create_function_def(
        func_name: str, return_type: str, arg_types: List[str]) -> Dict:
    function_def = {
        "name": func_name,
        "type": "function",
        "module": "bgl",
        "return": {
            "type": "return",
            "data_type": gltype_to_pytype(return_type)
        },
        "parameters": [],
        "parameter_details": [],
    }
    for i, arg_type in enumerate(arg_types):
        function_def["parameters"].append(f"p{i}")
        function_def["parameter_details"].append({
            "name": f"p{i}",
            "type": "parameter",
            "data_type": gltype_to_pytype(arg_type)
        })

    return function_def


def analyze(config: 'GenerationConfig') -> Dict:
    func_info = {}
    with open(config.bgl_c_file, "r", encoding="utf-8") as f:
        data = f.read()
        regex = r"BGL_Wrap\([A-Za-z0-9]+,\s+[A-Za-z]+,\s+\([A-Za-z0-9, ]+\)\);"
        matched = re.findall(regex, data)
        for m in matched:
            pattern = re.compile(r"\s+")
            replaced = pattern.sub("", m)
            if replaced:
                info = get_function_info(replaced)
                func_info[info["func_name"]] = info

    # read and query function and constant list.
    func_lists = []
    const_lists = []
    with open(config.bgl_c_file, "r", encoding="utf-8") as f:
        line = f.readline()
        while line:
            func_name = get_function_name(line)
            if func_name in func_info:
                func_lists.append(func_name)
            const_name = get_const_name(line)
            if const_name:
                const_lists.append(const_name)
            line = f.readline()

    # Create data to write.
    data = {"new": []}
    for const in const_lists:
        data["new"].append(create_constant_def(const))
    for func in func_lists:
        data["new"].append(create_function_def(func_info[func]["func_name"],
                                               func_info[func]["return_type"],
                                               func_info[func]["arg_types"]))

    return data


def parse_options() -> 'GenerationConfig':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", dest="bgl_c_file", type=str, help="Path to bgl.cc",
        required=True
    )
    parser.add_argument(
        "-o", dest="output_file", type=str, help="Output directory",
        required=True
    )
    parser.add_argument("-f", dest="output_format", type=str,
                        help="Output format (rst, json).", required=True)
    args = parser.parse_args()

    config = GenerationConfig()
    config.bgl_c_file = args.bgl_c_file
    config.output_file = args.output_file
    config.output_format = args.output_format

    if config.output_format not in ["rst", "json"]:
        raise ValueError(f"Unsupported output format: {config.output_format}")

    return config


def write_to_rst_modfile(data: Dict, config: 'GenerationConfig'):
    with open(config.output_file, "w", encoding="utf-8") as f:
        f.write(".. mod-type:: new\n\n")
        f.write(".. module:: bgl\n\n")
        for info in data["new"]:
            if info["type"] == "function":
                func_info = info
                f.write(f".. function:: {func_info['name']}"
                        f"({', '.join(func_info['parameters'])})\n\n")
                for param_info in func_info["parameter_details"]:
                    f.write(f"   :type {param_info['name']}: {param_info['data_type']}\n")
                if func_info["return"]["data_type"] == "":
                    f.write("\n")
                else:
                    f.write(f"   :rtype: {func_info['return']['data_type']}\n\n")
            elif info["type"] == "constant":
                constant_info = info
                f.write(f".. data:: {constant_info['name']}\n\n")
                if "data_type" in constant_info:
                    f.write(f"   :type: {constant_info['data_type']}\n\n")


def write_to_json_modfile(data: Dict, config: 'GenerationConfig'):
    with open(config.output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, sort_keys=True, separators=(",", ": "))


def write_to_modfile(data: Dict, config: 'GenerationConfig'):
    if config.output_format == "rst":
        write_to_rst_modfile(data, config)
    elif config.output_format == "json":
        write_to_json_modfile(data, config)


def main():
    config = parse_options()

    # Analyze bgl.cc.
    results = analyze(config)

    # Write definitions to file.
    write_to_modfile(results, config)


if __name__ == "__main__":
    main()
