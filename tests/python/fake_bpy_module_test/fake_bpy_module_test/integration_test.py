import shutil
import os

from fake_bpy_module.analyzer.analyzer import analyze   # pylint: disable=E0401
from fake_bpy_module.transformer.transformer import transform   # pylint: disable=E0401
from fake_bpy_module.generator.generator import generate    # pylint: disable=E0401
from fake_bpy_module.config import PackageGenerationConfig  # pylint: disable=E0401
from . import common


class IntegrationTest(common.FakeBpyModuleTestBase):

    name = "IntegrationTest"
    module_name = __module__
    data_dir = os.path.abspath(
        f"{os.path.dirname(__file__)}/integration_test_data/integration_test")

    def setUp(self):
        super().setUp()

        self.output_dir = "fake_bpy_module_test_tmp"
        self.output_file_path = f"{self.output_dir}/integration_test_output"
        os.makedirs(self.output_dir, exist_ok=False)

    def tearDown(self):
        super().tearDown()

        shutil.rmtree(self.output_dir)

    def __create_package_generator_config(self) -> PackageGenerationConfig:
        config = PackageGenerationConfig()
        config.output_dir = self.output_dir
        config.os = "Linux"
        config.style_format = "ruff"
        config.target = "blender"
        config.target_version = "2.80"
        config.mod_version = "2.80"

        return config

    def __is_py_typed_exist(self, filepath: str) -> bool:
        if not os.path.isfile(filepath):
            return False
        return os.path.getsize(filepath) == 0

    def test_single(self):
        rst_files = [
            f"{self.data_dir}/input/single/module_abc.rst",
        ]

        config = self.__create_package_generator_config()

        ext_patterns = ["py", "pyi"]
        for ext in ext_patterns:
            config.output_format = ext
            documents = analyze(rst_files, config)
            documents = transform(documents, [])
            generate(documents, config)

            expect_files_dir = f"{self.data_dir}/expect/single"
            actual_files_dir = self.output_dir

            py_files = [
                f"module_abc/__init__.{ext}",
            ]
            for file_ in py_files:
                expect_file_path = f"{expect_files_dir}/{file_}"
                actual_file_path = f"{actual_files_dir}/{file_}"
                with open(actual_file_path, "r", encoding="utf-8") as f:
                    expect_contents = f.read()
                with open(expect_file_path, "r", encoding="utf-8") as f:
                    actual_contents = f.read()
                self.log(f"============= Expect: {expect_file_path} =============")
                self.log(expect_contents)
                self.log(f"============= Actual: {actual_file_path} =============")
                self.log(actual_contents)
                self.assertEqual(expect_contents, actual_contents)

            self.assertFalse(self.__is_py_typed_exist(f"{self.output_dir}/py.typed"))

    def test_multiple(self):
        rst_files = [
            f"{self.data_dir}/input/multiple/module_1.rst",
            f"{self.data_dir}/input/multiple/module_1.submodule_1.rst",
            f"{self.data_dir}/input/multiple/module_2.rst",
        ]

        config = self.__create_package_generator_config()

        ext_patterns = ["py", "pyi"]
        for ext in ext_patterns:
            config.output_format = ext
            documents = analyze(rst_files, config)
            documents = transform(documents, [])
            generate(documents, config)

            expect_files_dir = f"{self.data_dir}/expect/multiple"
            actual_files_dir = self.output_dir

            py_files = [
                f"module_1/__init__.{ext}",
                f"module_1/submodule_1/__init__.{ext}",
                f"module_2/__init__.{ext}",
            ]
            for file_ in py_files:
                expect_file_path = f"{expect_files_dir}/{file_}"
                actual_file_path = f"{actual_files_dir}/{file_}"
                with open(actual_file_path, "r", encoding="utf-8") as f:
                    expect_contents = f.read()
                with open(expect_file_path, "r", encoding="utf-8") as f:
                    actual_contents = f.read()
                self.log(f"============= Expect: {expect_file_path} =============")
                self.log(expect_contents)
                self.log(f"============= Actual: {actual_file_path} =============")
                self.log(actual_contents)
                self.assertEqual(expect_contents, actual_contents)

            self.assertFalse(self.__is_py_typed_exist(f"{self.output_dir}/py.typed"))

    def test_eceptional(self):
        rst_files = [
            f"{self.data_dir}/input/exceptional/module_exceptional.rst",
        ]

        config = self.__create_package_generator_config()

        ext_patterns = ["py", "pyi"]
        for ext in ext_patterns:
            config.output_format = ext
            documents = analyze(rst_files, config)
            documents = transform(documents, [])
            generate(documents, config)

            expect_files_dir = f"{self.data_dir}/expect/exceptional"
            actual_files_dir = self.output_dir

            py_files = [
                f"module_exceptional/__init__.{ext}",
            ]
            for file_ in py_files:
                expect_file_path = f"{expect_files_dir}/{file_}"
                actual_file_path = f"{actual_files_dir}/{file_}"
                with open(actual_file_path, "r", encoding="utf-8") as f:
                    expect_contents = f.read()
                with open(expect_file_path, "r", encoding="utf-8") as f:
                    actual_contents = f.read()
                self.log(f"============= Expect: {expect_file_path} =============")
                self.log(expect_contents)
                self.log(f"============= Actual: {actual_file_path} =============")
                self.log(actual_contents)
                self.assertEqual(expect_contents, actual_contents)

            self.assertFalse(self.__is_py_typed_exist(f"{self.output_dir}/py.typed"))
