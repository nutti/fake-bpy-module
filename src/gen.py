# coding: UTF-8

import glob
import argparse
from typing import List
import os

import fake_bpy_module as fbm

INPUT_DIR: str = "."
SUPPORTED_TARGET: List[str] = ["pycharm"]
SUPPORTED_STYLE_FORMAT: List[str] = ["none", "pep8"]
SUPPORTED_MOD_BLENDER_VERSION: List[str] = [
    "2.78", "2.79", "2.80", "2.81", "2.82"
]
MOD_FILES_DIR: str = os.path.dirname(os.path.abspath(__file__))


class MathutilsAnalyzer(fbm.AnalyzerWithModFile):
    def _modify_post_process(self, result: 'fbm.AnalysisResult'):
        for section in result.section_info:
            for info in section.info_list:
                if info.type() == "function":
                    for i, p in enumerate(info.parameters()):
                        converted = p
                        converted = converted.replace("=noise.types.STDPERLIN", "=types.STDPERLIN")
                        converted = converted.replace("=noise.distance_metrics.DISTANCE", "=None")
                        info.set_parameter(i, converted)
                elif info.type() == "class":
                    for m in info.methods():
                        for i, p in enumerate(m.parameters()):
                            converted = p
                            converted = converted.replace("=noise.types.STDPERLIN", "=types.STDPERLIN")
                            converted = converted.replace("=noise.distance_metrics.DISTANCE", "=None")
                            m.set_parameter(i, converted)


class BglAnalyzer(fbm.AnalyzerWithModFile):
    def _modify_post_process(self, result: 'fbm.AnalysisResult'):
        for section in result.section_info:
            for info in section.info_list:
                if info.type() == "function":
                    if info.module() is None:
                        info.set_module("bgl")


class FreestyleAnalyzer(fbm.AnalyzerWithModFile):
    def _modify_post_process(self, result: 'fbm.AnalysisResult'):
        for section in result.section_info:
            for info in section.info_list:
                if info.type() == "function":
                    for i, p in enumerate(info.parameters()):
                        info.set_parameter(i, p.replace("=IntegrationType.MEAN", "=None"))
                elif info.type() == "class":
                    for m in info.methods():
                        for i, p in enumerate(m.parameters()):
                            m.set_parameter(i, p.replace("=IntegrationType.MEAN", "=None"))


class BpyAnalyzer(fbm.AnalyzerWithModFile):
    def _modify_post_process(self, result: 'fbm.AnalysisResult'):
        for section in result.section_info:
            for info in section.info_list:
                if info.type() == "function":
                    for i, p in enumerate(info.parameters()):
                        info.set_parameter(i, p.replace("=bpy.context.scene.frame_current", "=None"))
                elif info.type() == "class":
                    for m in info.methods():
                        for i, p in enumerate(m.parameters()):
                            m.set_parameter(i, p.replace("=bpy.context.scene.frame_current", "=None"))


def make_bpy_rule(config: 'fbm.PackageGeneratorConfig') -> 'fbm.PackageGenerationRule':
    all_files = glob.glob(INPUT_DIR + "/bpy*.xml")
    excludes_files = glob.glob(INPUT_DIR + "/bpy_extras*.xml")
    files = list(set(all_files) - set(excludes_files))
    mod_files = [
        "{}/mods/common/analyzer/bpy.json".format(MOD_FILES_DIR).replace("\\", "/"),
        "{}/mods/generated_mods/gen_startup_modfile/bpy.json".format(MOD_FILES_DIR).replace("\\", "/"),
        "{}/mods/generated_mods/gen_modules_modfile/bpy.json".format(MOD_FILES_DIR).replace("\\", "/"),
    ]
    if config.mod_version in ["2.80"]:
        mod_files.append("{}/mods/2.80/analyzer/bpy.json".format(MOD_FILES_DIR).replace("\\", "/"))
    elif config.mod_version in ["2.81"]:
        mod_files.append("{}/mods/2.81/analyzer/bpy.json".format(MOD_FILES_DIR).replace("\\", "/"))
    elif config.mod_version in ["2.82"]:
        mod_files.append("{}/mods/2.82/analyzer/bpy.json".format(MOD_FILES_DIR).replace("\\", "/"))
    return fbm.PackageGenerationRule("bpy", files, BpyAnalyzer(mod_files), fbm.BaseGenerator())


def make_bgl_rule(config: 'fbm.PackageGeneratorConfig') -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/bgl*.xml")
    mod_files = [
        "{}/mods/generated_mods/gen_bgl_modfile/bgl.json".format(MOD_FILES_DIR).replace("\\", "/"),
    ]
    return fbm.PackageGenerationRule("bgl", files, BglAnalyzer(mod_files), fbm.BaseGenerator())


def make_blf_rule(config: 'fbm.PackageGeneratorConfig') -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/blf*.xml")
    return fbm.PackageGenerationRule("blf", files, fbm.BaseAnalyzer(), fbm.BaseGenerator())


def make_mathutils_rule(config: 'fbm.PackageGeneratorConfig') -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/mathutils*.xml")
    mod_files = [
        "{}/mods/common/analyzer/mathutils.json".format(MOD_FILES_DIR).replace("\\", "/"),
    ]
    return fbm.PackageGenerationRule("mathutils", files, MathutilsAnalyzer(mod_files), fbm.BaseGenerator())


