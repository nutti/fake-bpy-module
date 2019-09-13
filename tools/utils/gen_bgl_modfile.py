import argparse
import re
from typing import List, Dict
import json


INDENT = " " * 2


class GenerationConfig:
    input_bgl_c_file = None
    output_file = None


def get_function_name(line: str) -> str:
    regex = r"^\s*PY_MOD_ADD_METHOD\(([A-Za-z0-9]+)\);$"
    pattern = re.compile(regex)
    match = re.match(pattern, line)
    if match:
        return match.group(1)

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
            "func_name": func_name,
            "return_type": return_type,
            "arg_types": args_list[1:-1].split(",")
        }

    return None


def create_constant_mod_item_str(const_name: str, is_final: bool) -> str:
    str = ""
    str += INDENT * 2 + "{\n"
    str += INDENT * 3 + "\"name\": \"" + const_name + "\",\n"
    str += INDENT * 3 + "\"type\": \"constant\",\n"
    str += INDENT * 3 + "\"module\": \"bgl\",\n"
    str += INDENT * 3 + "\"data_type\": \"float\"\n"
    if is_final:
        str += INDENT * 2 + "}\n"
    else:
        str += INDENT * 2 + "},\n"

    return str


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


def create_function_mod_item_str(func_name: str, return_type: str,
                                 arg_types: List[str], is_final: bool) -> str:
    str = ""
    str += INDENT * 2 + "{\n"
    str += INDENT * 3 + "\"name\": \"" + func_name + "\",\n"
    str += INDENT * 3 + "\"type\": \"function\",\n"
    str += INDENT * 3 + "\"module\": \"bgl\",\n"

    str += INDENT * 3 + "\"return\": {\n"
    str += INDENT * 4 + "\"type\": \"return\",\n"
    str += INDENT * 4 + "\"data_type\": \"{}\"\n".format(gltype_to_pytype(return_type))
    str += INDENT * 3 + "},\n"

    str += INDENT * 3 + "\"parameters\": [\n"
    for i, arg_type in enumerate(arg_types):
        str += INDENT * 4 + "\"p{}\"".format(i)
        if i == len(arg_types) - 1:
            str += "\n"
        else:
            str += ",\n"
    str += INDENT * 3 + "],\n"

    str += INDENT * 3 + "\"parameter_details\": [\n"
    for i, arg_type in enumerate(arg_types):
        str += INDENT * 4 + "{\n"
        str += INDENT * 5 + "\"name\": \"p{}\",\n".format(i)
        str += INDENT * 5 + "\"type\": \"parameter\",\n"
        str += INDENT * 5 + "\"data_type\": \"{}\"\n".format(gltype_to_pytype(arg_type))
        str += INDENT * 4 + "}"
        if i == len(arg_types) - 1:
            str += "\n"
        else:
            str += ",\n"
    str += INDENT * 3 + "]\n"

    if is_final:
        str += INDENT * 2 + "}\n"
    else:
        str += INDENT * 2 + "},\n"

    return str


def generate_bgl_modfile(config: 'GenerationConfig'):
    func_info = {}
    with open(config.input_bgl_c_file, "r") as f:
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
    with open(config.input_bgl_c_file, "r") as f:
        l = f.readline()
        while l:
            func_name = get_function_name(l)
            if func_name in func_info.keys():
                func_lists.append(func_name)
            const_name = get_const_name(l)
            if const_name:
                const_lists.append(const_name)
            l = f.readline()

    # write queried functions and constants to a file
    with open(config.output_file, "w") as f:
        f.write("{\n")
        f.write(INDENT + "\"new\": [\n")
        for i, const in enumerate(const_lists):
            is_final = (len(func_lists) == 0) and (i == len(const_lists) - 1)
            f.write(create_constant_mod_item_str(const, is_final))
        for i, func in enumerate(func_lists):
            is_final = (i == len(func_lists) - 1)
            f.write(create_function_mod_item_str(func_info[func]["func_name"],
                                                 func_info[func]["return_type"],
                                                 func_info[func]["arg_types"],
                                                 is_final))
        f.write(INDENT + "]\n")
        f.write("}")


def parse_options() -> 'GenerationConfig':
    usage = "Usage: python {} [-i <input_bgl_c_file>] [-o <output_file>]"\
        .format(__file__)
    parser = argparse.ArgumentParser(usage)
    parser.add_argument(
        "-i", dest="input_bgl_c_file", type=str, help="Path to bgl.c"
    )
    parser.add_argument(
        "-o", dest="output_file", type=str, help="Output directory"
    )
    args = parser.parse_args()

    config = GenerationConfig()
    config.input_bgl_c_file = args.input_bgl_c_file
    config.output_file = args.output_file

    return config


def validate_bgl_modfile(config: 'GenerationConfig'):
    with open(config.output_file, "r") as f:
        json.load(f)


def main():
    config = parse_options()
    generate_bgl_modfile(config)
    validate_bgl_modfile(config)


if __name__ == "__main__":
    main()
