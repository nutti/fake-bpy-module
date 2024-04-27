import shutil
import os
from docutils import nodes
from docutils.core import publish_doctree

from fake_bpy_module.analyzer.analyzer import BaseAnalyzer      # pylint: disable=E0401
from fake_bpy_module.transformer.transformer import Transformer     # pylint: disable=E0401
from fake_bpy_module.transformer.utils import ModuleStructure       # pylint: disable=E0401
from fake_bpy_module.generator.writers import (     # pylint: disable=E0401
    sorted_entry_point_nodes,
    PyCodeWriterBase,
    PyCodeWriter,
    PyInterfaceWriter,
)
from fake_bpy_module.generator.code_writer import (     # pylint: disable=E0401
    CodeWriterIndent,
    CodeWriter,
)
from fake_bpy_module.utils import append_child      # pylint: disable=E0401
from . import common


class CodeWriterIndentTest(common.FakeBpyModuleTestBase):

    name = "CodeWriterIndentTest"
    module_name = __module__

    def setUp(self):
        super().setUp()

        CodeWriterIndent.reset_indent()

    def test_single(self):
        with CodeWriterIndent() as _:
            self.assertEqual(CodeWriterIndent.current_indent(), 0)

    def test_multiple(self):
        with CodeWriterIndent():
            self.assertEqual(CodeWriterIndent.current_indent(), 0)

            with CodeWriterIndent(1):
                self.assertEqual(CodeWriterIndent.current_indent(), 1)

            self.assertEqual(CodeWriterIndent.current_indent(), 0)

            with CodeWriterIndent(2) as _:
                self.assertEqual(CodeWriterIndent.current_indent(), 2)

    def test_add_current_level(self):
        with CodeWriterIndent(1):
            self.assertEqual(CodeWriterIndent.current_indent(), 1)

            with CodeWriterIndent(2, True):
                self.assertEqual(CodeWriterIndent.current_indent(), 3)

            self.assertEqual(CodeWriterIndent.current_indent(), 1)

        with CodeWriterIndent(1, True):
            self.assertEqual(CodeWriterIndent.current_indent(), 1)

    def test_call_classmethod(self):
        CodeWriterIndent.add_indent(0)

        self.assertEqual(CodeWriterIndent.current_indent(), 0)

        CodeWriterIndent.add_indent(1)
        self.assertEqual(CodeWriterIndent.current_indent(), 1)
        CodeWriterIndent.remove_indent()

        self.assertEqual(CodeWriterIndent.current_indent(), 0)

        CodeWriterIndent.add_indent(2)
        self.assertEqual(CodeWriterIndent.current_indent(), 2)
        CodeWriterIndent.remove_indent()

        CodeWriterIndent.remove_indent()


