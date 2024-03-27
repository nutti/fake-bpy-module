import os

# pylint: disable=E0401
from fake_bpy_module.analyzer import BaseAnalyzer
from fake_bpy_module.docutils_based.transformer.transformer import Transformer
from .. import common


class ModApplierTest(common.FakeBpyModuleTestBase):

    name = "ModApplierTest"
    module_name = __module__
    data_dir = os.path.abspath(
        f"{os.path.dirname(__file__)}/../mod_applier_test_data")

    def compare_with_file_contents(self, actual: str, expect_file: str):
        with open(expect_file, "r", encoding="utf-8") as f:
            expect = f.read()
        self.assertEqual(actual, expect)

    def test_new_data(self):
        rst_files = ["base.rst"]
        mod_files = ["new_data.mod.rst"]
        expect_mod_files = ["new_data.mod.xml"]
        expect_files = ["new_data.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        mod_files = [f"{self.data_dir}/input/{f}" for f in mod_files]
        expect_mod_files = [f"{self.data_dir}/expect/{f}" for f in expect_mod_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer(mod_files)
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        transformer = Transformer(["mod_applier"], {"mod_applier": {"mod_files": mod_files}})
        transformed = transformer.transform(documents)
        self.assertEqual(len(transformer.get_transformers()), 1)
        mod_documents = transformer.get_transformers()[0].get_mod_documents()

        self.assertEqual(len(mod_documents), len(expect_mod_files))
        for mod_doc, expect_file in zip(mod_documents, expect_mod_files):
            self.compare_with_file_contents(mod_doc.pformat(), expect_file)

        self.assertEqual(len(transformed), len(rst_files))
        for doc, expect_file in zip(transformed, expect_files):
            self.compare_with_file_contents(doc.pformat(), expect_file)

    def test_new_function(self):
        rst_files = ["base.rst"]
        mod_files = ["new_function.mod.rst"]
        expect_mod_files = ["new_function.mod.xml"]
        expect_files = ["new_function.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        mod_files = [f"{self.data_dir}/input/{f}" for f in mod_files]
        expect_mod_files = [f"{self.data_dir}/expect/{f}" for f in expect_mod_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer(mod_files)
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        transformer = Transformer(["mod_applier"], {"mod_applier": {"mod_files": mod_files}})
        transformed = transformer.transform(documents)
        self.assertEqual(len(transformer.get_transformers()), 1)
        mod_documents = transformer.get_transformers()[0].get_mod_documents()

        self.assertEqual(len(mod_documents), len(expect_mod_files))
        for mod_doc, expect_file in zip(mod_documents, expect_mod_files):
            self.compare_with_file_contents(mod_doc.pformat(), expect_file)

        self.assertEqual(len(transformed), len(rst_files))
        for doc, expect_file in zip(transformed, expect_files):
            self.compare_with_file_contents(doc.pformat(), expect_file)

    def test_new_class(self):
        rst_files = ["base.rst"]
        mod_files = ["new_class.mod.rst"]
        expect_mod_files = ["new_class.mod.xml"]
        expect_files = ["new_class.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        mod_files = [f"{self.data_dir}/input/{f}" for f in mod_files]
        expect_mod_files = [f"{self.data_dir}/expect/{f}" for f in expect_mod_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer(mod_files)
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        transformer = Transformer(["mod_applier"], {"mod_applier": {"mod_files": mod_files}})
        transformed = transformer.transform(documents)
        self.assertEqual(len(transformer.get_transformers()), 1)
        mod_documents = transformer.get_transformers()[0].get_mod_documents()

        self.assertEqual(len(mod_documents), len(expect_mod_files))
        for mod_doc, expect_file in zip(mod_documents, expect_mod_files):
            self.compare_with_file_contents(mod_doc.pformat(), expect_file)

        self.assertEqual(len(transformed), len(rst_files))
        for doc, expect_file in zip(transformed, expect_files):
            self.compare_with_file_contents(doc.pformat(), expect_file)

    def test_append_function(self):
        rst_files = ["base.rst"]
        mod_files = ["append_function.mod.rst"]
        expect_mod_files = ["append_function.mod.xml"]
        expect_files = ["append_function.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        mod_files = [f"{self.data_dir}/input/{f}" for f in mod_files]
        expect_mod_files = [f"{self.data_dir}/expect/{f}" for f in expect_mod_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer(mod_files)
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        transformer = Transformer(["mod_applier"], {"mod_applier": {"mod_files": mod_files}})
        transformed = transformer.transform(documents)
        self.assertEqual(len(transformer.get_transformers()), 1)
        mod_documents = transformer.get_transformers()[0].get_mod_documents()

        self.assertEqual(len(mod_documents), len(expect_mod_files))
        for mod_doc, expect_file in zip(mod_documents, expect_mod_files):
            self.compare_with_file_contents(mod_doc.pformat(), expect_file)

        self.assertEqual(len(transformed), len(rst_files))
        for doc, expect_file in zip(transformed, expect_files):
            self.compare_with_file_contents(doc.pformat(), expect_file)

    def test_append_class(self):
        rst_files = ["base.rst"]
        mod_files = ["append_class.mod.rst"]
        expect_mod_files = ["append_class.mod.xml"]
        expect_files = ["append_class.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        mod_files = [f"{self.data_dir}/input/{f}" for f in mod_files]
        expect_mod_files = [f"{self.data_dir}/expect/{f}" for f in expect_mod_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer(mod_files)
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        transformer = Transformer(["mod_applier"], {"mod_applier": {"mod_files": mod_files}})
        transformed = transformer.transform(documents)
        self.assertEqual(len(transformer.get_transformers()), 1)
        mod_documents = transformer.get_transformers()[0].get_mod_documents()

        self.assertEqual(len(mod_documents), len(expect_mod_files))
        for mod_doc, expect_file in zip(mod_documents, expect_mod_files):
            self.compare_with_file_contents(mod_doc.pformat(), expect_file)

        self.assertEqual(len(transformed), len(rst_files))
        for doc, expect_file in zip(transformed, expect_files):
            self.compare_with_file_contents(doc.pformat(), expect_file)

    def test_mod_option(self):
        mod_files = ["mod_option.mod.rst"]
        expect_mod_files = ["mod_option.mod.xml"]
        mod_files = [f"{self.data_dir}/input/{f}" for f in mod_files]
        expect_mod_files = [f"{self.data_dir}/expect/{f}" for f in expect_mod_files]

        transformer = Transformer(["mod_applier"], {"mod_applier": {"mod_files": mod_files}})
        _ = transformer.transform([])
        self.assertEqual(len(transformer.get_transformers()), 1)
        mod_documents = transformer.get_transformers()[0].get_mod_documents()

        self.assertEqual(len(mod_documents), len(expect_mod_files))
        for mod_doc, expect_file in zip(mod_documents, expect_mod_files):
            self.compare_with_file_contents(mod_doc.pformat(), expect_file)
