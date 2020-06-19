import os
import sys
import argparse
import unittest


SUPPORTED_VERSIONS = [
    "2.78", "2.79", "2.80", "2.81", "2.82" "2.83"
]


class FakeBpyModuleTestConfig:
    def __init__(self):
        self.modules_path = ""
        self.blender_version = None


def parse_options(config: FakeBpyModuleTestConfig):
    usage = "Usage: python {} [-p <modules_path>] [-v <blender_version]".format(__file__)
    parser = argparse.ArgumentParser(usage)
    parser.add_argument("-p", dest="modules_path", type=str, help="fake-bpy-module path")
    parser.add_argument("-v", dest="blender_version", type=str, help="blender version")

    args = parser.parse_args()
    if args.modules_path:
        config.modules_path = args.modules_path
    if args.blender_version not in SUPPORTED_VERSIONS:
        raise ValueError("Not supported version {}".format(arg.blender_version))
    config.blender_version = args.blender_version


def main():
    config = FakeBpyModuleTestConfig()
    parse_options(config)

    sys.path.append(os.path.dirname(__file__))
    import fake_bpy_module_test

    path = os.path.abspath(config.modules_path)
    sys.path.append(path)

    test_cases = [
        fake_bpy_module_test.bpy_test.BpyTest,
        fake_bpy_module_test.bgl_test.BglTest,
        fake_bpy_module_test.blf_test.BlfTest,
        fake_bpy_module_test.mathutils_test.MathutilsTest,
        fake_bpy_module_test.gpu_test.GpuTest,
        fake_bpy_module_test.freestyle_test.FreestyleTest,
        fake_bpy_module_test.bpy_extras_test.BpyExtrasTest,
        fake_bpy_module_test.aud_test.AudTest,
        fake_bpy_module_test.bmesh_test.BmeshTest,
    ]
    if config.blender_version in ["2.80", "2.81", "2.82"]:
        test_cases.append(fake_bpy_module_test.gpu_extras_test.GpuExtrasTest)

    suite = unittest.TestSuite()
    for case in test_cases:
        suite.addTest(unittest.makeSuite(case))
    ret = unittest.TextTestRunner().run(suite).wasSuccessful()
    sys.exit(not ret)


if __name__ == "__main__":
    main()
