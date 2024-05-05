# coding: UTF-8

import glob
import argparse
from typing import List, Tuple
import os

import fake_bpy_module as fbm

INPUT_DIR: str = "."
MOD_FILES_DIR: str = os.path.dirname(os.path.abspath(__file__))


def generate(target_files: List[str], mod_files: List[str]):
    documents = fbm.analyze(target_files)
    documents = fbm.transform(documents, mod_files)
    fbm.generate(documents)


def parse_options():
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
        fbm.config.set_output_dir(args.output_dir)

    if args.style_format in fbm.support.SUPPORTED_STYLE_FORMAT:
        fbm.config.set_style_format(args.style_format)
    else:
        raise RuntimeError(
            f"Not supported style format {args.style_format}. "
            f"(Supported Style Format: {fbm.support.SUPPORTED_STYLE_FORMAT})")

    if args.target in fbm.support.SUPPORTED_TARGET:
        fbm.config.set_target(args.target)
    else:
        raise RuntimeError(
            f"Not supported target {args.target}."
            f"(Supported Target: {fbm.support.SUPPORTED_TARGET})")

    if args.target == "blender":
        if args.target_version in fbm.support.SUPPORTED_BLENDER_VERSION:
            fbm.config.set_target_version(args.target_version)
        else:
            raise RuntimeError(
                f"Not supported blender version {args.target_version}. "
                f"(Supported Version: "
                f"{fbm.support.SUPPORTED_BLENDER_VERSION})")

    if args.target == "upbge":
        if args.target_version in fbm.support.SUPPORTED_UPBGE_VERSION:
            fbm.config.set_target_version(args.target_version)
        else:
            raise RuntimeError(
                f"Not supported upbge version {args.target_version}. "
                f"(Supported Version: {fbm.support.SUPPORTED_UPBGE_VERSION})")

    if args.mod_version:
        if fbm.config.get_target() == "blender":
            if args.mod_version in fbm.support.SUPPORTED_MOD_BLENDER_VERSION:
                fbm.config.set_mod_version(args.mod_version)
            else:
                raise RuntimeError(
                    f"Not supported mod version {args.mod_version}. "
                    f"(Supported Version: "
                    f"{fbm.support.SUPPORTED_MOD_BLENDER_VERSION})")
        elif fbm.config.get_target() == "upbge":
            if args.mod_version in fbm.support.SUPPORTED_MOD_UPBGE_VERSION:
                fbm.config.set_mod_version(args.mod_version)
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


def collect_files() -> Tuple[str, str]:
    # Collect all rst files.
    rst_files = glob.glob(f"{INPUT_DIR}/**/*.rst", recursive=True)

    # Collect all mod files.
    mod_files = glob.glob(f"{MOD_FILES_DIR}/mods/generated_mods/**/*.mod.rst", recursive=True)
    mod_files += glob.glob(f"{MOD_FILES_DIR}/mods/common/**/*.mod.rst", recursive=True)
    if fbm.config.get_target() == "blender" and fbm.config.get_mod_version() in ["2.78", "2.79"]:
        mod_files += glob.glob(f"{MOD_FILES_DIR}/mods/{fbm.config.get_mod_version()}/**/*.mod.rst",
                               recursive=True)
    # Remove unnecessary mod files.
    mod_files = set(mod_files)
    if fbm.config.get_target() == "blender":
        if fbm.config.get_mod_version() not in ["2.78", "2.79"]:
            mod_files -= set(glob.glob(
                f"{MOD_FILES_DIR}/mods/generated_mods/gen_modules_modfile/gpu_extras.*.mod.rst"
            ))
    elif fbm.config.get_target() == "upbge":
        if fbm.config.get_mod_version() not in ["0.2.5"]:
            mod_files -= set(glob.glob(
                f"{MOD_FILES_DIR}/mods/generated_mods/gen_modules_modfile/gpu_extras.*.mod.rst"
            ))
    # TODO: sorted() is needed to solve unexpected errors.
    #       The error comes from the invalid processes in mod_applier when there are
    #       more than 2 mod files targeted for the same module.
    mod_files = sorted(mod_files)

    return rst_files, mod_files


def main():
    parse_options()
    rst_files, mod_files = collect_files()
    generate(rst_files, mod_files)


if __name__ == "__main__":
    main()