class CodeWriterTest(common.FakeBpyModuleTestBase):

    name = "CodeWriterTest"
    module_name = __module__
    data_dir = os.path.abspath(
        f"{os.path.dirname(__file__)}/generator_test_data/code_writer_test")

    def setUp(self):
        super().setUp()

        self.output_dir = "fake_bpy_module_test_tmp"
        self.output_file_path = f"{self.output_dir}/code_writer_test_output"
        os.makedirs(self.output_dir, exist_ok=False)

    def tearDown(self):
        super().tearDown()

        shutil.rmtree(self.output_dir)

    def test_normal(self):
        with open(self.output_file_path, "w", newline="\n",
                  encoding="utf-8") as f:
            writer = CodeWriter()

            writer.addln("import module_1")
            writer.new_line(2)
            writer.addln("i: int = 10")

            writer.format(style_config="ruff", file_format="py")
            writer.write(f)

        expect_file_path = f"{self.data_dir}/code_writer_test_normal.py"
        actual_file_path = self.output_file_path
        with open(actual_file_path, "r", encoding="utf-8") as f:
            expect_contents = f.read()
        with open(expect_file_path, "r", encoding="utf-8") as f:
            actual_contents = f.read()
        self.log(f"============= Expect: {expect_file_path} =============")
        self.log(expect_contents)
        self.log(f"============= Actual: {actual_file_path} =============")
        self.log(actual_contents)
        self.assertEqual(expect_contents, actual_contents)

    def test_with_code_indent(self):
        with open(self.output_file_path, "w", newline="\n",
                  encoding="utf-8") as f:
            writer = CodeWriter()

            writer.addln("import module_1")
            writer.new_line(2)
            writer.addln("def add(x1, x2):")
            with CodeWriterIndent(1):
                writer.addln("pass")
            writer.new_line(2)
            writer.addln("f: float = 0.5")

            writer.format(style_config="ruff", file_format="py")
            writer.write(f)

        expect_file_path = \
            f"{self.data_dir}/code_writer_test_with_code_indent.py"
        actual_file_path = self.output_file_path
        with open(actual_file_path, "r", encoding="utf-8") as f:
            expect_contents = f.read()
        with open(expect_file_path, "r", encoding="utf-8") as f:
            actual_contents = f.read()
        self.log(f"============= Expect: {expect_file_path} =============")
        self.log(expect_contents)
        self.log(f"============= Actual: {actual_file_path} =============")
        self.log(actual_contents)
        self.assertEqual(expect_contents, actual_contents)

    def test_with_reset(self):
        with open(self.output_file_path, "w", newline="\n",
                  encoding="utf-8") as f:
            writer = CodeWriter()

            writer.addln("import fake")
            writer.reset()

            writer.addln("import module_1")

            writer.new_line(2)
            writer.addln("b: bool = False")

            writer.format(style_config="ruff", file_format="py")
            writer.write(f)

        expect_file_path = f"{self.data_dir}/code_writer_test_with_reset.py"
        actual_file_path = self.output_file_path
        with open(actual_file_path, "r", encoding="utf-8") as f:
            expect_contents = f.read()
        with open(expect_file_path, "r", encoding="utf-8") as f:
            actual_contents = f.read()
        self.log(f"============= Expect: {expect_file_path} =============")
        self.log(expect_contents)
        self.log(f"============= Actual: {actual_file_path} =============")
        self.log(actual_contents)
        self.assertEqual(expect_contents, actual_contents)

    def test_get_data_as_string(self):
        writer = CodeWriter()

        writer.addln("import module_1")
        writer.new_line(2)
        writer.addln("i: int = 10")

        data_str = writer.get_data_as_string()

        expect_str = """import module_1


i: int = 10
"""
        self.assertEqual(expect_str, data_str)


