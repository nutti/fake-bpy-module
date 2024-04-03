import os

# pylint: disable=E0401
from fake_bpy_module.analyzer import BaseAnalyzer
from fake_bpy_module.docutils_based.transformer.transformer import Transformer
from .. import common


class TargetFileCombinerTest(common.FakeBpyModuleTestBase):

    name = "TargetFileCombiner"
    module_name = __module__
    data_dir = os.path.abspath(
        f"{os.path.dirname(__file__)}/../transformer_test_data")

    def compare_with_file_contents(self, actual: str, expect_file: str):
        with open(expect_file, "r", encoding="utf-8") as f:
            expect = f.read()
        self.assertEqual(actual, expect)

    def test_combine(self):
        rst_files = [
            "target_file_combiner_combine_module_1_a.rst",
            "target_file_combiner_combine_module_1_b.rst",
            "target_file_combiner_combine_module_2.rst",
        ]
        expect_files = [
            "target_file_combiner_combine_module_1_a.xml",
            "target_file_combiner_combine_module_1_b.xml",
            "target_file_combiner_combine_module_2.xml",
        ]
        expect_transformed_files = [
            "target_file_combiner_combine_module_1_transformed.xml",
            "target_file_combiner_combine_module_2_transformed.xml",
        ]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}" for f in expect_transformed_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), 3)
        for i, document in enumerate(documents):
            self.compare_with_file_contents(document.pformat(),
                                            expect_files[i])

        transformer = Transformer(["target_file_combiner"])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), 2)
        for i, document in enumerate(transformed):
            self.compare_with_file_contents(document.pformat(),
                                            expect_transformed_files[i])

    def test_child_module(self):
        rst_files = [
            "target_file_combiner_child_module_module_1.rst",
            "target_file_combiner_child_module_module_1_submodule_1.rst",
        ]
        expect_files = [
            "target_file_combiner_child_module_module_1.xml",
            "target_file_combiner_child_module_module_1_submodule_1.xml",
        ]
        expect_transformed_files = [
            "target_file_combiner_child_module_module_1_transformed.xml",
            "target_file_combiner_child_module_module_1_submodule_1_transformed.xml",
        ]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}" for f in expect_transformed_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), 2)
        for i, document in enumerate(documents):
            self.compare_with_file_contents(document.pformat(),
                                            expect_files[i])

        transformer = Transformer(["target_file_combiner"])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), 2)
        for i, document in enumerate(transformed):
            self.compare_with_file_contents(document.pformat(),
                                            expect_transformed_files[i])
