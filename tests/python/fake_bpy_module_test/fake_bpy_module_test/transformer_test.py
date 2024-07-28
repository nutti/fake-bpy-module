from pathlib import Path

from docutils import nodes  # noqa: TCH002
from docutils.core import publish_doctree
from fake_bpy_module import config
from fake_bpy_module.analyzer.analyzer import BaseAnalyzer
from fake_bpy_module.transformer.data_type_refiner import EntryPoint
from fake_bpy_module.transformer.transformer import Transformer

# pylint: disable=E0401
from fake_bpy_module.transformer.utils import (
    ModuleStructure,
    build_module_structure,
    get_base_name,
    get_module_name,
)

from . import common


class TransformerTestBase(common.FakeBpyModuleTestBase):

    def setUp(self) -> None:
        super().setUp()

        self.__setup_config()

    def __setup_config(self) -> None:
        config.set_target("blender")
        config.set_target_version("2.80")

    def compare_with_file_contents(self, actual: str, expect_file: str) -> None:
        with Path(expect_file).open("r", encoding="utf-8") as f:
            expect = f.read()
        self.assertEqual(actual, expect)


class BaseClassFixtureTest(TransformerTestBase):

    name = "BaseClassFixtureTest"
    module_name = __module__
    data_dir = Path(
        f"{Path(__file__).parent}/transformer_test_data/"
        "base_class_fixture_test").resolve()

    def test_basic(self) -> None:
        rst_files = ["basic.rst"]
        expect_files = ["basic.xml"]
        expect_transformed_files = ["basic_transformed.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer(["base_class_fixture"])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)


class ModuleLevelAttributeFixtureTest(TransformerTestBase):

    name = "ModuleLevelAttributeFixtureTest"
    module_name = __module__
    data_dir = Path(
        f"{Path(__file__).parent}/transformer_test_data/"
        "module_level_attribute_fixture_test").resolve()

    def test_basic(self) -> None:
        rst_files = ["basic.rst"]
        expect_files = ["basic.xml"]
        expect_transformed_files = ["basic_transformed.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer(["module_level_attribute_fixture"])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)


class ModuleNameFixtureTest(TransformerTestBase):

    name = "ModuleNameFixtureTest"
    module_name = __module__
    data_dir = Path(
        f"{Path(__file__).parent}/transformer_test_data/"
        "module_name_fixture_test").resolve()

    def test_no_module(self) -> None:
        rst_files = ["no_module.rst"]
        expect_files = ["no_module.xml"]
        expect_transformed_files = []
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer(["module_name_fixture"])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)

    def test_bge_no_module(self) -> None:
        rst_files = ["bge.types.NoModule.rst"]
        expect_files = ["bge.types.NoModule.xml"]
        expect_transformed_files = ["bge.types.NoModule_transformed.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
        config.set_target("upbge")
        config.set_target_version("0.2.5")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer(["module_name_fixture"])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)


class RstSpecificNodeCleanerTest(TransformerTestBase):

    name = "RstSpecificNodeCleanerTest"
    module_name = __module__
    data_dir = Path(
        f"{Path(__file__).parent}/transformer_test_data/"
        "rst_specific_node_cleaner_test").resolve()

    def test_basic(self) -> None:
        rst_files = ["basic.rst"]
        expect_files = ["basic.xml"]
        expect_transformed_files = ["basic_transformed.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer(["rst_specific_node_cleaner"])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)


class FormatValidatorTest(TransformerTestBase):

    name = "FormatValidatorTest"
    module_name = __module__

    def test_basic(self) -> None:
        document: nodes.document = publish_doctree(""".. module:: module_1

.. warning::

      Warning Contents
""")

        transformer = Transformer(["format_validator"])
        with self.assertRaises(TypeError):
            transformer.transform([document])


class BpyContextVariableConverterTest(TransformerTestBase):

    name = "BpyContextVariableConverterTest"
    module_name = __module__
    data_dir = Path(
        f"{Path(__file__).parent}/transformer_test_data/"
        "bpy_context_variable_converter_test").resolve()

    def test_basic(self) -> None:
        rst_files = [
            "basic_1.rst",
            "basic_2.rst",
            "basic_3.rst"
        ]
        expect_files = [
            "basic_1.xml",
            "basic_2.xml",
            "basic_3.xml"
        ]
        expect_transformed_files = [
            "basic_transformed_1.xml",
            "basic_transformed_2.xml"
        ]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer(["bpy_context_variable_converter"])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)


class BpyModuleTweakerTest(TransformerTestBase):

    name = "BpyModuleTweakerTest"
    module_name = __module__
    data_dir = Path(
        f"{Path(__file__).parent}/transformer_test_data/"
        "bpy_module_tweaker").resolve()

    def test_make_bpy_prop_functions_arguments_kwonlyargs(self) -> None:
        rst_files = ["make_bpy_prop_functions_arguments_kwonlyargs.rst"]
        expect_files = ["make_bpy_prop_functions_arguments_kwonlyargs.xml"]
        expect_transformed_files = [
            "make_bpy_prop_functions_arguments_kwonlyargs_transformed.xml"
        ]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer(["bpy_module_tweaker"])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)

    def test_add_bpy_app_handlers_functions_data_types(self) -> None:
        rst_files = ["add_bpy_app_handlers_functions_data_types.rst"]
        expect_files = ["add_bpy_app_handlers_functions_data_types.xml"]
        expect_transformed_files = [
            "add_bpy_app_handlers_functions_data_types_transformed.xml"
        ]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer(["bpy_module_tweaker"])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)

    def test_add_bpy_ops_override_parameters_transformed(self) -> None:
        rst_files = ["add_bpy_ops_override_parameters.rst"]
        expect_files = ["add_bpy_ops_override_parameters.xml"]
        expect_transformed_files = [
            "add_bpy_ops_override_parameters_transformed.xml"
        ]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer(["bpy_module_tweaker"])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)

    def test_rebase_bpy_types_class_base_class(self) -> None:
        rst_files = ["rebase_bpy_types_class_base_class.rst"]
        expect_files = ["rebase_bpy_types_class_base_class.xml"]
        expect_transformed_files = [
            "rebase_bpy_types_class_base_class_transformed.xml"
        ]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer(["bpy_module_tweaker"])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)


