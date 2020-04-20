################################################################################
#
# gen_startup_modfile.py
#
# Description:
#   gen_startup_modfile.py generates python classes definition which is
#   registered by scripts in 'startup' directory.
#   The definitions are output as a modfile format (JSON).
#
# Note:
#   This script does not need to be run from blender.
#   However, you need to download blender for passing 'startup' directory to
#   this script.
#
# Usage:
#   python gen_startup_modfile.py -i <startup_script_dir> -o <output_file>
#
#     startup_script_dir:
#       Path to blender's 'startup' directory.
#
#     output_file:
#       Generated definitions are output to specified file.
#
################################################################################

import argparse
import ast
import json
import os
from typing import List, Dict


def separator():
    if os.name == "nt":
        return "\\"
    return "/"


class GenerationConfig:
    startup_scripts_dir = None
    output_file = None


def parse_options() -> 'GenerationConfig':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", dest="startup_scripts_dir", type=str, help="Path to 'startup' directory.",
        required=True
    )
    parser.add_argument(
        "-o", dest="output_file", type=str, help="Output directory.", required=True
    )
    args = parser.parse_args()

    config = GenerationConfig()
    config.startup_scripts_dir = args.startup_scripts_dir
    config.output_file = args.output_file

    return config


def reverse_walk_find(node, cls):
    if isinstance(node, cls):
        return node
    if not hasattr(node, "parent"):
        return None
    return reverse_walk_find(node.parent, cls)


def is_primitive_class(class_: str) -> bool:
    primitive_classes = [
        "Panel",
        "UIList",
        "Menu",
        "Header",
    ]

    return class_ in primitive_classes


def get_scripts_list_to_parse(config: 'GenerationConfig') -> List[str]:
    scripts_to_parse = []
    for cur_dir, _, files in os.walk(config.startup_scripts_dir):
        for file_ in files:
            if not file_.endswith(".py"):
                continue

            filepath = os.path.join(cur_dir, file_).replace("/", separator())
            with open(filepath, "r") as f:
                lines = [l for l in f.readlines() if l.find("register_class(") != -1]
            if len(lines) > 0:
                scripts_to_parse.append(filepath)

    return scripts_to_parse            


def analyze(scripts_paths: List[str]) -> Dict:
    root_nodes = {}
    for script_path in scripts_paths:
        with open(script_path, "r") as f:
            source = f.read()

        root_nodes[script_path] = ast.parse(source, script_path)

    # Add parent attribute for reverse walk.
    for root in root_nodes.values():
        for node in ast.walk(root):
            for child in ast.iter_child_nodes(node):
                child.parent = node

    # Get all class definitions.
    class_defs = []
    for root in root_nodes.values():
        for node in ast.walk(root):
            if isinstance(node, ast.ClassDef):
                class_defs.append(node)

    classes_to_be_registerd = []
    for script_path, root in root_nodes.items():
        # Find if __name__ == '__main__'.
        for node in ast.walk(root):
            if not isinstance(node, ast.If):
                continue

            t = node.test
            if not isinstance(t, ast.Compare):
                continue
            if len(t.comparators) != 1:
                continue
            if not isinstance(t.comparators[0], ast.Str):
                continue
            if t.comparators[0].s != "__main__":
                continue
            if (t.left is not None) and (t.left.id == "__name__"):
                main_node = node
                break
        else:
            print("Could not find if __name__ == '__main__' (file: {})".format(script_path))
            continue

        # Find class to be registered by bpy.utils.register_class().
        for node in ast.walk(main_node):
            if not isinstance(node, ast.Call):
                continue
            if node.func.id != "register_class":
                continue

            # Parse 'for' statement based register_class.
            # example:
            #   classes = [...]
            #   for cls in classes:
            #       register_class(cls)
            for_node = reverse_walk_find(node, ast.For)
            if for_node:
                for assign in root.body:
                    if not isinstance(assign, ast.Assign):
                        continue
                    if len(assign.targets) != 1:
                        continue
                    if not isinstance(assign.targets[0], ast.Name):
                        continue
                    if not isinstance(for_node.iter, ast.Name):
                        continue
                    if for_node.iter.id != assign.targets[0].id:
                        continue
                    for c in assign.value.elts:
                        if not isinstance(c, ast.Name):
                            continue
                        classes_to_be_registerd.extend([cdef for cdef in class_defs if cdef.name == c.id])

    # Create data to write.
    data = { "new": [] }
    for class_ in classes_to_be_registerd:
        base_classes = ["bpy.types.{}".format(c.id)
                        for c in class_.bases
                        if isinstance(c, ast.Name) and is_primitive_class(c.id)]
        class_def = {
            "name": class_.name,
            "type": "class",
            "module": "bpy.types",
            "base_classes": base_classes,
        }
        data["new"].append(class_def)
    
    return data


def write_to_modfile(info: Dict, config: 'GenerationConfig'):
    with open(config.output_file, "w") as f:
        json.dump(info, f, indent=4, sort_keys=True, separators=(",", ": "))


def main():
    config = parse_options()

    # Find python scripts to parse.
    scripts_to_parse = get_scripts_list_to_parse(config)

    # Analyze scripts.
    results = analyze(scripts_to_parse)

    # Write registered classes to file.
    write_to_modfile(results, config)


if __name__ == "__main__":
    main()