class SortedEntryPointNodesTest(common.FakeBpyModuleTestBase):

    name = "SortedEntryPointNodesTest"
    module_name = __module__
    data_dir = os.path.abspath(
        f"{os.path.dirname(__file__)}/generator_test_data/sorted_entry_point_nodes_test")

    def compare_with_file_contents(self, actual: str, expect_file: str):
        with open(expect_file, "r", encoding="utf-8") as f:
            expect = f.read()
        self.assertEqual(actual, expect)

    def test_basic(self):
        rst_files = ["basic.rst"]
        expect_analyzed_files = ["basic.xml"]
        expect_sorted_files = ["basic_sorted.xml"]
        rst_files = [f"{self.data_dir}/input/basic/{f}" for f in rst_files]
        expect_analyzed_files = [f"{self.data_dir}/expect/basic/{f}" for f in expect_analyzed_files]
        expect_sorted_files = [f"{self.data_dir}/expect/basic/{f}" for f in expect_sorted_files]

        # Analyze
        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_analyzed_files))
        for doc, expect in zip(documents, expect_analyzed_files):
            self.compare_with_file_contents(doc.pformat(), expect)

        # Sort
        for doc, expect in zip(documents, expect_sorted_files):
            sorted_nodes = sorted_entry_point_nodes(doc)
            sorted_document: nodes.document = publish_doctree("")
            for node in sorted_nodes:
                append_child(sorted_document, node)

            self.compare_with_file_contents(sorted_document.pformat(), expect)

    def test_high_priority_class(self):
        rst_files = ["high_priority_class.rst"]
        expect_analyzed_files = ["high_priority_class.xml"]
        expect_sorted_files = ["high_priority_class_sorted.xml"]
        rst_files = [f"{self.data_dir}/input/high_priority_class/{f}" for f in rst_files]
        expect_analyzed_files = [f"{self.data_dir}/expect/high_priority_class/{f}"
                                 for f in expect_analyzed_files]
        expect_sorted_files = [f"{self.data_dir}/expect/high_priority_class/{f}"
                               for f in expect_sorted_files]

        # Analyze
        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_analyzed_files))
        for doc, expect in zip(documents, expect_analyzed_files):
            self.compare_with_file_contents(doc.pformat(), expect)

        # Sort
        for doc, expect in zip(documents, expect_sorted_files):
            sorted_nodes = sorted_entry_point_nodes(doc)
            sorted_document: nodes.document = publish_doctree("")
            for node in sorted_nodes:
                append_child(sorted_document, node)

            self.compare_with_file_contents(sorted_document.pformat(), expect)

    def test_base_class_dependency(self):
        rst_files = ["base_class_dependency.rst"]
        expect_analyzed_files = ["base_class_dependency.xml"]
        expect_sorted_files = ["base_class_dependency_sorted.xml"]
        rst_files = [f"{self.data_dir}/input/base_class_dependency/{f}" for f in rst_files]
        expect_analyzed_files = [f"{self.data_dir}/expect/base_class_dependency/{f}"
                                 for f in expect_analyzed_files]
        expect_sorted_files = [f"{self.data_dir}/expect/base_class_dependency/{f}"
                               for f in expect_sorted_files]

        # Analyze
        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_analyzed_files))
        for doc, expect in zip(documents, expect_analyzed_files):
            self.compare_with_file_contents(doc.pformat(), expect)

        # Sort
        for doc, expect in zip(documents, expect_sorted_files):
            sorted_nodes = sorted_entry_point_nodes(doc)
            sorted_document: nodes.document = publish_doctree("")
            for node in sorted_nodes:
                append_child(sorted_document, node)

            self.compare_with_file_contents(sorted_document.pformat(), expect)