class CannonicalDataTypeRewriterTest(TransformerTestBase):

    name = "CannonicalDataTypeRewriterTest"
    module_name = __module__
    data_dir = Path(
        f"{Path(__file__).parent}/transformer_test_data/"
        "cannonical_data_type_rewriter_test").resolve()

    def test_basic(self) -> None:
        rst_files = ["basic.rst"]
        expect_files = ["basic.xml"]
        expect_transformed_files = ["basic_transformed.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
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

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer(["cannonical_data_type_rewriter"], {
            "cannonical_data_type_rewriter": {
                "package_structure": package_structure,
            }
        })
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)


class CodeDocumentRefinerTest(TransformerTestBase):

    name = "CodeDocumentRefinerTest"
    module_name = __module__
    data_dir = Path(
        f"{Path(__file__).parent}/transformer_test_data/"
        "code_document_refiner_test").resolve()

    def test_merge(self) -> None:
        rst_files = ["merge.rst"]
        expect_files = ["merge.xml"]
        expect_transformed_files = ["merge_transformed.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer([
            "rst_specific_node_cleaner",
            "code_document_refiner",
        ])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)

    def test_remove_trivial_nodes(self) -> None:
        rst_files = ["remove_trivial_nodes.rst"]
        expect_files = ["remove_trivial_nodes.xml"]
        expect_transformed_files = ["remove_trivial_nodes_transformed.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer([
            "rst_specific_node_cleaner",
            "code_document_refiner",
        ])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)

    def test_remove_empty_nodes(self) -> None:
        rst_files = ["remove_empty_nodes.rst"]
        expect_files = ["remove_empty_nodes.xml"]
        expect_transformed_files = ["remove_empty_nodes_transformed.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer([
            "rst_specific_node_cleaner",
            "code_document_refiner",
        ])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)


