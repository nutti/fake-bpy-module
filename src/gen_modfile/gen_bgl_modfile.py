##############################################################################
#
# gen_bgl_modfile.py
#
# Description:
#   gen_bgl_modfile.py generates python constant and function definitions
#   which are defined by bgl.c.
#   The definitions are output as a modfile format (JSON).
#
# Note:
#   You need to download blender source code for passing 'bgl.c' file to
#   this script.
#
# Usage:
#   python gen_bgl_modfile.py -i <bgl_c_file> -o <output_file>
#
#     bgl_c_file:
#       Path to bgl.c.
#
#     output_file:
#       Generated definitions are output to specified file.
#
##############################################################################

import argparse
import re
from typing import List, Dict
import json


class GenerationConfig:
    bgl_c_file = None
    output_file = None


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
        "-i", dest="bgl_c_file", type=str, help="Path to bgl.c",
        required=True
    )
    parser.add_argument(
        "-o", dest="output_file", type=str, help="Output directory",
        required=True
    )
    args = parser.parse_args()

    config = GenerationConfig()
    config.bgl_c_file = args.bgl_c_file
    config.output_file = args.output_file

    return config


def write_to_modfile(info: Dict, config: 'GenerationConfig'):
    with open(config.output_file, "w", encoding="utf-8") as f:
        json.dump(info, f, indent=4, sort_keys=True, separators=(",", ": "))


def main():
    config = parse_options()

    # Analyze bgl.c.
    results = analyze(config)

    # Write definitions to file.
    write_to_modfile(results, config)


if __name__ == "__main__":
    main()