class PyCodeWriterTestBase(common.FakeBpyModuleTestBase):

    name = "PyCodeWriterTest"
    module_name = __module__
    data_dir = os.path.abspath(
        f"{os.path.dirname(__file__)}/generator_test_data/py_code_writer_test")
    writer_class: type[PyCodeWriterBase] = PyCodeWriterBase
    file_extension: str = ""
    output_file: str = "py_code_writer_test_output"

    def setUp(self):
        super().setUp()

        self.output_dir = "fake_bpy_module_test_tmp"
        self.output_file_path = f"{self.output_dir}/{self.output_file}"
        os.makedirs(self.output_dir, exist_ok=False)

    def tearDown(self):
        super().tearDown()

        shutil.rmtree(self.output_dir)

    def compare_with_file_contents(self, actual: str, expect_file: str):
        with open(expect_file, "r", encoding="utf-8") as f:
            expect = f.read()
        self.assertEqual(actual, expect)

    def test_class(self):
        rst_files = ["class.rst"]
        expect_analyzed_files = ["class.xml"]
        expect_generated_files = [f"class.{self.file_extension}"]
        rst_files = [f"{self.data_dir}/input/class/{f}" for f in rst_files]
        expect_analyzed_files = [f"{self.data_dir}/expect/class/{f}" for f in expect_analyzed_files]
        expect_generated_files = [f"{self.data_dir}/expect/class/{f}"
                                  for f in expect_generated_files]

        # Analyze
        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_analyzed_files))
        for doc, expect in zip(documents, expect_analyzed_files):
            self.compare_with_file_contents(doc.pformat(), expect)

        # Generate
        writer = self.writer_class()
        for doc, expect_file_path in zip(documents, expect_generated_files):
            writer.write(self.output_file_path, doc)

            actual_file_path = f"{self.output_file_path}.{writer.file_format}"
            with open(actual_file_path, "r", encoding="utf-8") as f:
                expect_contents = f.read()
            with open(expect_file_path, "r", encoding="utf-8") as f:
                actual_contents = f.read()
            self.log(f"============= Expect: {expect_file_path} =============")
            self.log(expect_contents)
            self.log(f"============= Actual: {actual_file_path} =============")
            self.log(actual_contents)
            self.assertEqual(expect_contents, actual_contents)

    def test_function(self):
        rst_files = ["function.rst"]
        expect_analyzed_files = ["function.xml"]
        expect_generated_files = [f"function.{self.file_extension}"]
        rst_files = [f"{self.data_dir}/input/function/{f}" for f in rst_files]
        expect_analyzed_files = [f"{self.data_dir}/expect/function/{f}"
                                 for f in expect_analyzed_files]
        expect_generated_files = [f"{self.data_dir}/expect/function/{f}"
                                  for f in expect_generated_files]

        # Analyze
        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_analyzed_files))
        for doc, expect in zip(documents, expect_analyzed_files):
            self.compare_with_file_contents(doc.pformat(), expect)

        # Generate
        writer = self.writer_class()
        for doc, expect_file_path in zip(documents, expect_generated_files):
            writer.write(self.output_file_path, doc)

            actual_file_path = f"{self.output_file_path}.{writer.file_format}"
            with open(actual_file_path, "r", encoding="utf-8") as f:
                expect_contents = f.read()
            with open(expect_file_path, "r", encoding="utf-8") as f:
                actual_contents = f.read()
            self.log(f"============= Expect: {expect_file_path} =============")
            self.log(expect_contents)
            self.log(f"============= Actual: {actual_file_path} =============")
            self.log(actual_contents)
            self.assertEqual(expect_contents, actual_contents)

    def test_data(self):
        rst_files = ["data.rst"]
        expect_analyzed_files = ["data.xml"]
        expect_generated_files = [f"data.{self.file_extension}"]
        rst_files = [f"{self.data_dir}/input/data/{f}" for f in rst_files]
        expect_analyzed_files = [f"{self.data_dir}/expect/data/{f}" for f in expect_analyzed_files]
        expect_generated_files = [f"{self.data_dir}/expect/data/{f}"
                                  for f in expect_generated_files]

        # Analyze
        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_analyzed_files))
        for doc, expect in zip(documents, expect_analyzed_files):
            self.compare_with_file_contents(doc.pformat(), expect)

        # Generate
        writer = self.writer_class()
        for doc, expect_file_path in zip(documents, expect_generated_files):
            writer.write(self.output_file_path, doc)

            actual_file_path = f"{self.output_file_path}.{writer.file_format}"
            with open(actual_file_path, "r", encoding="utf-8") as f:
                expect_contents = f.read()
            with open(expect_file_path, "r", encoding="utf-8") as f:
                actual_contents = f.read()
            self.log(f"============= Expect: {expect_file_path} =============")
            self.log(expect_contents)
            self.log(f"============= Actual: {actual_file_path} =============")
            self.log(actual_contents)
            self.assertEqual(expect_contents, actual_contents)

    def test_dependencies(self):
        rst_files = ["dependencies.rst"]
        expect_analyzed_files = ["dependencies.xml"]
        expect_transformed_files = ["dependencies_transformed.xml"]
        expect_generated_files = [f"dependencies.{self.file_extension}"]
        rst_files = [f"{self.data_dir}/input/dependencies/{f}" for f in rst_files]
        expect_analyzed_files = [f"{self.data_dir}/expect/dependencies/{f}"
                                 for f in expect_analyzed_files]
        expect_transformed_files = [f"{self.data_dir}/expect/dependencies/{f}"
                                    for f in expect_transformed_files]
        expect_generated_files = [f"{self.data_dir}/expect/dependencies/{f}"
                                  for f in expect_generated_files]

        # Analyze
        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_analyzed_files))
        for doc, expect in zip(documents, expect_analyzed_files):
            self.compare_with_file_contents(doc.pformat(), expect)

        # Transform
        package_structure = ModuleStructure()
        module_1_structure = ModuleStructure()
        module_1_structure.name = "module_1"
        package_structure.add_child(module_1_structure)
        module_2_structure = ModuleStructure()
        module_2_structure.name = "module_2"
        package_structure.add_child(module_2_structure)

        transformer = Transformer([
            "dependency_builder",
        ], {
            "dependency_builder": {
                "package_structure": package_structure
            }
        })
        documents = transformer.transform(documents)

        self.assertEqual(len(documents), len(expect_transformed_files))
        for doc, expect in zip(documents, expect_transformed_files):
            self.compare_with_file_contents(doc.pformat(), expect)

        # Generate
        writer = self.writer_class()
        for doc, expect_file_path in zip(documents, expect_generated_files):
            writer.write(self.output_file_path, doc)

            actual_file_path = f"{self.output_file_path}.{writer.file_format}"
            with open(actual_file_path, "r", encoding="utf-8") as f:
                expect_contents = f.read()
            with open(expect_file_path, "r", encoding="utf-8") as f:
                actual_contents = f.read()
            self.log(f"============= Expect: {expect_file_path} =============")
            self.log(expect_contents)
            self.log(f"============= Actual: {actual_file_path} =============")
            self.log(actual_contents)
            self.assertEqual(expect_contents, actual_contents)

    def test_children(self):
        rst_files = ["children.rst"]
        expect_analyzed_files = ["children.xml"]
        expect_transformed_files = [
            "module_1_transformed.xml",
            "module_1.submodule_1_transformed.xml"
        ]
        expect_generated_files = [
            f"module_1.{self.file_extension}",
            f"module_1.submodule_1.{self.file_extension}"
        ]
        rst_files = [f"{self.data_dir}/input/children/{f}" for f in rst_files]
        expect_analyzed_files = [f"{self.data_dir}/expect/children/{f}"
                                 for f in expect_analyzed_files]
        expect_transformed_files = [f"{self.data_dir}/expect/children/{f}"
                                    for f in expect_transformed_files]
        expect_generated_files = [f"{self.data_dir}/expect/children/{f}"
                                  for f in expect_generated_files]

        # Analyze
        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_analyzed_files))
        for doc, expect in zip(documents, expect_analyzed_files):
            self.compare_with_file_contents(doc.pformat(), expect)

        # Transform
        package_structure = ModuleStructure()
        module_1_structure = ModuleStructure()
        module_1_structure.name = "module_1"
        package_structure.add_child(module_1_structure)
        submodule_1_structure = ModuleStructure()
        submodule_1_structure.name = "submodule_1"
        module_1_structure.add_child(submodule_1_structure)

        transformer = Transformer([
            "target_file_combiner",
        ], {
            "target_file_combiner": {
                "package_structure": package_structure
            }
        })
        documents = transformer.transform(documents)

        self.assertEqual(len(documents), len(expect_transformed_files))
        for doc, expect in zip(documents, expect_transformed_files):
            self.compare_with_file_contents(doc.pformat(), expect)

        # Generate
        writer = self.writer_class()
        for doc, expect_file_path in zip(documents, expect_generated_files):
            writer.write(self.output_file_path, doc)

            actual_file_path = f"{self.output_file_path}.{writer.file_format}"
            with open(actual_file_path, "r", encoding="utf-8") as f:
                expect_contents = f.read()
            with open(expect_file_path, "r", encoding="utf-8") as f:
                actual_contents = f.read()
            self.log(f"============= Expect: {expect_file_path} =============")
            self.log(expect_contents)
            self.log(f"============= Actual: {actual_file_path} =============")
            self.log(actual_contents)
            self.assertEqual(expect_contents, actual_contents)

    def test_deprecated(self):
        rst_files = ["deprecated.rst"]
        expect_analyzed_files = ["deprecated.xml"]
        expect_generated_files = [f"deprecated.{self.file_extension}"]
        rst_files = [f"{self.data_dir}/input/deprecated/{f}" for f in rst_files]
        expect_analyzed_files = [f"{self.data_dir}/expect/deprecated/{f}"
                                 for f in expect_analyzed_files]
        expect_generated_files = [f"{self.data_dir}/expect/deprecated/{f}"
                                  for f in expect_generated_files]

        # Analyze
        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_analyzed_files))
        for doc, expect in zip(documents, expect_analyzed_files):
            self.compare_with_file_contents(doc.pformat(), expect)

        # Generate
        writer = self.writer_class()
        for doc, expect_file_path in zip(documents, expect_generated_files):
            writer.write(self.output_file_path, doc)

            actual_file_path = f"{self.output_file_path}.{writer.file_format}"
            with open(actual_file_path, "r", encoding="utf-8") as f:
                expect_contents = f.read()
            with open(expect_file_path, "r", encoding="utf-8") as f:
                actual_contents = f.read()
            self.log(f"============= Expect: {expect_file_path} =============")
            self.log(expect_contents)
            self.log(f"============= Actual: {actual_file_path} =============")
            self.log(actual_contents)
            self.assertEqual(expect_contents, actual_contents)