class DataTypeRefinerTest(TransformerTestBase):

    name = "DataTypeRefinerTest"
    module_name = __module__
    data_dir = Path(
        f"{Path(__file__).parent}/transformer_test_data/"
        "data_type_refiner_test").resolve()

    def compare_with_file_contents(self, actual: str, expect_file: str) -> None:
        with Path(expect_file).open("r", encoding="utf-8") as f:
            expect = f.read()
        self.assertEqual(actual, expect)

    def test_basic(self) -> None:
        rst_files = ["basic.rst"]
        expect_files = ["basic.xml"]
        expect_transformed_files = ["basic_transformed.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        package_structure = ModuleStructure()
        module_structure = ModuleStructure()
        module_structure.name = "refined_module_a"
        package_structure.add_child(module_structure)
        module_structure = ModuleStructure()
        module_structure.name = "refined_module_b"
        package_structure.add_child(module_structure)
        module_structure = ModuleStructure()
        module_structure.name = "refined_module_c"
        package_structure.add_child(module_structure)
        module_structure = ModuleStructure()
        module_structure.name = "refined_module_d"
        package_structure.add_child(module_structure)

        entry_points = []
        entry_point = EntryPoint("refined_module_a", "RefinedClassA", "class")
        entry_points.append(entry_point)
        entry_point = EntryPoint("refined_module_a", "RefinedClassB", "class")
        entry_points.append(entry_point)
        entry_point = EntryPoint("refined_module_b", "RefinedClassC", "class")
        entry_points.append(entry_point)
        entry_point = EntryPoint("refined_module_b", "RefinedClassD", "class")
        entry_points.append(entry_point)
        entry_point = EntryPoint("refined_module_a", "RefinedClassE", "class")
        entry_points.append(entry_point)
        entry_point = EntryPoint("refined_module_c", "RefinedClassF", "class")
        entry_points.append(entry_point)
        entry_point = EntryPoint("refined_module_d", "RefinedClassG", "class")
        entry_points.append(entry_point)

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer(["data_type_refiner"], {
            "data_type_refiner": {
                "package_structure": package_structure,
                "entry_points": entry_points,
            }
        })
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)

    def test_various_data_type(self) -> None:
        rst_files = ["various_data_type.rst"]
        expect_files = ["various_data_type.xml"]
        expect_transformed_files = ["various_data_type_transformed.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        rna_enum_file = Path(__file__).parents[4] / "gen_module-tmp/sphinx-in/bpy_types_enum_items/.rst"  # noqa: E501
        rna_enum_file.parent.mkdir(parents=True, exist_ok=True)
        rna_enum_file.write_text("""\
.. _rna_enum:


####################################

:ONE: One.

   One
:TWO: Two.

   Two""")

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        entry_points = []
        entry_point = EntryPoint("refined_module_a", "RefinedClassA", "class")
        entry_points.append(entry_point)
        entry_point = EntryPoint("module_1", "ClassA", "class")
        entry_points.append(entry_point)
        entry_point = EntryPoint("mathutils", "Vector", "class")
        entry_points.append(entry_point)
        entry_point = EntryPoint("mathutils", "Matrix", "class")
        entry_points.append(entry_point)
        entry_point = EntryPoint("bpy.types", "Struct", "class")
        entry_points.append(entry_point)
        entry_point = EntryPoint("bpy.types", "bpy_struct", "class")
        entry_points.append(entry_point)
        entry_point = EntryPoint("bpy.types", "bpy_prop_collection", "class")
        entry_points.append(entry_point)
        entry_point = EntryPoint("bpy.ops.test", "op", "class")
        entry_points.append(entry_point)
        entry_point = EntryPoint("bgl", "Buffer", "class")
        entry_points.append(entry_point)

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer(["data_type_refiner"], {
            "data_type_refiner": {
                "entry_points": entry_points,
            }
        })
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)

    def test_special_data_type(self) -> None:
        rst_files = ["special_data_type.rst"]
        expect_files = ["special_data_type.xml"]
        expect_transformed_files = ["special_data_type_transformed.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        entry_points = []
        entry_point = EntryPoint("module_1", "ClassA", "class")
        entry_points.append(entry_point)
        entry_point = EntryPoint("module_2", "ClassB", "class")
        entry_points.append(entry_point)

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer(["data_type_refiner"], {
            "data_type_refiner": {
                "entry_points": entry_points,
            }
        })
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)

    def test_option(self) -> None:
        rst_files = ["option_bpy.rst", "option_non_bpy.rst"]
        expect_files = ["option_bpy.xml", "option_non_bpy.xml"]
        expect_transformed_files = [
            "option_bpy_transformed.xml",
            "option_non_bpy_transformed.xml"
        ]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer(["data_type_refiner"], {})
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)

    def test_description_dependency(self) -> None:
        rst_files = ["description_dependency.rst"]
        expect_files = ["description_dependency.xml"]
        expect_transformed_files = ["description_dependency_transformed.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer(["data_type_refiner"], {})
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)


