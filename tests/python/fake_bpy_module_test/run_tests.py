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
        fake_bpy_module_test.dag_test.DAGTest,
        fake_bpy_module_test.utils_test.UtilsTest,

        fake_bpy_module_test.docutils_based.analyzer_test.BaseAnalyzerTest,
        fake_bpy_module_test.docutils_based.transformer_test.TransformerTest,
        fake_bpy_module_test.docutils_based.cannonical_data_type_rewriter_test.CannonicalDataTypeRewriterTest,  # pylint: disable=C0301
        fake_bpy_module_test.docutils_based.data_type_refiner_test.DataTypeRefinerTest,
        fake_bpy_module_test.docutils_based.dependency_builder_test.DependencyBuilderTest,
        fake_bpy_module_test.docutils_based.mod_applier_test.ModApplierTest,
        fake_bpy_module_test.docutils_based.target_file_combiner_test.TargetFileCombinerTest,
    ]

    suite = unittest.TestSuite()
    for case in test_cases:
        suite.addTest(unittest.makeSuite(case))
    ret = unittest.TextTestRunner().run(suite).wasSuccessful()
    sys.exit(not ret)


if __name__ == "__main__":
    main()
