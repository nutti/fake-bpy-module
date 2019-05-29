# coding: UTF-8

import glob
import argparse
from typing import List
import os

import fake_bpy_module as fbm

INPUT_DIR: str = "."
SUPPORTED_TARGET: List[str] = ["pycharm"]
SUPPORTED_STYLE_FORMAT: List[str] = ["none", "pep8"]
MOD_FILES_DIR: str = os.path.dirname(os.path.abspath(__file__))


class BglAnalyzer(fbm.BaseAnalyzer):
    def _modify(self, result: 'fbm.AnalysisResult'):
        for section in result.section_info:
            for info in section.info_list:
                if info.type() == "function":
                    if info.module() is None:
                        info.set_module("bgl")


def make_bpy_rule() -> 'fbm.PackageGenerationRule':
    all_files = glob.glob(INPUT_DIR + "/bpy*.xml")
    excludes_files = glob.glob(INPUT_DIR + "/bpy_extras*.xml")
    files = list(set(all_files) - set(excludes_files))
    mod_file = "{}/mods/analyzer/bpy.json".format(MOD_FILES_DIR)
    mod_file = mod_file.replace("\\", "/")
    return fbm.PackageGenerationRule("bpy", files, fbm.AnalyzerWithModFile(mod_file), fbm.BaseGenerator())


def make_bgl_rule() -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/bgl*.xml")
    return fbm.PackageGenerationRule("bgl", files, BglAnalyzer(), fbm.BaseGenerator())


def make_blf_rule() -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/blf*.xml")
    return fbm.PackageGenerationRule("blf", files, fbm.BaseAnalyzer(), fbm.BaseGenerator())


def make_mathutils_rule() -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/mathutils*.xml")
    mod_file = "{}/mods/analyzer/mathutils.json".format(MOD_FILES_DIR)
    mod_file = mod_file.replace("\\", "/")
    return fbm.PackageGenerationRule("mathutils", files, fbm.AnalyzerWithModFile(mod_file), fbm.BaseGenerator())


def make_gpu_rule() -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/gpu*.xml")
    mod_file = "{}/mods/analyzer/gpu.json".format(MOD_FILES_DIR)
    mod_file = mod_file.replace("\\", "/")
    return fbm.PackageGenerationRule("gpu", files, fbm.AnalyzerWithModFile(mod_file), fbm.BaseGenerator())


def make_gpu_extra_rule() -> 'fbm.PackageGenerationRule':
    all_files = glob.glob(INPUT_DIR + "/bpy_extras*.xml")
    excludes_files = glob.glob(INPUT_DIR + "/bpy_extras*.xml")
    files = list(set(all_files) - set(excludes_files))
    return fbm.PackageGenerationRule("gpu_extras", files, fbm.BaseAnalyzer(), fbm.BaseGenerator())


def make_freestyle_rule() -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/freestyle*.xml")
    mod_file = "{}/mods/analyzer/freestyle.json".format(MOD_FILES_DIR)
    mod_file = mod_file.replace("\\", "/")
    return fbm.PackageGenerationRule("freestyle", files, fbm.AnalyzerWithModFile(mod_file), fbm.BaseGenerator())


def make_bpy_extra_rule() -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/bpy_extras*.xml")
    mod_file = "{}/mods/analyzer/bpy_extra.json".format(MOD_FILES_DIR)
    mod_file = mod_file.replace("\\", "/")
    return fbm.PackageGenerationRule("bpy_extras", files, fbm.AnalyzerWithModFile(mod_file), fbm.BaseGenerator())


def make_aud_rule() -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/aud*.xml")
    return fbm.PackageGenerationRule("aud", files, fbm.BaseAnalyzer(), fbm.BaseGenerator())


def make_bmesh_rule() -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/bmesh*.xml")
    mod_file = "{}/mods/analyzer/bmesh.json".format(MOD_FILES_DIR)
    mod_file = mod_file.replace("\\", "/")
    return fbm.PackageGenerationRule("bmesh", files, fbm.AnalyzerWithModFile(mod_file), fbm.BaseGenerator())


def parse_options(config: 'fbm.PackageGeneratorConfig'):
    global INPUT_DIR, SUPPORTED_TARGET
    usage = "Usage: python {} [-i <input_dir>] [-o <output_dir>] [-d] [-f <style-format>]"\
        .format(__file__)
    parser = argparse.ArgumentParser(usage)
    parser.add_argument(
        "-i", dest="input_dir", type=str, help="Input Directory"
    )
    parser.add_argument(
        "-o", dest="output_dir", type=str, help="Output Directory"
    )
    parser.add_argument(
        "-d", dest="dump", action="store_true",
        help="Dump intermediate structure to JSON files"
    )
    parser.add_argument(
        "-f", dest="style_format", type=str, help="Style format (None, pep8)"
    )
    args = parser.parse_args()
    if args.input_dir:
        INPUT_DIR = args.input_dir
    if args.output_dir:
        config.output_dir = args.output_dir

    if args.style_format in SUPPORTED_STYLE_FORMAT:
        config.style_format = args.style_format
    else:
        raise RuntimeError("Not supported style format {}. "
                           "(Supported Style Format: {})"
                           .format(args.style_format, SUPPORTED_STYLE_FORMAT))

    if args.dump:
        config.dump = True


def main():
    config = fbm.PackageGeneratorConfig()
    config.os = fbm.check_os()
    parse_options(config)

    pkg_generator = fbm.PackageGenerator(config)
    pkg_generator.add_rule(make_bpy_rule())
    pkg_generator.add_rule(make_bgl_rule())
    pkg_generator.add_rule(make_blf_rule())
    pkg_generator.add_rule(make_mathutils_rule())
    pkg_generator.add_rule(make_gpu_rule())
    pkg_generator.add_rule(make_gpu_extra_rule())
    pkg_generator.add_rule(make_freestyle_rule())
    pkg_generator.add_rule(make_bpy_extra_rule())
    pkg_generator.add_rule(make_aud_rule())
    pkg_generator.add_rule(make_bmesh_rule())
    pkg_generator.generate()


if __name__ == "__main__":
    main()
