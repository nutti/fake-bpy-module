import os
import sys
import argparse
import unittest
import glob
import re
import shutil
import inspect

from typing import List


TESTS_TEMPLATE_FILE = "template.py.tpl"
GENERATED_TESTS_DIR = "generated_tests"


class ImportModuleTestConfig:
    def __init__(self):
        self.modules_path = ""


def parse_options(config: ImportModuleTestConfig):
    usage = "Usage: python {} [-p <modules_path>]".format(__file__)
    parser = argparse.ArgumentParser(usage)
    parser.add_argument("-p", dest="modules_path", type=str, help="fake-bpy-module path")

    args = parser.parse_args()
    if args.modules_path:
        config.modules_path = args.modules_path


def generate_tests(config: ImportModuleTestConfig) -> list:
    # Search modules to test.
    files = glob.glob("{}/*".format(config.modules_path), recursive=False)
    module_names = [os.path.splitext(os.path.basename(f))[0] for f in files]

    # Load template.
    script_dir = os.path.dirname(__file__)
    with open("{}/{}".format(script_dir, TESTS_TEMPLATE_FILE), "r") as f:
        template_content = f.readlines()

    # Generate test codes.
    tests_dir = "{}/{}".format(script_dir, GENERATED_TESTS_DIR)
    os.makedirs(tests_dir, exist_ok=False)
    init_file = open("{}/__init__.py".format(tests_dir), "w")

    def replace_template_content(content: List[str], module_name: str) -> List[str]:
        output = []
        for line in content:
            line = re.sub(r"<%% CLASS_NAME %%>",
                          "{}ImportTest".format(re.sub(r"_(.)", lambda x: x.group(1).upper(), module_name.capitalize())),
                          line)
            line = re.sub(r"<%% MODULE_NAME %%>", module_name, line)
            output.append(line)
        return output

    for mod_name in module_names:
        test_codes = replace_template_content(template_content, mod_name)
        with open("{}/{}_test.py".format(tests_dir, mod_name), "w") as f:
            f.writelines(test_codes)
        init_file.write("from . import {}_test\n".format(mod_name))
    init_file.close()

    # Load generated modules.
    # After this time, we can delete generated test codes.
    sys.path.append(os.path.dirname(__file__))
    exec("import {}".format(GENERATED_TESTS_DIR))

    # Get test cases.
    generated_tests_package = sys.modules[GENERATED_TESTS_DIR]
    tests_modules = [m[1] for m in inspect.getmembers(generated_tests_package, inspect.ismodule)]
    test_cases = []
    for m in tests_modules:
        test_cases.extend([m[1] for m in inspect.getmembers(m, inspect.isclass)])

    # Delete generated test codes.
    shutil.rmtree(tests_dir)

    return test_cases


def run_tests(test_cases: list) -> bool:
    suite = unittest.TestSuite()
    for case in test_cases:
        suite.addTest(unittest.makeSuite(case))
    ret = unittest.TextTestRunner().run(suite).wasSuccessful()

    return ret


def main():
    # Parse options.
    config = ImportModuleTestConfig()
    parse_options(config)

    # Add testee module.
    path = os.path.abspath(config.modules_path)
    sys.path.append(path)

    # Generate tests.
    test_cases = generate_tests(config)

    # Run tests.
    ret = run_tests(test_cases)
    sys.exit(not ret)


if __name__ == "__main__":
    main()
