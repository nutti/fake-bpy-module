import os

# pylint: disable=E0401
from fake_bpy_module.analyzer import BaseAnalyzer
from fake_bpy_module.docutils_based.transformer.transformer import Transformer
from fake_bpy_module.generator import ModuleStructure, EntryPoint
from .. import common


class DataTypeRefinerTest(common.FakeBpyModuleTestBase):

    name = "TransformerTest"
    module_name = __module__
    data_dir = os.path.abspath(
        f"{os.path.dirname(__file__)}/../transformer_test_data")

    def compare_with_file_contents(self, actual: str, expect_file: str):
        with open(expect_file, "r", encoding="utf-8") as f:
            expect = f.read()
        self.assertEqual(actual, expect)

    def test_basic(self):
        rst_files = ["data_type_refiner.rst"]
        expect_files = ["data_type_refiner.xml"]
        expect_transformed_files = ["data_type_refiner_transformed.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}" for f in expect_transformed_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
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

        self.assertEqual(len(documents), 1)
        self.compare_with_file_contents(documents[0].pformat(),
                                        expect_files[0])

        transformer = Transformer(["data_type_refiner"], {
            "data_type_refiner": {
                "package_structure": package_structure,
                "entry_points": entry_points,
            }
        })
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), 1)
        self.compare_with_file_contents(transformed[0].pformat(),
                                        expect_transformed_files[0])

    def test_various_data_type(self):
        rst_files = ["data_type_refiner_various_data_type.rst"]
        expect_files = ["data_type_refiner_various_data_type.xml"]
        expect_transformed_files = ["data_type_refiner_various_data_type_transformed.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}" for f in expect_transformed_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
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

        self.assertEqual(len(documents), 1)
        self.compare_with_file_contents(documents[0].pformat(),
                                        expect_files[0])

        transformer = Transformer(["data_type_refiner"], {
            "data_type_refiner": {
                "entry_points": entry_points,
            }
        })
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), 1)
        self.compare_with_file_contents(transformed[0].pformat(),
                                        expect_transformed_files[0])

    def test_special_data_type(self):
        rst_files = ["data_type_refiner_special_data_type.rst"]
        expect_files = ["data_type_refiner_special_data_type.xml"]
        expect_transformed_files = ["data_type_refiner_special_data_type_transformed.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]
        expect_transformed_files = [f"{self.data_dir}/expect/{f}" for f in expect_transformed_files]

        analyzer = BaseAnalyzer([])
        analyzer.set_target("blender")
        analyzer.set_target_version("2.80")
        documents = analyzer.analyze(rst_files)

        entry_points = []
        entry_point = EntryPoint("module_1", "ClassA", "class")
        entry_points.append(entry_point)
        entry_point = EntryPoint("module_2", "ClassB", "class")
        entry_points.append(entry_point)

        self.assertEqual(len(documents), 1)
        self.compare_with_file_contents(documents[0].pformat(),
                                        expect_files[0])

        transformer = Transformer(["data_type_refiner"], {
            "data_type_refiner": {
                "entry_points": entry_points,
            }
        })
        transformed = transformer.transform(documents)

        self.assertEqual(len(transformed), 1)
        self.compare_with_file_contents(transformed[0].pformat(),
                                        expect_transformed_files[0])
