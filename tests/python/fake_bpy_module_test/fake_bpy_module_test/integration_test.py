import shutil
from pathlib import Path

from fake_bpy_module import config  # pylint: disable=E0401
from fake_bpy_module.analyzer.analyzer import analyze  # pylint: disable=E0401
from fake_bpy_module.generator.generator import (
    generate,  # pylint: disable=E0401
)
from fake_bpy_module.transformer.transformer import (
    transform,  # pylint: disable=E0401
)

from . import common


class IntegrationTest(common.FakeBpyModuleTestBase):

    name = "IntegrationTest"
    module_name = __module__
    data_dir = Path(
        f"{Path(__file__).parent}/integration_test_data/integration_test").resolve()

    def setUp(self) -> None:
        super().setUp()

        self.output_dir = "fake_bpy_module_test_tmp"
        self.output_file_path = f"{self.output_dir}/integration_test_output"
        Path(self.output_dir).mkdir(parents=True, exist_ok=False)

        self.__setup_config()

    def tearDown(self) -> None:
        super().tearDown()

        shutil.rmtree(self.output_dir)

    def __setup_config(self) -> None:
        config.set_output_dir(self.output_dir)
        config.set_os("Linux")
        config.set_style_format("ruff")
        config.set_target("blender")
        config.set_target_version("2.80")
        config.set_mod_version("2.80")

    def __is_py_typed_exist(self, filepath: str) -> bool:
        if not Path(filepath).is_file():
            return False
        return Path(filepath).stat().st_size == 0

    def test_single(self) -> None:
        rst_files = [
            f"{self.data_dir}/input/single/module_abc.rst",
        ]

        ext_patterns = ["py", "pyi"]
        for ext in ext_patterns:
            config.set_output_format(ext)
            documents = analyze(rst_files)
            documents = transform(documents, [])
            generate(documents)

            expect_files_dir = f"{self.data_dir}/expect/single"
            actual_files_dir = self.output_dir

            py_files = [
                f"module_abc/__init__.{ext}",
            ]
            for file_ in py_files:
                expect_file_path = f"{expect_files_dir}/{file_}"
                actual_file_path = f"{actual_files_dir}/{file_}"
                with Path(actual_file_path).open("r", encoding="utf-8") as f:
                    expect_contents = f.read()
                with Path(expect_file_path).open("r", encoding="utf-8") as f:
                    actual_contents = f.read()
                self.log(
                    f"============= Expect: {expect_file_path} =============")
                self.log(expect_contents)
                self.log(
                    f"============= Actual: {actual_file_path} =============")
                self.log(actual_contents)
                self.assertEqual(expect_contents, actual_contents)

            self.assertFalse(self.__is_py_typed_exist(f"{self.output_dir}/py.typed"))

    def test_multiple(self) -> None:
        rst_files = [
            f"{self.data_dir}/input/multiple/module_1.rst",
            f"{self.data_dir}/input/multiple/module_1.submodule_1.rst",
            f"{self.data_dir}/input/multiple/module_2.rst",
        ]

        ext_patterns = ["py", "pyi"]
        for ext in ext_patterns:
            config.set_output_format(ext)
            documents = analyze(rst_files)
            documents = transform(documents, [])
            generate(documents)

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
                with Path(actual_file_path).open("r", encoding="utf-8") as f:
                    expect_contents = f.read()
                with Path(expect_file_path).open("r", encoding="utf-8") as f:
                    actual_contents = f.read()
                self.log(
                    f"============= Expect: {expect_file_path} =============")
                self.log(expect_contents)
                self.log(
                    f"============= Actual: {actual_file_path} =============")
                self.log(actual_contents)
                self.assertEqual(expect_contents, actual_contents)

            self.assertFalse(self.__is_py_typed_exist(f"{self.output_dir}/py.typed"))

    def test_eceptional(self) -> None:
        rst_files = [
            f"{self.data_dir}/input/exceptional/module_exceptional.rst",
        ]

        ext_patterns = ["py", "pyi"]
        for ext in ext_patterns:
            config.set_output_format(ext)
            documents = analyze(rst_files)
            documents = transform(documents, [])
            generate(documents)

            expect_files_dir = f"{self.data_dir}/expect/exceptional"
            actual_files_dir = self.output_dir

            py_files = [
                f"module_exceptional/__init__.{ext}",
            ]
            for file_ in py_files:
                expect_file_path = f"{expect_files_dir}/{file_}"
                actual_file_path = f"{actual_files_dir}/{file_}"
                with Path(actual_file_path).open("r", encoding="utf-8") as f:
                    expect_contents = f.read()
                with Path(expect_file_path).open("r", encoding="utf-8") as f:
                    actual_contents = f.read()
                self.log(
                    f"============= Expect: {expect_file_path} =============")
                self.log(expect_contents)
                self.log(
                    f"============= Actual: {actual_file_path} =============")
                self.log(actual_contents)
                self.assertEqual(expect_contents, actual_contents)

            self.assertFalse(self.__is_py_typed_exist(f"{self.output_dir}/py.typed"))
