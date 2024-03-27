import os
from docutils import nodes
from docutils.core import publish_doctree

# pylint: disable=E0401
from fake_bpy_module.analyzer import BaseAnalyzer
from fake_bpy_module.docutils_based.transformer.transformer import Transformer
from .. import common


class TransformerTest(common.FakeBpyModuleTestBase):

    name = "TransformerTest"
    module_name = __module__
    data_dir = os.path.abspath(
        f"{os.path.dirname(__file__)}/../transformer_test_data")

    def compare_with_file_contents(self, actual: str, expect_file: str):
        with open(expect_file, "r", encoding="utf-8") as f:
            expect = f.read()
        self.assertEqual(actual, expect)

    def test_base_class_fixture(self):
        rst_files = ["base_class_fixture.rst"]
        expect_files = ["base_class_fixture.xml"]
        expect_transformed_files = ["base_class_fixture_transformed.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}" for f in expect_transformed_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), 1)
        self.compare_with_file_contents(documents[0].pformat(),
                                        expect_files[0])

        transformer = Transformer(["base_class_fixture"])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), 1)
        self.compare_with_file_contents(transformed[0].pformat(),
                                        expect_transformed_files[0])

    def test_module_level_attribute_fixture(self):
        rst_files = ["module_level_attribute_fixture.rst"]
        expect_files = ["module_level_attribute_fixture.xml"]
        expect_transformed_files = ["module_level_attribute_fixture_transformed.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}" for f in expect_transformed_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), 1)
        self.compare_with_file_contents(documents[0].pformat(),
                                        expect_files[0])

        transformer = Transformer(["module_level_attribute_fixture"])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), 1)
        self.compare_with_file_contents(transformed[0].pformat(),
                                        expect_transformed_files[0])

    def test_bpy_app_handlers_data_type_adder(self):
        rst_files = ["bpy_app_handlers_data_type_adder.rst"]
        expect_files = ["bpy_app_handlers_data_type_adder.xml"]
        expect_transformed_files = ["bpy_app_handlers_data_type_adder_transformed.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}" for f in expect_transformed_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), 1)
        self.compare_with_file_contents(documents[0].pformat(),
                                        expect_files[0])

        transformer = Transformer(["bpy_app_handlers_data_type_adder"])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), 1)
        self.compare_with_file_contents(transformed[0].pformat(),
                                        expect_transformed_files[0])

    def test_bpy_ops_override_parameters_adder(self):
        rst_files = ["bpy_ops_override_parameters_adder.rst"]
        expect_files = ["bpy_ops_override_parameters_adder.xml"]
        expect_transformed_files = ["bpy_ops_override_parameters_adder_transformed.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}" for f in expect_transformed_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), 1)
        self.compare_with_file_contents(documents[0].pformat(),
                                        expect_files[0])

        transformer = Transformer(["bpy_ops_override_parameters_adder"])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), 1)
        self.compare_with_file_contents(transformed[0].pformat(),
                                        expect_transformed_files[0])

    def test_rst_specific_node_cleaner(self):
        rst_files = ["rst_specific_node_cleaner.rst"]
        expect_files = ["rst_specific_node_cleaner.xml"]
        expect_transformed_files = ["rst_specific_node_cleaner_transformed.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}" for f in expect_transformed_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), 1)
        self.compare_with_file_contents(documents[0].pformat(),
                                        expect_files[0])

        transformer = Transformer(["rst_specific_node_cleaner"])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), 1)
        self.compare_with_file_contents(transformed[0].pformat(),
                                        expect_transformed_files[0])

    def test_format_validator(self):
        document: nodes.document = publish_doctree(""".. module:: module.a

.. warning::

      Warning Contents
""")

        transformer = Transformer(["format_validator"])
        with self.assertRaises(ValueError):
            transformer.transform([document])

    def test_bpy_context_variable_converter(self):
        rst_files = [
            "bpy_context_variable_converter_1.rst",
            "bpy_context_variable_converter_2.rst",
            "bpy_context_variable_converter_3.rst"
        ]
        expect_files = [
            "bpy_context_variable_converter_1.xml",
            "bpy_context_variable_converter_2.xml",
            "bpy_context_variable_converter_3.xml"
        ]
        expect_transformed_files = [
            "bpy_context_variable_converter_transformed_1.xml",
            "bpy_context_variable_converter_transformed_2.xml"
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

        transformer = Transformer(["bpy_context_variable_converter"])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), 2)
        for i, t in enumerate(transformed):
            self.compare_with_file_contents(t.pformat(),
                                            expect_transformed_files[i])

    def test_bpy_types_class_base_class_rebaser(self):
        rst_files = ["bpy_types_class_base_class_rebaser.rst"]
        expect_files = ["bpy_types_class_base_class_rebaser.xml"]
        expect_transformed_files = ["bpy_types_class_base_class_rebaser_transformed.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}" for f in expect_transformed_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), 1)
        self.compare_with_file_contents(documents[0].pformat(),
                                        expect_files[0])

        transformer = Transformer(["bpy_types_class_base_class_rebaser"])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), 1)
        self.compare_with_file_contents(transformed[0].pformat(),
                                        expect_transformed_files[0])
