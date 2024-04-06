import os
import docutils

# pylint: disable=E0401
from fake_bpy_module.analyzer.analyzer import (
    BaseAnalyzer
)
from . import common


class BaseAnalyzerTest(common.FakeBpyModuleTestBase):

    name = "BaseAnalyzerTest"
    module_name = __module__
    data_dir = os.path.abspath(
        f"{os.path.dirname(__file__)}/analyzer_test_data")

    def compare_with_file_contents(self, actual: str, expect_file: str):
        with open(expect_file, "r", encoding="utf-8") as f:
            expect = f.read()
        self.assertEqual(actual, expect)

    def test_no_contents(self):
        rst_files = ["no_contents.rst"]
        expect_files = ["no_contents.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), 1)
        self.compare_with_file_contents(documents[0].pformat(),
                                        expect_files[0])

    def test_only_base_class(self):
        rst_files = ["only_base_class.rst"]
        expect_files = ["only_base_class.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), 1)
        self.compare_with_file_contents(documents[0].pformat(),
                                        expect_files[0])

    def test_only_module_name(self):
        rst_files = ["only_module_class.rst"]
        expect_files = ["only_module_class.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), 1)
        self.compare_with_file_contents(documents[0].pformat(),
                                        expect_files[0])

    def test_single_constant(self):
        rst_files = ["single_constant.rst"]
        expect_files = ["single_constant.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), 1)
        self.compare_with_file_contents(documents[0].pformat(),
                                        expect_files[0])

    def test_multiple_constants(self):
        rst_files = ["multiple_constants.rst"]
        expect_files = ["multiple_constants.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), 1)
        self.compare_with_file_contents(documents[0].pformat(),
                                        expect_files[0])

    def test_single_function(self):
        rst_files = ["single_function.rst"]
        expect_files = ["single_function.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), 1)
        self.compare_with_file_contents(documents[0].pformat(),
                                        expect_files[0])

    def test_multiple_functions(self):
        rst_files = ["multiple_functions.rst"]
        expect_files = ["multiple_functions.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), 1)
        self.compare_with_file_contents(documents[0].pformat(),
                                        expect_files[0])

    def test_single_class(self):
        rst_files = ["single_class.rst"]
        expect_files = ["single_class.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), 1)
        self.compare_with_file_contents(documents[0].pformat(),
                                        expect_files[0])

    def test_multiple_classes(self):
        rst_files = ["multiple_classes.rst"]
        expect_files = ["multiple_classes.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), 1)
        self.compare_with_file_contents(documents[0].pformat(),
                                        expect_files[0])

    def test_noisy_1(self):
        rst_files = ["noisy_1.rst"]
        expect_files = ["noisy_1.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), 1)
        self.compare_with_file_contents(documents[0].pformat(),
                                        expect_files[0])

    def test_noisy_2(self):
        rst_files = ["noisy_2.rst"]
        expect_files = ["noisy_2.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), 1)
        self.compare_with_file_contents(documents[0].pformat(),
                                        expect_files[0])

    def test_invalid_rst_format_1(self):
        rst_files = ["invalid_rst_format_1.rst"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        with self.assertRaises(docutils.utils.SystemMessage):
            _ = analyzer.analyze(rst_files)

    def test_invalid_rst_format_2(self):
        rst_files = ["invalid_rst_format_2.rst"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        with self.assertRaises(docutils.utils.SystemMessage):
            _ = analyzer.analyze(rst_files)

    # TODO: move to transform_test.py
    # pylint: disable=W0101
    def test_no_module(self):

        return

        rst_files = ["no_module.rst"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        with self.assertRaises(docutils.utils.SystemMessage):
            _ = analyzer.analyze(rst_files)

    def test_bpy_290_tweak(self):
        rst_files = ["bpy_290_tweak.rst"]
        expect_files = ["bpy_290_tweak.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.90")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), 1)
        self.compare_with_file_contents(documents[0].pformat(),
                                        expect_files[0])

    def test_bge_support(self):
        rst_files = ["bge_support.rst"]
        expect_files = ["bge_support.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("upbge")
        analyzer.set_target_version("0.2.5")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), 1)
        self.compare_with_file_contents(documents[0].pformat(),
                                        expect_files[0])

    # TODO: move to transform_test.py
    # pylint: disable=W0101
    def test_bge_support_no_module(self):
        rst_files = ["bge.types.NoModule.rst"]
        expect_files = ["bge.types.NoModule.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("upbge")
        analyzer.set_target_version("0.2.5")
        documents = analyzer.analyze(rst_files)

        return

        self.assertEqual(len(documents), 1)
        self.compare_with_file_contents(documents[0].pformat(),
                                        expect_files[0])

    def test_invalid_function(self):
        rst_files = ["invalid_function.rst"]
        expect_files = ["invalid_function.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("upbge")
        analyzer.set_target_version("0.2.5")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), 1)
        self.compare_with_file_contents(documents[0].pformat(),
                                        expect_files[0])

    def test_invalid_function_arg_order(self):
        rst_files = ["invalid_function_arg_order.rst"]
        expect_files = ["invalid_function_arg_order.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("upbge")
        analyzer.set_target_version("0.2.5")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), 1)
        self.compare_with_file_contents(documents[0].pformat(),
                                        expect_files[0])
