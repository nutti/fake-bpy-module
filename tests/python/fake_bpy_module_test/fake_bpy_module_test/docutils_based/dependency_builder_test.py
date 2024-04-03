import os

# pylint: disable=E0401
from fake_bpy_module.analyzer import BaseAnalyzer
from fake_bpy_module.docutils_based.transformer.transformer import Transformer
from fake_bpy_module.docutils_based.transformer.common import ModuleStructure
from .. import common


class DependencyBuilderTest(common.FakeBpyModuleTestBase):

    name = "DependencyBuilder"
    module_name = __module__
    data_dir = os.path.abspath(
        f"{os.path.dirname(__file__)}/../transformer_test_data")

    def compare_with_file_contents(self, actual: str, expect_file: str):
        with open(expect_file, "r", encoding="utf-8") as f:
            expect = f.read()
        self.assertEqual(actual, expect)

    def test_basic(self):
        rst_files = [
            "dependency_builder.rst",
        ]
        expect_files = [
            "dependency_builder.xml",
        ]
        expect_transformed_files = [
            "dependency_builder_transformed.xml",
        ]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}" for f in expect_transformed_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        package_structure = ModuleStructure()

        module_a_structure = ModuleStructure()
        module_a_structure.name = "module_1"
        package_structure.add_child(module_a_structure)
        module_structure = ModuleStructure()
        module_structure.name = "submodule_1"
        module_a_structure.add_child(module_structure)
        module_structure = ModuleStructure()
        module_structure.name = "submodule_2"
        module_a_structure.add_child(module_structure)

        module_b_structure = ModuleStructure()
        module_b_structure.name = "module_2"
        package_structure.add_child(module_b_structure)
        module_structure = ModuleStructure()
        module_structure.name = "submodule_3"
        module_b_structure.add_child(module_structure)

        self.assertEqual(len(documents), 1)
        for i, document in enumerate(documents):
            self.compare_with_file_contents(document.pformat(),
                                            expect_files[i])

        transformer = Transformer(["dependency_builder"], {
            "dependency_builder": {
                "package_structure": package_structure,
            }
        })
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), 1)
        for i, document in enumerate(transformed):
            self.compare_with_file_contents(document.pformat(),
                                            expect_transformed_files[i])
