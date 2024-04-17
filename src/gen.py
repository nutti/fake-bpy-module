# coding: UTF-8

import glob
import argparse
from typing import List
import os
import re

import fake_bpy_module as fbm

INPUT_DIR: str = "."
MOD_FILES_DIR: str = os.path.dirname(os.path.abspath(__file__))


def create_generator(
        name: str, target_files: List[str], mod_files: List[str],
        config: 'fbm.PackageGeneratorConfig') -> 'fbm.PackageGenerationRule':
    generator: fbm.BaseWriter = None
    if config.output_format == ".py":
        generator = fbm.PyCodeWriter()
    elif config.output_format == "pyi":
        generator = fbm.PyInterfaceWriter()

    analyzer = fbm.BaseAnalyzer(mod_files)

    return fbm.PackageGenerationRule(name, target_files, analyzer, generator)


def make_bpy_rule(
        config: 'fbm.PackageGeneratorConfig') -> 'fbm.PackageGenerationRule':
    all_files = glob.glob(INPUT_DIR + "/bpy*.rst")
    excludes_files = glob.glob(INPUT_DIR + "/bpy_extras*.rst")
    files = list(set(all_files) - set(excludes_files))
    mod_files = [
        f"{MOD_FILES_DIR}/mods/common/analyzer/append/bpy.types.mod.rst"
        .replace("\\", "/"),
        f"{MOD_FILES_DIR}/mods/common/analyzer/new/bpy.types.mod.rst"
        .replace("\\", "/"),
    ]
    mod_files += glob.glob(
        f"{MOD_FILES_DIR}/mods/generated_mods/gen_startup_modfile/bpy.*.mod.rst"
        .replace("\\", "/"))
    mod_files += glob.glob(
        f"{MOD_FILES_DIR}/mods/generated_mods/gen_modules_modfile/bpy.*.mod.rst"
        .replace("\\", "/"))
    return create_generator("bpy", files, mod_files, config)


def make_bgl_rule(
        config: 'fbm.PackageGeneratorConfig') -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/bgl*.rst")
    mod_files = [
        f"{MOD_FILES_DIR}/mods/generated_mods/gen_bgl_modfile/bgl.mod.rst"
        .replace("\\", "/")
    ]
    return create_generator("bgl", files, mod_files, config)


def make_blf_rule(
        config: 'fbm.PackageGeneratorConfig') -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/blf*.rst")
    return create_generator("blf", files, None, config)


def make_mathutils_rule(
        config: 'fbm.PackageGeneratorConfig') -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/mathutils*.rst")
    mod_files = [
        f"{MOD_FILES_DIR}/mods/common/analyzer/append/mathutils.bvhtree.mod.rst"
        .replace("\\", "/"),
        f"{MOD_FILES_DIR}/mods/common/analyzer/append/mathutils.kdtree.mod.rst"
        .replace("\\", "/"),
        f"{MOD_FILES_DIR}/mods/common/analyzer/append/mathutils.mod.rst"
        .replace("\\", "/"),
    ]
    if config.target == "blender" and config.mod_version in ["2.78", "2.79"]:
        mod_files.append(
            f"{MOD_FILES_DIR}/mods/{config.mod_version}/analyzer/new/"
            "mathutils.noise.types.mod.rst".replace("\\", "/"))
    return create_generator("mathutils", files, mod_files, config)


def make_gpu_rule(
        config: 'fbm.PackageGeneratorConfig') -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/gpu*.rst")
    return create_generator("gpu", files, None, config)


def make_gpu_extras_rule(
        config: 'fbm.PackageGeneratorConfig') -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/gpu_extras*.rst")
    mod_files = []
    if config.target == "blender":
        if config.mod_version not in ["2.78", "2.79"]:
            mod_files.extend(
                glob.glob(
                    f"{MOD_FILES_DIR}/mods/generated_mods/gen_modules_modfile/"
                    "gpu_extras.*.mod.rst".replace("\\", "/")))
    elif config.target == "upbge":
        if config.mod_version not in ["0.2.5"]:
            mod_files.extend(
                glob.glob(
                    f"{MOD_FILES_DIR}/mods/generated_mods/gen_modules_modfile/"
                    "gpu_extras.*.mod.rst".replace("\\", "/")))
    return create_generator("gpu_extras", files, mod_files, config)


def make_freestyle_rule(
        config: 'fbm.PackageGeneratorConfig') -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/freestyle*.rst")
    return create_generator("freestyle", files, None, config)


