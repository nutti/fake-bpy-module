import os
import sys
import argparse
import unittest


class FakeBpyModuleTestConfig:
    def __init__(self):
        self.modules_path = ""


def parse_options(config: FakeBpyModuleTestConfig):
    usage = "Usage: python {} [-p <modules_path>]".format(__file__)
    parser = argparse.ArgumentParser(usage)
    parser.add_argument("-p", dest="modules_path", type=str, help="fake-bpy-module path")

    args = parser.parse_args()
    if args.modules_path:
        config.modules_path = args.modules_path


def main():
    config = FakeBpyModuleTestConfig()
    parse_options(config)

    path = os.path.abspath(config.modules_path)
    sys.path.append(path)

    sys.path.append(os.path.dirname(__file__))
    import fake_bpy_module_test

    test_cases = [
        fake_bpy_module_test.analyzer_test.BaseAnalyzerTest,
        fake_bpy_module_test.analyzer_test.AnalyzerWithModFileTest,
        fake_bpy_module_test.dag_test.DAGTest,
        fake_bpy_module_test.generator_test.CodeWriterIndentTest,
        fake_bpy_module_test.generator_test.CodeWriterTest,
        fake_bpy_module_test.generator_test.BaseGeneratorTest,
        fake_bpy_module_test.generator_test.DependencyTest,
        fake_bpy_module_test.generator_test.GenerationInfoByTargetTest,
        fake_bpy_module_test.generator_test.GenerationInfoByRuleTest,
        fake_bpy_module_test.generator_test.PackageGeneratorConfigTest,
        fake_bpy_module_test.generator_test.PackageGenerationRuleTest,
        fake_bpy_module_test.generator_test.PackageAnalyzerTest,
        fake_bpy_module_test.generator_test.PackageGeneratorTest,
        fake_bpy_module_test.info_test.DataTypeTest,
        fake_bpy_module_test.info_test.UnknownDataTypeTest,
        fake_bpy_module_test.info_test.IntermidiateDataTypeTest,
        fake_bpy_module_test.info_test.BuiltinDataTypeTest,
        fake_bpy_module_test.info_test.ModifierDataTypeTest,
        fake_bpy_module_test.info_test.CustomDataTypeTest,
        fake_bpy_module_test.info_test.MixinDataTypeTest,
        fake_bpy_module_test.info_test.InfoTest,
        fake_bpy_module_test.info_test.ParameterDetailTest,
        fake_bpy_module_test.info_test.ReturnInfoTest,
        fake_bpy_module_test.info_test.VariableInfoTest,
        fake_bpy_module_test.info_test.FunctionInfoTest,
        fake_bpy_module_test.info_test.ClassInfoTest,
        fake_bpy_module_test.info_test.SectionInfoTest,
        fake_bpy_module_test.refiner_test.ModuleStructureTest,
        fake_bpy_module_test.refiner_test.EntryPointTest,
        fake_bpy_module_test.refiner_test.DataTypeRefinerTest,
        fake_bpy_module_test.utils_test.UtilsTest,
    ]

    suite = unittest.TestSuite()
    for case in test_cases:
        suite.addTest(unittest.makeSuite(case))
    ret = unittest.TextTestRunner().run(suite).wasSuccessful()
    sys.exit(not ret)


if __name__ == "__main__":
    main()
