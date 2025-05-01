import argparse
import inspect
import re
import shutil
import sys
import unittest
from pathlib import Path

TESTS_TEMPLATE_FILE = "template.py.tpl"
GENERATED_TESTS_DIR = "generated_tests"


class ImportModuleTestConfig:
    def __init__(self) -> None:
        self.modules_path = ""


def parse_options(config: ImportModuleTestConfig) -> None:
    usage = f"Usage: python {__file__} [-p <modules_path>]"
    parser = argparse.ArgumentParser(usage)
    parser.add_argument(
        "-p", dest="modules_path", type=str, help="fake-bpy-module path")

    args = parser.parse_args()
    if args.modules_path:
        config.modules_path = args.modules_path


def generate_tests(config: ImportModuleTestConfig) -> list:
    # Search modules to test.
    files = Path(config.modules_path).glob("*")
    module_names = []
    for f in files:
        basename = Path(f).name
        if basename == "py.typed":
            continue
        path = Path(basename)
        module_name = path.parent / path.stem
        module_names.append(str(module_name))

    # Load template.
    script_dir = Path(__file__).parent
    path = Path(f"{script_dir}/{TESTS_TEMPLATE_FILE}")
    with path.open("r", encoding="utf-8") as f:
        template_content = f.readlines()

    # Generate test codes.
    tests_dir = f"{script_dir}/{GENERATED_TESTS_DIR}"
    Path(tests_dir).mkdir(exist_ok=False)
    init_file = Path(f"{tests_dir}/__init__.py").open("w",   # pylint: disable=R1732  # noqa: SIM115
                     encoding="utf-8")

    def replace_template_content(
            content: list[str], module_name: str) -> list[str]:
        output = []
        for raw_line in content:
            line = re.sub(
                r"<%% CLASS_NAME %%>",
                "{}ImportTest".format(  # pylint: disable=C0209
                    re.sub(
                        r"_(.)",
                        lambda x: x.group(1).upper(),
                        module_name.capitalize()
                    )
                ),
                raw_line)
            line = re.sub(r"<%% MODULE_NAME %%>", module_name, line)
            output.append(line)
        return output

    for mod_name in module_names:
        test_codes = replace_template_content(template_content, mod_name)
        path = Path(f"{tests_dir}/{mod_name}_test.py")
        with path.open("w", encoding="utf-8") as f:
            f.writelines(test_codes)
        init_file.write(f"from . import {mod_name}_test\n")
    init_file.close()

    # Load generated modules.
    # After this time, we can delete generated test codes.
    sys.path.append(str(Path(__file__).parent))
    # pylint: disable=W0122
    exec(f"import {GENERATED_TESTS_DIR}")  # noqa: S102

    # Get test cases.
    generated_tests_package = sys.modules[GENERATED_TESTS_DIR]
    tests_modules = [
        m[1]
        for m in inspect.getmembers(generated_tests_package, inspect.ismodule)]
    test_cases = []
    for m in tests_modules:
        test_cases.extend([
            m[1]
            for m in inspect.getmembers(m, inspect.isclass)])

    # Delete generated test codes.
    shutil.rmtree(tests_dir)

    return test_cases


def run_tests(test_cases: list) -> bool:
    suite = unittest.TestSuite()
    for case in test_cases:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(case))
    return unittest.TextTestRunner().run(suite).wasSuccessful()


def main() -> None:
    # Parse options.
    config = ImportModuleTestConfig()
    parse_options(config)

    # Add testee module.
    path = Path(config.modules_path).resolve()
    sys.path.append(str(path))

    # Generate tests.
    test_cases = generate_tests(config)

    # Run tests.
    ret = run_tests(test_cases)
    sys.exit(not ret)


if __name__ == "__main__":
    main()