def make_gpu_rule(config: 'fbm.PackageGeneratorConfig') -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/gpu*.xml")
    mod_files = [
        "{}/mods/common/analyzer/gpu.json".format(MOD_FILES_DIR).replace("\\", "/"),
    ]
    return fbm.PackageGenerationRule("gpu", files, fbm.AnalyzerWithModFile(mod_files), fbm.BaseGenerator())


def make_gpu_extras_rule(config: 'fbm.PackageGeneratorConfig') -> 'fbm.PackageGenerationRule':
    all_files = glob.glob(INPUT_DIR + "/bpy_extras*.xml")
    excludes_files = glob.glob(INPUT_DIR + "/bpy_extras*.xml")
    files = list(set(all_files) - set(excludes_files))
    mod_files = []
    if config.mod_version in ["2.80", "2.81", "2.82"]:
        mod_files.append("{}/mods/generated_mods/gen_modules_modfile/gpu_extras.json".format(MOD_FILES_DIR).replace("\\", "/"))
    return fbm.PackageGenerationRule("gpu_extras", files, fbm.AnalyzerWithModFile(mod_files), fbm.BaseGenerator())


def make_freestyle_rule(config: 'fbm.PackageGeneratorConfig') -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/freestyle*.xml")
    mod_files = [
        "{}/mods/common/analyzer/freestyle.json".format(MOD_FILES_DIR).replace("\\", "/"),
    ]
    return fbm.PackageGenerationRule("freestyle", files, FreestyleAnalyzer(mod_files), fbm.BaseGenerator())


def make_bpy_extras_rule(config: 'fbm.PackageGeneratorConfig') -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/bpy_extras*.xml")
    mod_files = [
        "{}/mods/common/analyzer/bpy_extras.json".format(MOD_FILES_DIR).replace("\\", "/"),
        "{}/mods/generated_mods/gen_modules_modfile/bpy_extras.json".format(MOD_FILES_DIR).replace("\\", "/")
    ]
    return fbm.PackageGenerationRule("bpy_extras", files, fbm.AnalyzerWithModFile(mod_files), fbm.BaseGenerator())


def make_aud_rule(config: 'fbm.PackageGeneratorConfig') -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/aud*.xml")
    return fbm.PackageGenerationRule("aud", files, fbm.BaseAnalyzer(), fbm.BaseGenerator())


def make_bmesh_rule(config: 'fbm.PackageGeneratorConfig') -> 'fbm.PackageGenerationRule':
    files = glob.glob(INPUT_DIR + "/bmesh*.xml")
    mod_files = [
        "{}/mods/common/analyzer/bmesh.json".format(MOD_FILES_DIR).replace("\\", "/"),
    ]
    return fbm.PackageGenerationRule("bmesh", files, fbm.AnalyzerWithModFile(mod_files), fbm.BaseGenerator())


def make_other_rules(config: 'fbm.PackageGeneratorConfig') -> List['fbm.PackageGenerationRule']:
    mod_files = glob.glob("{}/mods/generated_mods/gen_modules_modfile/*.json".format(MOD_FILES_DIR).replace("\\", "/"))
    mod_files = set(mod_files) - {
        "{}/mods/generated_mods/gen_modules_modfile/bpy.json".format(MOD_FILES_DIR).replace("\\", "/"),
        "{}/mods/generated_mods/gen_modules_modfile/bpy_extras.json".format(MOD_FILES_DIR).replace("\\", "/"),
    }

    if config.mod_version in ["2.80", "2.81", "2.82"]:
        mod_files -= {
            "{}/mods/generated_mods/gen_modules_modfile/gpu_extras.json".format(MOD_FILES_DIR).replace("\\", "/"),
        }

    rules = []
    for mod_file in mod_files:
        mod_name = mod_file[mod_file.rfind("/") + 1:].replace(".json", "")
        rules.append(fbm.PackageGenerationRule(mod_name, [], fbm.AnalyzerWithModFile([mod_file]), fbm.BaseGenerator()))
    return rules


def parse_options(config: 'fbm.PackageGeneratorConfig'):
    global INPUT_DIR, SUPPORTED_TARGET
    usage = "Usage: python {} [-i <input_dir>] [-o <output_dir>] [-d] [-f <style_format>] [-m <mod_version>]"\
        .format(__file__)
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
        "-f", dest="style_format", type=str, help="Style format (None, pep8)"
    )
    parser.add_argument(
        "-m", dest="mod_version", type=str,
        help="Blender version for specific mod patches to be applied (ex. 2.79, 2.80)"
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
    if args.mod_version:
        if args.mod_version in SUPPORTED_MOD_BLENDER_VERSION:
            config.mod_version = args.mod_version
        else:
            raise RuntimeError("Not supported mod version {}. "
                               "(Supported Version: {})"
                               .format(args.mod_version, SUPPORTED_MOD_BLENDER_VERSION))

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
    for rule in make_other_rules(config):
        pkg_generator.add_rule(rule)
    pkg_generator.generate()


if __name__ == "__main__":
    main()
