import argparse
import ast
import json
from typing import List


INDENT = " " * 2


# use below command on release/scripts to check target files
#   egrep -rn "register_class\(" . | awk '{print $1}' | sed -E 's/:[0-9]+:.*/",/g' | sed -E 's/^\.\//"/g' | uniq
target_py_scripts = [
    "startup/keyingsets_builtins.py",
    "startup/bl_operators/__init__.py",
    "startup/bl_ui/properties_data_empty.py",
    "startup/bl_ui/properties_physics_field.py",
    "startup/bl_ui/properties_texture.py",
    "startup/bl_ui/properties_material_gpencil.py",
    "startup/bl_ui/space_sequencer.py",
    "startup/bl_ui/space_topbar.py",
    "startup/bl_ui/properties_particle.py",
    "startup/bl_ui/properties_physics_rigidbody.py",
    "startup/bl_ui/properties_freestyle.py",
    "startup/bl_ui/space_node.py",
    "startup/bl_ui/properties_object.py",
    "startup/bl_ui/properties_render.py",
    "startup/bl_ui/space_statusbar.py",
    "startup/bl_ui/space_clip.py",
    "startup/bl_ui/space_info.py",
    "startup/bl_ui/properties_mask_common.py",
    "startup/bl_ui/space_graph.py",
    "startup/bl_ui/properties_animviz.py",
    "startup/bl_ui/space_text.py",
    "startup/bl_ui/properties_data_bone.py",
    "startup/bl_ui/space_console.py",
    "startup/bl_ui/properties_constraint.py",
    "startup/bl_ui/properties_physics_softbody.py",
    "startup/bl_ui/properties_data_light.py",
    "startup/bl_ui/properties_workspace.py",
    "startup/bl_ui/__init__.py",
    "startup/bl_ui/properties_data_shaderfx.py",
    "startup/bl_ui/properties_view_layer.py",
    "startup/bl_ui/properties_data_armature.py",
    "startup/bl_ui/properties_scene.py",
    "startup/bl_ui/properties_data_lightprobe.py",
    "startup/bl_ui/space_dopesheet.py",
    "startup/bl_ui/properties_data_modifier.py",
    "startup/bl_ui/space_outliner.py",
    "startup/bl_ui/properties_data_speaker.py",
    "startup/bl_ui/space_view3d.py",
    "startup/bl_ui/properties_data_metaball.py",
    "startup/bl_ui/space_view3d_toolbar.py",
    "startup/bl_ui/properties_material.py",
    "startup/bl_ui/properties_physics_common.py",
    "startup/bl_ui/space_toolsystem_common.py",
    "startup/bl_ui/properties_paint_common.py",
    "startup/bl_ui/space_filebrowser.py",
    "startup/bl_ui/properties_data_gpencil.py",
    "startup/bl_ui/properties_physics_cloth.py",
    "startup/bl_ui/space_nla.py",
    "startup/bl_ui/properties_physics_rigidbody_constraint.py",
    "startup/bl_ui/properties_grease_pencil_common.py",
    "startup/bl_ui/space_toolsystem_toolbar.py",
    "startup/bl_ui/space_userpref.py",
    "startup/bl_ui/properties_data_mesh.py",
    "startup/bl_ui/properties_data_curve.py",
    "startup/bl_ui/properties_output.py",
    "startup/bl_ui/properties_physics_dynamicpaint.py",
    "startup/bl_ui/space_time.py",
    "startup/bl_ui/space_properties.py",
    "startup/bl_ui/properties_physics_fluid.py",
    "startup/bl_ui/properties_data_lattice.py",
    "startup/bl_ui/properties_physics_smoke.py",
    "startup/bl_ui/properties_world.py",
    "startup/bl_ui/properties_data_camera.py",
    "startup/bl_ui/space_image.py",
]


class GenerationConfig:
    input_py_scripts_dir = None
    output_file = None


def parse_options() -> 'GenerationConfig':
    usage = "Usage: python {} [-i <input_py_scripts_dir>] [-o <output_file>]"\
        .format(__file__)
    parser = argparse.ArgumentParser(usage)
    parser.add_argument(
        "-i", dest="input_py_scripts_dir", type=str, help="Path to python scripts directory"
    )
    parser.add_argument(
        "-o", dest="output_file", type=str, help="Output directory"
    )
    args = parser.parse_args()

    config = GenerationConfig()
    config.input_py_scripts_dir = args.input_py_scripts_dir
    config.output_file = args.output_file

    return config


def reverse_walk_find(node, cls):
    if isinstance(node, cls):
        return node
    if not hasattr(node, "parent"):
        return None
    return reverse_walk_find(node.parent, cls)


def create_class_mod_item_str(class_name: str, base_classes: List[str],
                              is_final: bool) -> str:
    str = ""
    str += INDENT * 2 + "{\n"
    str += INDENT * 3 + "\"name\": \"" + class_name + "\",\n"
    str += INDENT * 3 + "\"type\": \"class\",\n"
    str += INDENT * 3 + "\"module\": \"bpy.types\",\n"
    str += INDENT * 3 + "\"base_classes\": [" + ", ".join(base_classes) + "],\n"
    str += INDENT * 3 + "\"methods\": [],\n"
    str += INDENT * 3 + "\"attributes\": []\n"
    if is_final:
        str += INDENT * 2 + "}\n"
    else:
        str += INDENT * 2 + "},\n"

    return str


def is_primitive_class(class_: str) -> bool:
    primitive_classes = [
        "Panel",
        "UIList",
        "Menu",
        "Header",
    ]

    return class_ in primitive_classes


def generate_bgl_modfile(config: 'GenerationConfig'):
    root_nodes = {}
    for script in target_py_scripts:
        script_path = "{}/{}".format(config.input_py_scripts_dir, script)
        with open(script_path, "r") as f:
            source = f.read()

        root_nodes[script_path] = ast.parse(source, config.input_py_scripts_dir)

    # add parent attribute for reverse walk
    for root in root_nodes.values():
        for node in ast.walk(root):
            for child in ast.iter_child_nodes(node):
                child.parent = node

    # get all class definitions
    class_defs = []
    for root in root_nodes.values():
        for node in ast.walk(root):
            if isinstance(node, ast.ClassDef):
                class_defs.append(node)

    classes_to_be_registerd = []
    for script_path, root in root_nodes.items():
        # find if __name__ == '__main__'
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

        # find class to be registered by bpy.utils.register_class
        for node in ast.walk(main_node):
            if not isinstance(node, ast.Call):
                continue
            if node.func.id != "register_class":
                continue

            # parse 'for' statement based register_class
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

    # write queried classes to a file
    with open(config.output_file, "w") as f:
        f.write("{\n")
        f.write(INDENT + "\"new\": [\n")
        for i, class_ in enumerate(classes_to_be_registerd):
            is_final = (i == len(classes_to_be_registerd) - 1)
            base_classes = ["\"bpy.types.{}\"".format(c.id)
                            for c in class_.bases
                            if isinstance(c, ast.Name) and is_primitive_class(c.id)]
            f.write(create_class_mod_item_str(class_.name, base_classes, is_final))
        f.write(INDENT + "]\n")
        f.write("}")


def validate_bgl_modfile(config: 'GenerationConfig'):
    with open(config.output_file, "r") as f:
        json.load(f)


def main():
    config = parse_options()
    generate_bgl_modfile(config)
    validate_bgl_modfile(config)


if __name__ == "__main__":
    main()