def make_bpy_extras_rule(
        config: 'fbm.PackageGeneratorConfig') -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/bpy_extras*.rst")
    mod_files = glob.glob(
        f"{MOD_FILES_DIR}/mods/generated_mods/gen_modules_modfile/"
        "bpy_extras.*.mod.rst".replace("\\", "/"))
    mod_files = None
    return create_generator("bpy_extras", files, mod_files, config)


def make_aud_rule(
        config: 'fbm.PackageGeneratorConfig') -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/aud*.rst")
    return create_generator("aud", files, None, config)


def make_bmesh_rule(
        config: 'fbm.PackageGeneratorConfig') -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/bmesh*.rst")
    mod_files = [
        f"{MOD_FILES_DIR}/mods/common/analyzer/append/bmesh.types.mod.rst"
        .replace("\\", "/"),
    ]
    return create_generator("bmesh", files, mod_files, config)


def make_idprop_rule(
        config: 'fbm.PackageGeneratorConfig') -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/idprop*.rst")
    return create_generator("idprop", files, None, config)


def make_imbuf_rule(
        config: 'fbm.PackageGeneratorConfig') -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/imbuf*.rst")
    return create_generator("imbuf", files, None, config)


def make_bl_math_rule(
        config: 'fbm.PackageGeneratorConfig') -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/bl_math*.rst")
    return create_generator("bl_math", files, None, config)


def make_bge_rule(
        config: 'fbm.PackageGeneratorConfig') -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/bge*.rst")
    files.extend(glob.glob(INPUT_DIR + "/bge_types/bge*.rst"))
    return create_generator("bge", files, None, config)