class DefaultValueFillerTest(TransformerTestBase):

    name = "DefaultValueFillerTest"
    module_name = __module__
    data_dir = Path(
        f"{Path(__file__).parent}/transformer_test_data/"
        "default_value_filler_test").resolve()

    def compare_with_file_contents(self, actual: str, expect_file: str) -> None:
        with Path(expect_file).open("r", encoding="utf-8") as f:
            expect = f.read()
        self.assertEqual(actual, expect)

    def test_basic(self) -> None:
        rst_files = ["basic.rst"]
        expect_files = ["basic.xml"]
        expect_transformed_files = ["basic_transformed.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer(["default_value_filler"], {})
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)


class DependencyBuilderTest(TransformerTestBase):

    name = "DependencyBuilderTest"
    module_name = __module__
    data_dir = Path(
        f"{Path(__file__).parent}/transformer_test_data/"
        "dependency_builder_test").resolve()

    def test_basic(self) -> None:
        rst_files = ["basic.rst"]
        expect_files = ["basic.xml"]
        expect_transformed_files = ["basic_transformed.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
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

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer(["dependency_builder"], {
            "dependency_builder": {
                "package_structure": package_structure,
            }
        })
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)


class DuplicationRemoverTest(TransformerTestBase):

    name = "DuplicationRemoverTest"
    module_name = __module__
    data_dir = Path(
        f"{Path(__file__).parent}/transformer_test_data/"
        "duplication_remover").resolve()

    def test_basic(self) -> None:
        rst_files = [
            "function_argument.rst", "class_attribute.rst",
            "class.rst", "function.rst", "data.rst"
        ]
        expect_files = [
            "function_argument.xml", "class_attribute.xml",
            "class.xml", "function.xml", "data.xml"
        ]
        expect_transformed_files = [
            "function_argument_transformed.xml",
            "class_attribute_transformed.xml",
            "class_transformed.xml", "function_transformed.xml",
            "data_transformed.xml"
        ]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer([
            "duplication_remover",
        ])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)


class FirstTitleRemoverTest(TransformerTestBase):

    name = "FirstTitleRemoverTest"
    module_name = __module__
    data_dir = Path(
        f"{Path(__file__).parent}/transformer_test_data/"
        "first_title_remover_test").resolve()

    def test_basic(self) -> None:
        rst_files = ["basic.rst"]
        expect_files = ["basic.xml"]
        expect_transformed_files = ["basic_transformed.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer([
            "first_title_remover",
        ])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)

    def test_multiple_titles(self) -> None:
        rst_files = ["multiple_titles.rst"]
        expect_files = ["multiple_titles.xml"]
        expect_transformed_files = ["multiple_titles_transformed.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer([
            "first_title_remover",
        ])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)


