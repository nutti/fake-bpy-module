import os
import sys
import argparse
import unittest


class FakeBpyModuleTestConfig:
    def __init__(self):
        self.modules_path = ""


def parse_options(config: FakeBpyModuleTestConfig):
    usage = f"Usage: python {__file__} [-p <modules_path>]"
    parser = argparse.ArgumentParser(usage)
    parser.add_argument(
        "-p", dest="modules_path", type=str, help="fake-module path")

    args = parser.parse_args()
    if args.modules_path:
        config.modules_path = args.modules_path


def main():
    config = FakeBpyModuleTestConfig()
    parse_options(config)

    path = os.path.abspath(config.modules_path)
    sys.path.append(path)

    sys.path.append(os.path.dirname(__file__))
    import fake_bpy_module_test     # pylint: disable=C0415

    test_cases = [
        fake_bpy_module_test.utils_test.UtilsTest,

        fake_bpy_module_test.analyzer_test.BaseAnalyzerTest,

        fake_bpy_module_test.transformer_test.BaseClassFixtureTest,
        fake_bpy_module_test.transformer_test.BpyAppHandlersDataTypeAdderTest,
        fake_bpy_module_test.transformer_test.BpyContextVariableConverterTest,
        fake_bpy_module_test.transformer_test.BpyOpsOverrideParametersAdderTest,
        fake_bpy_module_test.transformer_test.BpyTypesClassBaseClassRebaserTest,
        fake_bpy_module_test.transformer_test.CannonicalDataTypeRewriterTest,
        fake_bpy_module_test.transformer_test.DataTypeRefinerTest,
        fake_bpy_module_test.transformer_test.DependencyBuilderTest,
        fake_bpy_module_test.transformer_test.ModApplierTest,
        fake_bpy_module_test.transformer_test.ModuleLevelAttributeFixtureTest,
        fake_bpy_module_test.transformer_test.RstSpecificNodeCleanerTest,
        fake_bpy_module_test.transformer_test.TargetFileCombinerTest,
        fake_bpy_module_test.transformer_test.FormatValidatorTest,
    ]

    suite = unittest.TestSuite()
    for case in test_cases:
        suite.addTest(unittest.makeSuite(case))
    ret = unittest.TextTestRunner().run(suite).wasSuccessful()
    sys.exit(not ret)


if __name__ == "__main__":
    main()
