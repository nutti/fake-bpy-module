# coding: UTF-8

import glob
import argparse

from fake_bpy_module.analyzer import (
    BaseAnalyzer,
    MathutilsAnalyzer,
    BpyAnalyzer,
    BglAnalyzer,
    BpyExtraAnalyzer,
    BmeshAnalyzer,
    GpuAnalyzer,
    FreestyleAnalyzer,
)
from fake_bpy_module.generator import (
    BaseGenerator,
    PackageGeneratorConfig,
    PackageGenerator,
    PackageGenerationRule,
)
from fake_bpy_module.utils import (
    check_os,
)

INPUT_DIR = "."
SUPPORTED_TARGET = ["pycharm"]
SUPPORTED_STYLE_FORMAT = ["none", "pep8"]


def make_bpy_rule():
    all_files = glob.glob(INPUT_DIR + "/bpy*.xml")
    excludes_files = glob.glob(INPUT_DIR + "/bpy_extras*.xml")
    files = list(set(all_files) - set(excludes_files))
    return PackageGenerationRule("bpy", files, BpyAnalyzer(), BaseGenerator())


def make_bgl_rule():
    files = glob.glob(INPUT_DIR + "/bgl*.xml")
    return PackageGenerationRule("bgl", files, BglAnalyzer(), BaseGenerator())


def make_blf_rule():
    files = glob.glob(INPUT_DIR + "/blf*.xml")
    return PackageGenerationRule("blf", files, BaseAnalyzer(), BaseGenerator())


def make_mathutils_rule():
    files = glob.glob(INPUT_DIR + "/mathutils*.xml")
    return PackageGenerationRule("mathutils", files, MathutilsAnalyzer(), BaseGenerator())


def make_gpu_rule():
    files = glob.glob(INPUT_DIR + "/gpu*.xml")
    return PackageGenerationRule("gpu", files, GpuAnalyzer(), BaseGenerator())


def make_freestyle_rule():
    files = glob.glob(INPUT_DIR + "/freestyle*.xml")
    return PackageGenerationRule("freestyle", files, FreestyleAnalyzer(), BaseGenerator())


def make_bpy_extra_rule():
    files = glob.glob(INPUT_DIR + "/bpy_extras*.xml")
    return PackageGenerationRule("bpy_extras", files, BpyExtraAnalyzer(), BaseGenerator())


def make_aud_rule():
    files = glob.glob(INPUT_DIR + "/aud*.xml")
    return PackageGenerationRule("aud", files, BaseAnalyzer(), BaseGenerator())


def make_bmesh_rule():
    files = glob.glob(INPUT_DIR + "/bmesh*.xml")
    return PackageGenerationRule("bmesh", files, BmeshAnalyzer(), BaseGenerator())

# TODO: gen bpy.context



def parse_options(config):
    global INPUT_DIR, SUPPORTED_TARGET
    usage = "Usage: python {} [-i <input_dir>] [-o <output_dir>] [-t <target>]"\
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
    config = PackageGeneratorConfig()
    config.os = check_os()
    parse_options(config)

    pkg_generator = PackageGenerator(config)
    pkg_generator.add_rule(make_bpy_rule())
    pkg_generator.add_rule(make_bgl_rule())
    pkg_generator.add_rule(make_blf_rule())
    pkg_generator.add_rule(make_mathutils_rule())
    pkg_generator.add_rule(make_gpu_rule())
    pkg_generator.add_rule(make_freestyle_rule())
    pkg_generator.add_rule(make_bpy_extra_rule())
    pkg_generator.add_rule(make_aud_rule())
    pkg_generator.add_rule(make_bmesh_rule())
    pkg_generator.generate()


if __name__ == "__main__":
    main()