def make_other_rules(config: 'fbm.PackageGeneratorConfig') -> List['fbm.PackageGenerationRule']:    # noqa # pylint: disable=C0301
    mod_files = glob.glob(
        f"{MOD_FILES_DIR}/mods/generated_mods/gen_modules_modfile/*.mod.rst"
        .replace("\\", "/"))
    mod_files += glob.glob(
        f"{MOD_FILES_DIR}/mods/generated_mods/gen_startup_modfile/*.mod.rst"
        .replace("\\", "/"))
    exclude_mod_files = glob.glob(
        f"{MOD_FILES_DIR}/mods/generated_mods/gen_startup_modfile/bpy.*.mod.rst"
        .replace("\\", "/"))
    exclude_mod_files += glob.glob(
        f"{MOD_FILES_DIR}/mods/generated_mods/gen_modules_modfile/bpy_extras.*.mod.rst"
        .replace("\\", "/"))
    exclude_mod_files += glob.glob(
        f"{MOD_FILES_DIR}/mods/generated_mods/gen_modules_modfile/bpy.*.mod.rst"
        .replace("\\", "/"))
    mod_files = set(mod_files) - set(exclude_mod_files)

    if config.target == "blender":
        if config.mod_version not in ["2.78", "2.79"]:
            mod_files -= set(glob.glob(
                f"{MOD_FILES_DIR}/mods/generated_mods/gen_modules_modfile/"
                "gpu_extras.*.mod.rst".replace("\\", "/"),
            ))
    elif config.target == "upbge":
        if config.mod_version not in ["0.2.5"]:
            mod_files -= set(glob.glob(
                f"{MOD_FILES_DIR}/mods/generated_mods/gen_modules_modfile/"
                "gpu_extras.*.mod.rst".replace("\\", "/"),
            ))

    regex = re.compile(r".. module:: (.*)")
    modules = {}
    for mod_file in mod_files:
        mod_name = None
        with open(mod_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                if m := regex.match(line):
                    mod_name = m.group(1)
                    break
        if mod_name is None:
            raise ValueError(f"{mod_file} does not contain module directive.")

        index = mod_name.find(".")
        if index != -1:
            mod_name = mod_name[:index]
        if mod_name not in modules:
            modules[mod_name] = []
        modules[mod_name].append(mod_file)

    rules = []
    for mod_name, files in modules.items():
        rules.append(create_generator(mod_name, [], files, config))
    return rules


def parse_options(config: 'fbm.PackageGeneratorConfig'):
    # pylint: disable=W0603
    global INPUT_DIR  # pylint: disable=W0602
    usage = f"Usage: python {__file__} [-i <input_dir>] [-o <output_dir>] " \
            "[-T <target>] [-t <target_version>] [-d] [-f <style_format>] " \
            "[-m <mod_version>]"
    parser = argparse.ArgumentParser(usage)
    parser.add_argument(
        "-i", dest="input_dir", type=str, help="Input directory"
    )
    parser.add_argument(
        "-o", dest="output_dir", type=str, help="Output directory"
    )
    parser.add_argument(
        "-d", dest="dump", action="store_true",
        help="Dump intermediate structure to JSON files"
    )
    parser.add_argument(
        "-f", dest="style_format", type=str,
        help="Style format (none, yapf, ruff)"
    )
    parser.add_argument(
        "-m", dest="mod_version", type=str,
        help="Blender version for specific mod patches to be applied "
             "(ex. 2.79, 2.80)"
    )
    parser.add_argument(
        "-T", dest="target", type=str,
        help="Target (blender, upbge)"
    )
    parser.add_argument(
        "-t", dest="target_version", type=str,
        help="Target version (ex. 2.79, 2.80)"
    )
    parser.add_argument(
        "-l", dest="output_log_level", type=str,
        help="Output log level (debug, info, notice, warn, err"
    )
    args = parser.parse_args()
    if args.input_dir:
        INPUT_DIR = args.input_dir
    if args.output_dir:
        config.output_dir = args.output_dir

    if args.style_format in fbm.support.SUPPORTED_STYLE_FORMAT:
        config.style_format = args.style_format
    else:
        raise RuntimeError(
            f"Not supported style format {args.style_format}. "
            f"(Supported Style Format: {fbm.support.SUPPORTED_STYLE_FORMAT})")

    if args.target in fbm.support.SUPPORTED_TARGET:
        config.target = args.target
    else:
        raise RuntimeError(
            f"Not supported target {args.target}."
            f"(Supported Target: {fbm.support.SUPPORTED_TARGET})")

    if args.target == "blender":
        if args.target_version in fbm.support.SUPPORTED_BLENDER_VERSION:
            config.target_version = args.target_version
        else:
            raise RuntimeError(
                f"Not supported blender version {args.target_version}. "
                f"(Supported Version: "
                f"{fbm.support.SUPPORTED_BLENDER_VERSION})")

    if args.target == "upbge":
        if args.target_version in fbm.support.SUPPORTED_UPBGE_VERSION:
            config.target_version = args.target_version
        else:
            raise RuntimeError(
                f"Not supported upbge version {args.target_version}. "
                f"(Supported Version: {fbm.support.SUPPORTED_UPBGE_VERSION})")

    if args.mod_version:
        if config.target == "blender":
            if args.mod_version in fbm.support.SUPPORTED_MOD_BLENDER_VERSION:
                config.mod_version = args.mod_version
            else:
                raise RuntimeError(
                    f"Not supported mod version {args.mod_version}. "
                    f"(Supported Version: "
                    f"{fbm.support.SUPPORTED_MOD_BLENDER_VERSION})")
        elif config.target == "upbge":
            if args.mod_version in fbm.support.SUPPORTED_MOD_UPBGE_VERSION:
                config.mod_version = args.mod_version
            else:
                raise RuntimeError(
                    f"Not supported mod version {args.mod_version}. "
                    f"(Supported Version: "
                    f"{fbm.support.SUPPORTED_MOD_UPBGE_VERSION})")

    if args.output_log_level:
        ARG_TO_LOG_LEVEL = {
            "debug": fbm.utils.LOG_LEVEL_DEBUG,
            "info": fbm.utils.LOG_LEVEL_INFO,
            "notice": fbm.utils.LOG_LEVEL_NOTICE,
            "warn": fbm.utils.LOG_LEVEL_WARN,
            "err": fbm.utils.LOG_LEVEL_ERR,
        }
        fbm.utils.LOG_LEVEL = ARG_TO_LOG_LEVEL[args.output_log_level]

    if args.dump:
        config.dump = True


def main():
    config = fbm.PackageGeneratorConfig()
    config.os = fbm.check_os()
    parse_options(config)

    pkg_generator = fbm.PackageGenerator(config)
    pkg_generator.add_rule(make_bpy_rule(config))
    pkg_generator.add_rule(make_bgl_rule(config))
    pkg_generator.add_rule(make_blf_rule(config))
    pkg_generator.add_rule(make_mathutils_rule(config))
    pkg_generator.add_rule(make_gpu_rule(config))
    pkg_generator.add_rule(make_gpu_extras_rule(config))
    pkg_generator.add_rule(make_freestyle_rule(config))
    pkg_generator.add_rule(make_bpy_extras_rule(config))
    pkg_generator.add_rule(make_aud_rule(config))
    pkg_generator.add_rule(make_bmesh_rule(config))
    pkg_generator.add_rule(make_idprop_rule(config))
    pkg_generator.add_rule(make_imbuf_rule(config))
    pkg_generator.add_rule(make_bl_math_rule(config))
    if config.target == "upbge":
        pkg_generator.add_rule(make_bge_rule(config))
    for rule in make_other_rules(config):
        pkg_generator.add_rule(rule)
    pkg_generator.generate()


if __name__ == "__main__":
    main()