class PyCodeWriterTest(PyCodeWriterTestBase):

    name = "PyCodeWriterTest"
    module_name = __module__
    data_dir = os.path.abspath(
        f"{os.path.dirname(__file__)}/generator_test_data/py_code_writer_test")
    writer_class: type[PyCodeWriterBase] = PyCodeWriter
    file_extension: str = "py"
    output_file: str = "py_code_writer_test_output"


class PyInterfaceWriterTest(PyCodeWriterTestBase):

    name = "PyInterfaceWriterTest"
    module_name = __module__
    data_dir = os.path.abspath(
        f"{os.path.dirname(__file__)}/generator_test_data/py_interface_writer_test")
    writer_class: type[PyCodeWriterBase] = PyInterfaceWriter
    file_extension: str = "pyi"
    output_file: str = "py_interface_writer_test_output"


class CodeDocumentNodeTranslatorTest(common.FakeBpyModuleTestBase):

    name = "CodeDocumentNodeTranslatorTest"
    module_name = __module__
    data_dir = os.path.abspath(
        f"{os.path.dirname(__file__)}/generator_test_data/code_document_node_translator_test")

    def setUp(self):
        super().setUp()

        self.output_dir = "fake_bpy_module_test_tmp"
        self.output_file_path = f"{self.output_dir}/code_document_node_translator_test_output"
        os.makedirs(self.output_dir, exist_ok=False)

    def tearDown(self):
        super().tearDown()

        shutil.rmtree(self.output_dir)

    def compare_with_file_contents(self, actual: str, expect_file: str):
        with open(expect_file, "r", encoding="utf-8") as f:
            expect = f.read()
        self.assertEqual(actual, expect)

    def test_basic(self):
        rst_files = ["basic.rst"]
        expect_analyzed_files = ["basic.xml"]
        expect_transformed_files = ["basic_transformed.xml"]
        expect_generated_files = ["basic.py"]
        rst_files = [f"{self.data_dir}/input/basic/{f}" for f in rst_files]
        expect_analyzed_files = [f"{self.data_dir}/expect/basic/{f}" for f in expect_analyzed_files]
        expect_transformed_files = [f"{self.data_dir}/expect/basic/{f}"
                                    for f in expect_transformed_files]
        expect_generated_files = [f"{self.data_dir}/expect/basic/{f}"
                                  for f in expect_generated_files]

        # Analyze
        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(expect_analyzed_files))
        for doc, expect in zip(documents, expect_analyzed_files):
            self.compare_with_file_contents(doc.pformat(), expect)

        # Transform
        transformer = Transformer([
            "rst_specific_node_cleaner",
            "code_document_refiner",
        ])
        documents = transformer.transform(documents)

        self.assertEqual(len(documents), len(expect_transformed_files))
        for doc, expect in zip(documents, expect_transformed_files):
            self.compare_with_file_contents(doc.pformat(), expect)

        # Generate
        writer = PyCodeWriter()
        for doc, expect_file_path in zip(documents, expect_generated_files):
            writer.write(self.output_file_path, doc)

            actual_file_path = f"{self.output_file_path}.{writer.file_format}"
            with open(actual_file_path, "r", encoding="utf-8") as f:
                expect_contents = f.read()
            with open(expect_file_path, "r", encoding="utf-8") as f:
                actual_contents = f.read()
            self.log(f"============= Expect: {expect_file_path} =============")
            self.log(expect_contents)
            self.log(f"============= Actual: {actual_file_path} =============")
            self.log(actual_contents)
            self.assertEqual(expect_contents, actual_contents)