class ModApplierTest(TransformerTestBase):

    name = "ModApplierTest"
    module_name = __module__
    data_dir = Path(
        f"{Path(__file__).parent}/transformer_test_data/"
        "mod_applier_test").resolve()

    def test_new_data(self) -> None:
        rst_files = ["base.rst"]
        mod_files = ["new_data.mod.rst"]
        expect_mod_files = ["new_data.mod.xml"]
        expect_files = ["new_data.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        mod_files = [f"{self.data_dir}/input/{f}" for f in mod_files]
        expect_mod_files = [f"{self.data_dir}/expect/{f}"
                            for f in expect_mod_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        transformer = Transformer(["mod_applier"],
                                  {"mod_applier": {"mod_files": mod_files}})
        transformed = transformer.transform(documents)
        self.assertEqual(len(transformer.get_transformers()), 1)
        mod_documents = transformer.get_transformers()[0].get_mod_documents()

        self.assertEqual(len(mod_documents), len(expect_mod_files))
        for mod_doc, expect_file in zip(mod_documents, expect_mod_files,
                                        strict=True):
            self.compare_with_file_contents(mod_doc.pformat(), expect_file)

        self.assertEqual(len(transformed), len(rst_files))
        for doc, expect_file in zip(transformed, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect_file)

    def test_new_function(self) -> None:
        rst_files = ["base.rst"]
        mod_files = ["new_function.mod.rst"]
        expect_mod_files = ["new_function.mod.xml"]
        expect_files = ["new_function.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        mod_files = [f"{self.data_dir}/input/{f}" for f in mod_files]
        expect_mod_files = [f"{self.data_dir}/expect/{f}"
                            for f in expect_mod_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        transformer = Transformer(["mod_applier"],
                                  {"mod_applier": {"mod_files": mod_files}})
        transformed = transformer.transform(documents)
        self.assertEqual(len(transformer.get_transformers()), 1)
        mod_documents = transformer.get_transformers()[0].get_mod_documents()

        self.assertEqual(len(mod_documents), len(expect_mod_files))
        for mod_doc, expect_file in zip(mod_documents, expect_mod_files,
                                        strict=True):
            self.compare_with_file_contents(mod_doc.pformat(), expect_file)

        self.assertEqual(len(transformed), len(rst_files))
        for doc, expect_file in zip(transformed, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect_file)

    def test_new_class(self) -> None:
        rst_files = ["base.rst"]
        mod_files = ["new_class.mod.rst"]
        expect_mod_files = ["new_class.mod.xml"]
        expect_files = ["new_class.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        mod_files = [f"{self.data_dir}/input/{f}" for f in mod_files]
        expect_mod_files = [f"{self.data_dir}/expect/{f}"
                            for f in expect_mod_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        transformer = Transformer(["mod_applier"],
                                  {"mod_applier": {"mod_files": mod_files}})
        transformed = transformer.transform(documents)
        self.assertEqual(len(transformer.get_transformers()), 1)
        mod_documents = transformer.get_transformers()[0].get_mod_documents()

        self.assertEqual(len(mod_documents), len(expect_mod_files))
        for mod_doc, expect_file in zip(mod_documents, expect_mod_files,
                                        strict=True):
            self.compare_with_file_contents(mod_doc.pformat(), expect_file)

        self.assertEqual(len(transformed), len(rst_files))
        for doc, expect_file in zip(transformed, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect_file)

    def test_append_function(self) -> None:
        rst_files = ["base.rst"]
        mod_files = ["append_function.mod.rst"]
        expect_mod_files = ["append_function.mod.xml"]
        expect_files = ["append_function.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        mod_files = [f"{self.data_dir}/input/{f}" for f in mod_files]
        expect_mod_files = [f"{self.data_dir}/expect/{f}"
                            for f in expect_mod_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        transformer = Transformer(["mod_applier"],
                                  {"mod_applier": {"mod_files": mod_files}})
        transformed = transformer.transform(documents)
        self.assertEqual(len(transformer.get_transformers()), 1)
        mod_documents = transformer.get_transformers()[0].get_mod_documents()

        self.assertEqual(len(mod_documents), len(expect_mod_files))
        for mod_doc, expect_file in zip(mod_documents, expect_mod_files,
                                        strict=True):
            self.compare_with_file_contents(mod_doc.pformat(), expect_file)

        self.assertEqual(len(transformed), len(rst_files))
        for doc, expect_file in zip(transformed, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect_file)

    def test_append_class(self) -> None:
        rst_files = ["base.rst"]
        mod_files = ["append_class.mod.rst"]
        expect_mod_files = ["append_class.mod.xml"]
        expect_files = ["append_class.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        mod_files = [f"{self.data_dir}/input/{f}" for f in mod_files]
        expect_mod_files = [f"{self.data_dir}/expect/{f}"
                            for f in expect_mod_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        transformer = Transformer(["mod_applier"],
                                  {"mod_applier": {"mod_files": mod_files}})
        transformed = transformer.transform(documents)
        self.assertEqual(len(transformer.get_transformers()), 1)
        mod_documents = transformer.get_transformers()[0].get_mod_documents()

        self.assertEqual(len(mod_documents), len(expect_mod_files))
        for mod_doc, expect_file in zip(mod_documents, expect_mod_files,
                                        strict=True):
            self.compare_with_file_contents(mod_doc.pformat(), expect_file)

        self.assertEqual(len(transformed), len(rst_files))
        for doc, expect_file in zip(transformed, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect_file)

    def test_update_data(self) -> None:
        rst_files = ["base.rst"]
        mod_files = ["update_data.mod.rst"]
        expect_mod_files = ["update_data.mod.xml"]
        expect_files = ["update_data.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        mod_files = [f"{self.data_dir}/input/{f}" for f in mod_files]
        expect_mod_files = [f"{self.data_dir}/expect/{f}"
                            for f in expect_mod_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        transformer = Transformer(["mod_applier"],
                                  {"mod_applier": {"mod_files": mod_files}})
        transformed = transformer.transform(documents)
        self.assertEqual(len(transformer.get_transformers()), 1)
        mod_documents = transformer.get_transformers()[0].get_mod_documents()

        self.assertEqual(len(mod_documents), len(expect_mod_files))
        for mod_doc, expect_file in zip(mod_documents, expect_mod_files,
                                        strict=True):
            self.compare_with_file_contents(mod_doc.pformat(), expect_file)

        self.assertEqual(len(transformed), len(rst_files))
        for doc, expect_file in zip(transformed, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect_file)

    def test_update_function(self) -> None:
        rst_files = ["base.rst"]
        mod_files = ["update_function.mod.rst"]
        expect_mod_files = ["update_function.mod.xml"]
        expect_files = ["update_function.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        mod_files = [f"{self.data_dir}/input/{f}" for f in mod_files]
        expect_mod_files = [f"{self.data_dir}/expect/{f}"
                            for f in expect_mod_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        transformer = Transformer(["mod_applier"],
                                  {"mod_applier": {"mod_files": mod_files}})
        transformed = transformer.transform(documents)
        self.assertEqual(len(transformer.get_transformers()), 1)
        mod_documents = transformer.get_transformers()[0].get_mod_documents()

        self.assertEqual(len(mod_documents), len(expect_mod_files))
        for mod_doc, expect_file in zip(mod_documents, expect_mod_files,
                                        strict=True):
            self.compare_with_file_contents(mod_doc.pformat(), expect_file)

        self.assertEqual(len(transformed), len(rst_files))
        for doc, expect_file in zip(transformed, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect_file)

    def test_update_class(self) -> None:
        rst_files = ["base.rst"]
        mod_files = ["update_class.mod.rst"]
        expect_mod_files = ["update_class.mod.xml"]
        expect_files = ["update_class.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        mod_files = [f"{self.data_dir}/input/{f}" for f in mod_files]
        expect_mod_files = [f"{self.data_dir}/expect/{f}"
                            for f in expect_mod_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        transformer = Transformer(["mod_applier"],
                                  {"mod_applier": {"mod_files": mod_files}})
        transformed = transformer.transform(documents)
        self.assertEqual(len(transformer.get_transformers()), 1)
        mod_documents = transformer.get_transformers()[0].get_mod_documents()

        self.assertEqual(len(mod_documents), len(expect_mod_files))
        for mod_doc, expect_file in zip(mod_documents, expect_mod_files,
                                        strict=True):
            self.compare_with_file_contents(mod_doc.pformat(), expect_file)

        self.assertEqual(len(transformed), len(rst_files))
        for doc, expect_file in zip(transformed, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect_file)

    def test_mod_option(self) -> None:
        mod_files = ["mod_option.mod.rst"]
        expect_mod_files = ["mod_option.mod.xml"]
        mod_files = [f"{self.data_dir}/input/{f}" for f in mod_files]
        expect_mod_files = [f"{self.data_dir}/expect/{f}"
                            for f in expect_mod_files]

        transformer = Transformer(["mod_applier"],
                                  {"mod_applier": {"mod_files": mod_files}})
        _ = transformer.transform([])
        self.assertEqual(len(transformer.get_transformers()), 1)
        mod_documents = transformer.get_transformers()[0].get_mod_documents()

        self.assertEqual(len(mod_documents), len(expect_mod_files))
        for mod_doc, expect_file in zip(mod_documents, expect_mod_files,
                                        strict=True):
            self.compare_with_file_contents(mod_doc.pformat(), expect_file)


class SameModuleMergerTest(TransformerTestBase):

    name = "SameModuleMergerTest"
    module_name = __module__
    data_dir = Path(
        f"{Path(__file__).parent}/transformer_test_data/"
        "same_module_merger_test").resolve()

    def test_basic(self) -> None:
        rst_files = [
            "basic_module_1_a.rst",
            "basic_module_1_b.rst",
            "basic_module_2.rst",
        ]
        expect_files = [
            "basic_module_1_a.xml",
            "basic_module_1_b.xml",
            "basic_module_2.xml",
        ]
        expect_transformed_files = [
            "basic_module_1_transformed.xml",
            "basic_module_2_transformed.xml",
        ]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer(["same_module_merger"])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)


class SelfRewriterTest(TransformerTestBase):

    name = "SelfRewriterTest"
    module_name = __module__
    data_dir = Path(
        f"{Path(__file__).parent}/transformer_test_data/"
        "self_rewriter_test").resolve()

    def test_basic(self) -> None:
        rst_files = ["basic.rst"]
        expect_files = ["basic.xml"]
        expect_transformed_files = ["basic_transformed.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer(["self_rewriter"])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)


class TargetFileCombinerTest(TransformerTestBase):

    name = "TargetFileCombinerTest"
    module_name = __module__
    data_dir = Path(
        f"{Path(__file__).parent}/transformer_test_data/"
        "target_file_combiner_test").resolve()

    def test_combine(self) -> None:
        rst_files = [
            "combine_module_1_a.rst",
            "combine_module_1_b.rst",
            "combine_module_2.rst",
        ]
        expect_files = [
            "combine_module_1_a.xml",
            "combine_module_1_b.xml",
            "combine_module_2.xml",
        ]
        expect_transformed_files = [
            "combine_module_1_transformed.xml",
            "combine_module_2_transformed.xml",
        ]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer(["target_file_combiner"])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)

    def test_child_module(self) -> None:
        rst_files = [
            "child_module_module_1.rst",
            "child_module_module_1_submodule_1.rst",
        ]
        expect_files = [
            "child_module_module_1.xml",
            "child_module_module_1_submodule_1.xml",
        ]
        expect_transformed_files = [
            "child_module_module_1_transformed.xml",
            "child_module_module_1_submodule_1_transformed.xml",
        ]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}"
                                    for f in expect_transformed_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

        transformer = Transformer(["target_file_combiner"])
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), len(expect_transformed_files))
        for trans, expect in zip(transformed, expect_transformed_files,
                                 strict=True):
            self.compare_with_file_contents(trans.pformat(), expect)


class ModuleStructureTest(common.FakeBpyModuleTestBase):

    name = "ModuleStructureTest"
    module_name = __module__

    def test_root_only(self) -> None:
        root = ModuleStructure()

        with self.assertRaises(RuntimeError):
            _ = root.name

        expect_dict = {
            "name": None,
            "children": [],
        }

        self.assertDictEqual(root.to_dict(), expect_dict)

    def test_one_child(self) -> None:
        root = ModuleStructure()

        module_1 = ModuleStructure()
        module_1.name = "module_1"
        root.add_child(module_1)

        expect_dict = {
            "name": None,
            "module_1": [
                {
                    "name": "module_1",
                    "module_1": [],
                }
            ]
        }

        self.assertEqual(module_1.name, "module_1")
        self.assertEqual(root.children(), [module_1])
        self.assertDictEqual(root.to_dict(), expect_dict)

    def test_multiple_children(self) -> None:
        root = ModuleStructure()

        module_1 = ModuleStructure()
        module_1.name = "module_1"
        root.add_child(module_1)

        module_2 = ModuleStructure()
        module_2.name = "module_2"
        root.add_child(module_2)

        submodule_1 = ModuleStructure()
        submodule_1.name = "submodule_1"
        module_2.add_child(submodule_1)

        expect_dict = {
            "name": None,
            "children": [
                {
                    "name": "module_1",
                    "children": [],
                },
                {
                    "name": "module_2",
                    "children": [
                        {
                            "name": "submodule_1",
                            "children": [],
                        }
                    ],
                }
            ]
        }

        self.assertEqual(module_1.name, "module_1")
        self.assertEqual(module_2.name, "module_2")
        self.assertEqual(submodule_1.name, "submodule_1")
        self.assertEqual(root.children(), [module_1, module_2])
        self.assertEqual(module_1.children(), [])
        self.assertEqual(module_2.children(), [submodule_1])
        self.assertDictEqual(root.to_dict(), expect_dict)


class UtilsTest(TransformerTestBase):

    name = "UtilsTest"
    module_name = __module__

    def test_build_module_structure(self) -> None:
        documents: list[nodes.document] = []
        documents.append(publish_doctree(".. module:: module_1"))
        documents.append(publish_doctree(".. module:: module_1.submodule_1"))
        documents.append(publish_doctree(".. module:: module_1.submodule_2"))
        documents.append(publish_doctree(
            ".. module:: module_1.submodule_2.subsubmodule_1"))

        expect_dict = {
            "name": None,
            "children": [
                {
                    "name": "module_1",
                    "children": [
                        {
                            "name": "submodule_1",
                            "children": [],
                        },
                        {
                            "name": "submodule_2",
                            "children": [
                                {
                                    "name": "subsubmodule_1",
                                    "children": [],
                                }
                            ],
                        }
                    ]
                }
            ]
        }

        module_structure: ModuleStructure = build_module_structure(documents)
        self.assertEqual(len(module_structure.children()), 1)
        root = module_structure.children()[0]
        self.assertEqual(root.name, "module_1")
        self.assertEqual(len(root.children()), 2)
        children = root.children()
        self.assertEqual(children[0].name, "submodule_1")
        self.assertEqual(children[1].name, "submodule_2")
        self.assertEqual(len(children[0].children()), 0)
        self.assertEqual(len(children[1].children()), 1)
        grand_children = children[1].children()
        self.assertEqual(grand_children[0].name, "subsubmodule_1")
        self.assertDictEqual(module_structure.to_dict(), expect_dict)

    def test_get_base_name(self) -> None:
        self.assertEqual(get_base_name("module_1.function_1"), "function_1")
        self.assertEqual(get_base_name("module_1.submodule_1.DATA_1"), "DATA_1")

    def test_get_module_name(self) -> None:
        package = ModuleStructure()
        module = ModuleStructure()
        module.name = "module_1"
        submodule = ModuleStructure()
        submodule.name = "submodule_1"
        module.add_child(submodule)
        package.add_child(module)

        self.assertIsNone(get_module_name(None, package))
        self.assertEqual(
            get_module_name("module_1.submodule_1.ClassA", package),
            "module_1.submodule_1")
        self.assertIsNone(get_module_name("module_1.submodule_2.ClassA",
                                          package))
        self.assertEqual(get_module_name("module_1.ClassB", package),
                         "module_1")
