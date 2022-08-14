import os
import difflib
import json

from . import common
from fake_bpy_module.analyzer import (
    BaseAnalyzer,
    AnalyzerWithModFile,
    BpyModuleAnalyzer,
)
from fake_bpy_module.common import (
    SectionInfo,
    ClassInfo,
    FunctionInfo,
    VariableInfo,
)


class BaseAnalyzerTest(common.FakeBpyModuleTestBase):

    name = "BaseAnalyzerTest"
    module_name = __module__
    data_dir = os.path.abspath("{}/analyzer_test_data".format(os.path.dirname(__file__)))

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def compare_dict_and_log(self, d1, d2):
        json1 = json.dumps(d1, indent=4).split("\n")
        json2 = json.dumps(d2, indent=4).split("\n")
        diff = difflib.unified_diff(json1, json2)
        self.log("\n".join(diff))
        self.assertDictEqual(d1, d2)

    def test_no_contents(self):
        rst_files = ["no_contents.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        analyzer = BaseAnalyzer()
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 1)

        section_info = SectionInfo()

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())

    def test_only_base_class(self):
        rst_files = ["only_base_class.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        analyzer = BaseAnalyzer()
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 1)

        section_info = SectionInfo()

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())

    def test_only_module_name(self):
        rst_files = ["only_module_class.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        analyzer = BaseAnalyzer()
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 1)

        section_info = SectionInfo()

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())

    def test_single_constant(self):
        rst_files = ["single_constant.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        analyzer = BaseAnalyzer()
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 1)

        section_info = SectionInfo()

        variable_info = VariableInfo("constant")
        variable_info.from_dict({
            "type": "constant",
            "name": "DATA_1",
            "description": "DATA_1 description",
            "module": "module.a",
            "data_type": "DATA_1 type",
        }, method='NEW')
        section_info.add_info(variable_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())

    def test_multiple_constants(self):
        rst_files = ["multiple_constants.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        analyzer = BaseAnalyzer()
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 1)

        section_info = SectionInfo()

        variable_info = VariableInfo("constant")
        variable_info.from_dict({
            "type": "constant",
            "name": "DATA_1",
            "description": "DATA_1 description",
            "module": "module.a",
        }, method='NEW')
        section_info.add_info(variable_info)

        variable_info = VariableInfo("constant")
        variable_info.from_dict({
            "type": "constant",
            "name": "DATA_2",
            "module": "module.a",
            "data_type": "DATA_2 type",
        }, method='NEW')
        section_info.add_info(variable_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())

    def test_single_function(self):
        rst_files = ["single_function.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        analyzer = BaseAnalyzer()
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 1)

        section_info = SectionInfo()

        function_info = FunctionInfo("function")
        function_info.from_dict({
            "type": "function",
            "name": "function_1",
            "description": "function_1 description",
            "module": "module.a",
            "parameters": ["arg_1", "arg_2=\"test\"", "arg_3=1234"],
            "parameter_details": [{
                "type": "parameter",
                "name": "arg_1",
                "description": "function_1 arg_1 description",
                "data_type": "function_1 arg_1 type",
            },
            {
                "type": "parameter",
                "name": "arg_2",
                "description": "function_1 arg_2 description",
                "data_type": "function_1 arg_2 type",
            },
            {
                "type": "parameter",
                "name": "arg_3",
                "description": "function_1 arg_3 description",
                "data_type": "function_1 arg_3 type",
            }],
            "return": {
                "type": "return",
                "description": "function_1 return description",
                "data_type": "function_1 return type",
            }
        }, method='NEW')
        section_info.add_info(function_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())

    def test_multiple_functions(self):
        rst_files = ["multiple_functions.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        analyzer = BaseAnalyzer()
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 1)

        section_info = SectionInfo()

        function_info = FunctionInfo("function")
        function_info.from_dict({
            "type": "function",
            "name": "function_1",
            "description": "function_1 description",
            "module": "module.a",
            "parameters": ["arg_1", "arg_2"],
            "parameter_details": [{
                "type": "parameter",
                "name": "arg_1",
                "description": "function_1 arg_1 description",
                "data_type": "function_1 arg_1 type",
            },
            {
                "type": "parameter",
                "name": "arg_2",
                "description": "function_1 arg_2 description",
                "data_type": "function_1 arg_2 type",
            }]
        }, method='NEW')
        section_info.add_info(function_info)

        function_info = FunctionInfo("function")
        function_info.from_dict({
            "type": "function",
            "name": "method_1",
            "description": "method_1 description",
            "module": "module.a",
            "parameters": [],
            "parameter_details": [],
            "return": {
                "type": "return",
                "description": "method_1 return description",
                "data_type": "method_1 return type",
            }
        }, method='NEW')
        section_info.add_info(function_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())

    def test_single_class(self):
        rst_files = ["single_class.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        analyzer = BaseAnalyzer()
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 1)

        section_info = SectionInfo()

        class_info = ClassInfo()
        class_info.from_dict({
            "type": "class",
            "name": "ClassA",
            "module": "module.a",
            "description": "ClassA description",
            "attributes": [{
                "type": "attribute",
                "name": "attr_1",
                "description": "attr_1 description",
                "class": "ClassA",
                "module": "module.a",
                "data_type": "attr_1 type",
            },
            {
                "type": "attribute",
                "name": "data_1",
                "description": "data_1 description",
                "class": "ClassA",
                "module": "module.a",
                "data_type": "data_1 type",
            }],
            "methods": [{
                "type": "method",
                "name": "method_1",
                "description": "method_1 description",
                "class": "ClassA",
                "module": "module.a",
                "parameters": ["arg_1", "arg_2=\"test\""],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "method_1 arg_1 description",
                    "data_type": "method_1 arg_1 type",
                },
                {
                    "type": "parameter",
                    "name": "arg_2",
                    "description": "method_1 arg_2 description",
                    "data_type": "method_1 arg_2 type",
                }],
                "return": {
                    "type": "return",
                    "description": "method_1 return description",
                    "data_type": "method_1 return type",
                }
            },
            {
                "type": "classmethod",
                "name": "classmethod_1",
                "description": "classmethod_1 description",
                "class": "ClassA",
                "module": "module.a",
                "parameters": ["arg_1", "arg_2=123"],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "classmethod_1 arg_1 description",
                    "data_type": "classmethod_1 arg_1 type",
                },
                {
                    "type": "parameter",
                    "name": "arg_2",
                    "description": "classmethod_1 arg_2 description",
                    "data_type": "classmethod_1 arg_2 type",
                }],
                "return": {
                    "type": "return",
                    "description": "classmethod_1 return description",
                    "data_type": "classmethod_1 return type",
                }
            },
            {
                "type": "staticmethod",
                "name": "staticmethod_1",
                "description": "staticmethod_1 description",
                "class": "ClassA",
                "module": "module.a",
                "parameters": ["arg_1", "arg_2=(0, 0)"],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "staticmethod_1 arg_1 description",
                    "data_type": "staticmethod_1 arg_1 type",
                },
                {
                    "type": "parameter",
                    "name": "arg_2",
                    "description": "staticmethod_1 arg_2 description",
                    "data_type": "staticmethod_1 arg_2 type",
                }],
                "return": {
                    "type": "return",
                    "description": "staticmethod_1 return description",
                    "data_type": "staticmethod_1 return type",
                }
            },
            {
                "type": "staticmethod",
                "name": "function_1",
                "description": "function_1 description",
                "class": "ClassA",
                "module": "module.a",
                "parameters": ["arg_1", "arg_2='MAX_INT'"],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "function_1 arg_1 description",
                    "data_type": "function_1 arg_1 type",
                },
                {
                    "type": "parameter",
                    "name": "arg_2",
                    "description": "function_1 arg_2 description",
                    "data_type": "function_1 arg_2 type",
                }],
                "return": {
                    "type": "return",
                    "description": "function_1 return description",
                    "data_type": "function_1 return type",
                }
            }]
        }, method='NEW')
        section_info.add_info(class_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())

    def test_multiple_classes(self):
        rst_files = ["multiple_classes.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        analyzer = BaseAnalyzer()
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 1)

        section_info = SectionInfo()

        class_info = ClassInfo()
        class_info.from_dict({
            "type": "class",
            "name": "ClassA",
            "module": "module.a",
            "description": "ClassA description",
            "base_classes": [
                "BaseClass1",
                "BaseClass2",
            ],
            "attributes": [{
                "type": "attribute",
                "name": "attr_1",
                "description": "attr_1 description",
                "class": "ClassA",
                "module": "module.a",
                "data_type": "attr_1 type",
            }],
            "methods": [{
                "type": "method",
                "name": "method_1",
                "description": "method_1 description",
                "class": "ClassA",
                "module": "module.a",
                "parameters": [],
                "parameter_details": [],
            }]
        }, method='NEW')
        section_info.add_info(class_info)

        class_info = ClassInfo()
        class_info.from_dict({
            "type": "class",
            "name": "ClassB",
            "module": "module.a",
            "description": "ClassB description",
            "base_classes": [
                "BaseClass1",
                "BaseClass2",
            ],
            "attributes": [{
                "type": "attribute",
                "name": "data_1",
                "description": "data_1 description",
                "class": "ClassB",
                "module": "module.a",
                "data_type": "data_1 type",
            }],
            "methods": [{
                "type": "method",
                "name": "method_1",
                "description": "method_1 description",
                "class": "ClassB",
                "module": "module.a",
                "parameters": ["arg_1=5.4"],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "method_1 arg_1 description",
                    "data_type": "method_1 arg_1 type",
                }],
                "return": {
                    "type": "return",
                    "description": "method_1 return description",
                    "data_type": "method_1 return type",
                }
            }]
        }, method='NEW')
        section_info.add_info(class_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())

    def test_noisy_1(self):
        rst_files = ["noisy_1.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        analyzer = BaseAnalyzer()
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 1)

        section_info = SectionInfo()

        class_info = ClassInfo()
        class_info.from_dict({
            "type": "class",
            "name": "ClassA",
            "module": "module.a",
            "description": "ClassA description",
            "base_classes": [
                "BaseClass1",
                "BaseClass2",
            ],
            "attributes": [{
                "type": "attribute",
                "name": "attr_1",
                "description": "attr_1 description",
                "class": "ClassA",
                "module": "module.a",
                "data_type": "attr_1 type, long",
            }],
            "methods": [{
                "type": "classmethod",
                "name": "classmethod_1",
                "description": "classmethod_1 description",
                "class": "ClassA",
                "module": "module.a",
                "parameters": [],
                "parameter_details": [],
            },
            {
                "type": "staticmethod",
                "name": "staticmethod_1",
                "description": "staticmethod_1 description",
                "class": "ClassA",
                "module": "module.a",
                "parameters": ["a", "b"],
                "parameter_details": [],
            }]
        }, method='NEW')
        section_info.add_info(class_info)

        class_info = ClassInfo()
        class_info.from_dict({
            "type": "class",
            "name": "ClassB",
            "module": "module.a",
            "description": "ClassB description",
            "base_classes": [
                "BaseClass1",
                "BaseClass2",
            ],
            "attributes": [{
                "type": "attribute",
                "name": "data_1",
                "description": "data_1 description",
                "class": "ClassB",
                "module": "module.a",
                "data_type": "data_1 type",
            }],
            "methods": [{
                "type": "method",
                "name": "method_1",
                "description": "method_1 description",
                "class": "ClassB",
                "module": "module.a",
                "parameters": ["arg_1=5.4"],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "method_1 arg_1 description",
                    "data_type": "method_1 arg_1 type",
                }],
                "return": {
                    "type": "return",
                    "description": "method_1 return description",
                    "data_type": "method_1 return type",
                }
            }]
        }, method='NEW')
        section_info.add_info(class_info)

        variable_info = VariableInfo("constant")
        variable_info.from_dict({
            "type": "constant",
            "name": "DATA_1",
            "description": "DATA_1 description",
            "module": "module.a",
            "data_type": "DATA_1 type",
        }, method='NEW')
        section_info.add_info(variable_info)

        function_info = FunctionInfo("function")
        function_info.from_dict({
            "type": "function",
            "name": "function_1",
            "description": "function_1 description",
            "module": "module.a",
            "parameters": ["arg_1"],
            "parameter_details": [{
                "type": "parameter",
                "name": "arg_1",
                "description": "function_1 arg_1 description",
                "data_type": "function_1 arg_1 type",
            }],
            "return": {
                "type": "return",
                "description": "function_1 return description",
                "data_type": "function_1 return type",
            }
        }, method='NEW')
        section_info.add_info(function_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())

    def test_noisy_2(self):
        rst_files = ["noisy_2.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        analyzer = BaseAnalyzer()
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 1)

        section_info = SectionInfo()

        class_info = ClassInfo()
        class_info.from_dict({
            "type": "class",
            "name": "ClassA",
            "module": "module.a",
            "description": "ClassA description",
            "base_classes": [
                "BaseClass1",
                "BaseClass2",
            ],
            "attributes": [{
                "type": "attribute",
                "name": "attr_1",
                "description": "attr_1 description",
                "class": "ClassA",
                "module": "module.a",
                "data_type": "attr_1 type, long",
            }],
            "methods": [{
                "type": "classmethod",
                "name": "classmethod_1",
                "description": "classmethod_1 description",
                "class": "ClassA",
                "module": "module.a",
                "parameters": [],
                "parameter_details": [],
            },
            {
                "type": "staticmethod",
                "name": "staticmethod_1",
                "description": "staticmethod_1 description",
                "class": "ClassA",
                "module": "module.a",
                "parameters": ["a", "b"],
                "parameter_details": [],
            }]
        }, method='NEW')
        section_info.add_info(class_info)

        class_info = ClassInfo()
        class_info.from_dict({
            "type": "class",
            "name": "ClassB",
            "module": "module.a",
            "description": "ClassB description",
            "base_classes": [
                "BaseClass1",
                "BaseClass2",
            ],
            "attributes": [{
                "type": "attribute",
                "name": "data_1",
                "description": "data_1 description",
                "class": "ClassB",
                "module": "module.a",
                "data_type": "data_1 type",
            }],
            "methods": [{
                "type": "method",
                "name": "method_1",
                "description": "method_1 description",
                "class": "ClassB",
                "module": "module.a",
                "parameters": ["arg_1=5.4"],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "method_1 arg_1 description",
                    "data_type": "method_1 arg_1 type",
                }],
                "return": {
                    "type": "return",
                    "description": "method_1 return description",
                    "data_type": "method_1 return type",
                }
            }]
        }, method='NEW')
        section_info.add_info(class_info)

        variable_info = VariableInfo("constant")
        variable_info.from_dict({
            "type": "constant",
            "name": "DATA_1",
            "description": "DATA_1 description",
            "module": "module.a",
            "data_type": "DATA_1 type",
        }, method='NEW')
        section_info.add_info(variable_info)

        variable_info = VariableInfo("constant")
        variable_info.from_dict({
            "type": "constant",
            "name": "DATA_2",
            "description": "DATA_2 description",
            "module": "module.a",
            "data_type": "DATA_2 type",
        }, method='NEW')
        section_info.add_info(variable_info)

        function_info = FunctionInfo("function")
        function_info.from_dict({
            "type": "function",
            "name": "function_1",
            "description": "function_1 description",
            "module": "module.a",
            "parameters": ["arg_1=[[1.3, -3.4], [4.5, -0.9]]"],
            "parameter_details": [{
                "type": "parameter",
                "name": "arg_1",
                "description": "function_1 arg_1 description",
                "data_type": "function_1 arg_1 type",
            }],
            "return": {
                "type": "return",
                "description": "function_1 return description",
                "data_type": "function_1 return type",
            }
        }, method='NEW')
        section_info.add_info(function_info)

        function_info = FunctionInfo("function")
        function_info.from_dict({
            "type": "function",
            "name": "function_2",
            "description": "function_2 description",
            "module": "module.a",
            "parameters": ["arg_1", "arg_2=\"test\""],
            "parameter_details": [{
                "type": "parameter",
                "name": "arg_1",
                "description": "function_2 arg_1 description",
                "data_type": "function_2 arg_1 type",
            },
            {
                "type": "parameter",
                "name": "arg_2",
                "description": "function_2 arg_2 description",
                "data_type": "str",
            }],
            "return": {
                "type": "return",
                "description": "",
                "data_type": "",
            }
        }, method='NEW')
        section_info.add_info(function_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())

    def test_invalid_rst_format_1(self):
        rst_files = ["invalid_rst_format_1.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        analyzer = BaseAnalyzer()

        with self.assertRaises(ValueError):
            result = analyzer.analyze(rst_files)
            self.log(json.dumps(result.section_info[0].to_dict(), indent=4))

    def test_invalid_rst_format_2(self):
        rst_files = ["invalid_rst_format_2.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        analyzer = BaseAnalyzer()

        with self.assertRaises(ValueError):
            result = analyzer.analyze(rst_files)
            self.log(json.dumps(result.section_info[0].to_dict(), indent=4))

    def test_no_module(self):
        rst_files = ["no_module.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        analyzer = BaseAnalyzer()
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 1)

        section_info = SectionInfo()
        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())

    def test_bpy_290_tweak(self):
        rst_files = ["bpy_290_tweak.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        analyzer = BaseAnalyzer()
        analyzer.set_blender_version("2.90")
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 1)

        section_info = SectionInfo()

        class_info = ClassInfo()
        class_info.from_dict({
            "type": "class",
            "name": "ClassA",
            "module": "bpy.types",
            "description": "ClassA description",
            "attributes": [{
                "type": "attribute",
                "name": "attr_1",
                "description": "attr_1 description",
                "class": "ClassA",
                "module": "bpy.types",
                "data_type": "attr_1 type",
            }]
        }, method='NEW')
        section_info.add_info(class_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())

    def test_bge_support(self):
        rst_files = ["bge_support.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        analyzer = BaseAnalyzer()
        analyzer.enable_bge_support()
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 1)

        section_info = SectionInfo()

        function_info = FunctionInfo("function")
        function_info.from_dict({
            "type": "function",
            "name": "function_1",
            "description": "function_1 description",
            "module": "module.a",
            "parameters": ["arg_1", "arg_2"],
            "parameter_details": [{
                "type": "parameter",
                "name": "arg_1",
                "description": "function_1 arg_1 description",
                "data_type": "function_1 arg_1 type",
            },
            {
                "type": "parameter",
                "name": "arg_2",
                "description": "function_1 arg_2 description",
                "data_type": "function_1 arg_2 type",
            }]
        }, method='NEW')
        section_info.add_info(function_info)

        variable_info = VariableInfo("constant")
        variable_info.from_dict({
            "type": "constant",
            "name": "DATA_1",
            "description": "DATA_1 description",
            "module": "module.a",
        }, method='NEW')
        section_info.add_info(variable_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())

    def test_bge_support_no_module(self):
        rst_files = ["bge.types.NoModule.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        analyzer = BaseAnalyzer()
        analyzer.enable_bge_support()
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 1)

        section_info = SectionInfo()

        function_info = FunctionInfo("function")
        function_info.from_dict({
            "type": "function",
            "name": "function_1",
            "description": "function_1 description",
            "module": "bge.types",
            "parameters": ["arg_1", "arg_2"],
            "parameter_details": [{
                "type": "parameter",
                "name": "arg_1",
                "description": "function_1 arg_1 description",
                "data_type": "function_1 arg_1 type",
            },
            {
                "type": "parameter",
                "name": "arg_2",
                "description": "function_1 arg_2 description",
                "data_type": "function_1 arg_2 type",
            }]
        }, method='NEW')
        section_info.add_info(function_info)

        class_info = ClassInfo()
        class_info.from_dict({
            "type": "class",
            "name": "ClassA",
            "module": "bge.types",
            "description": "ClassA description",
            "attributes": [{
                "type": "attribute",
                "name": "attr_1",
                "description": "attr_1 description",
                "class": "ClassA",
                "module": "bge.types",
                "data_type": "attr_1 type",
            }],
            "methods": [{
                "type": "method",
                "name": "method_1",
                "description": "method_1 description",
                "class": "ClassA",
                "module": "bge.types",
                "parameters": ["arg_1", "arg_2=\"test\""],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "method_1 arg_1 description",
                    "data_type": "method_1 arg_1 type",
                },
                {
                    "type": "parameter",
                    "name": "arg_2",
                    "description": "method_1 arg_2 description",
                    "data_type": "method_1 arg_2 type",
                }],
                "return": {
                    "type": "return",
                    "description": "method_1 return description",
                    "data_type": "method_1 return type",
                }
            }]
        }, method='NEW')
        section_info.add_info(class_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())

    def test_multiple_sections(self):
        rst_files = ["single_constant.rst", "single_function.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        analyzer = BaseAnalyzer()
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 2)

        self.log("First section:")

        section_info = SectionInfo()

        variable_info = VariableInfo("constant")
        variable_info.from_dict({
            "type": "constant",
            "name": "DATA_1",
            "description": "DATA_1 description",
            "module": "module.a",
            "data_type": "DATA_1 type",
        }, method='NEW')
        section_info.add_info(variable_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())

        self.log("Second section:")

        section_info = SectionInfo()

        function_info = FunctionInfo("function")
        function_info.from_dict({
            "type": "function",
            "name": "function_1",
            "description": "function_1 description",
            "module": "module.a",
            "parameters": ["arg_1", "arg_2=\"test\"", "arg_3=1234"],
            "parameter_details": [{
                "type": "parameter",
                "name": "arg_1",
                "description": "function_1 arg_1 description",
                "data_type": "function_1 arg_1 type",
            },
            {
                "type": "parameter",
                "name": "arg_2",
                "description": "function_1 arg_2 description",
                "data_type": "function_1 arg_2 type",
            },
            {
                "type": "parameter",
                "name": "arg_3",
                "description": "function_1 arg_3 description",
                "data_type": "function_1 arg_3 type",
            }],
            "return": {
                "type": "return",
                "description": "function_1 return description",
                "data_type": "function_1 return type",
            }
        }, method='NEW')
        section_info.add_info(function_info)

        self.compare_dict_and_log(result.section_info[1].to_dict(),
                                  section_info.to_dict())


class AnalyzerWithModFileTest(common.FakeBpyModuleTestBase):

    name = "AnalyzerWithModFileTest"
    module_name = __module__
    data_dir = os.path.abspath("{}/analyzer_test_data".format(os.path.dirname(__file__)))

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def compare_dict_and_log(self, d1, d2):
        json1 = json.dumps(d1, indent=4).split("\n")
        json2 = json.dumps(d2, indent=4).split("\n")
        diff = difflib.unified_diff(json1, json2)
        self.log("\n".join(diff))

    def test_remove_constant(self):
        rst_files = ["multiple_constants.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        mod_files = ["remove_constant.mod"]
        mod_files = ["{}/{}".format(self.data_dir, f) for f in mod_files]

        analyzer = AnalyzerWithModFile(mod_files)
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 1)

        section_info = SectionInfo()

        variable_info = VariableInfo("constant")
        variable_info.from_dict({
            "type": "constant",
            "name": "DATA_2",
            "module": "module.a",
            "data_type": "DATA_2 type",
        }, method='NEW')
        section_info.add_info(variable_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())

    def test_remove_function(self):
        rst_files = ["multiple_functions.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        mod_files = ["remove_function.mod"]
        mod_files = ["{}/{}".format(self.data_dir, f) for f in mod_files]

        analyzer = AnalyzerWithModFile(mod_files)
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 1)

        section_info = SectionInfo()

        function_info = FunctionInfo("function")
        function_info.from_dict({
            "type": "function",
            "name": "function_1",
            "description": "function_1 description",
            "module": "module.a",
            "parameters": ["arg_1", "arg_2"],
            "parameter_details": [{
                "type": "parameter",
                "name": "arg_1",
                "description": "function_1 arg_1 description",
                "data_type": "function_1 arg_1 type",
            },
            {
                "type": "parameter",
                "name": "arg_2",
                "description": "function_1 arg_2 description",
                "data_type": "function_1 arg_2 type",
            }]
        }, method='NEW')
        section_info.add_info(function_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())

    def test_remove_class(self):
        rst_files = ["multiple_classes.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        mod_files = ["remove_class.mod"]
        mod_files = ["{}/{}".format(self.data_dir, f) for f in mod_files]

        analyzer = AnalyzerWithModFile(mod_files)
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 1)

        section_info = SectionInfo()

        class_info = ClassInfo()
        class_info.from_dict({
            "type": "class",
            "name": "ClassA",
            "module": "module.a",
            "description": "ClassA description",
            "base_classes": [
                "BaseClass1",
                "BaseClass2",
            ],
            "attributes": [{
                "type": "attribute",
                "name": "attr_1",
                "description": "attr_1 description",
                "class": "ClassA",
                "module": "module.a",
                "data_type": "attr_1 type",
            }],
            "methods": [{
                "type": "method",
                "name": "method_1",
                "description": "method_1 description",
                "class": "ClassA",
                "module": "module.a",
                "parameters": [],
                "parameter_details": [],
            }]
        }, method='NEW')
        section_info.add_info(class_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())

    def test_new_constant(self):
        rst_files = ["single_constant.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        mod_files = ["new_constant.mod"]
        mod_files = ["{}/{}".format(self.data_dir, f) for f in mod_files]

        analyzer = AnalyzerWithModFile(mod_files)
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 2)

        self.log("First section:")

        section_info = SectionInfo()

        variable_info = VariableInfo("constant")
        variable_info.from_dict({
            "type": "constant",
            "name": "DATA_1",
            "module": "module.a",
            "description": "DATA_1 description",
            "data_type": "DATA_1 type",
        }, method='NEW')
        section_info.add_info(variable_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())


        self.log("Second section:")

        section_info = SectionInfo()

        variable_info = VariableInfo("constant")
        variable_info.from_dict({
            "type": "constant",
            "name": "DATA_2",
            "module": "module.a",
            "description": "DATA_2 description",
            "data_type": "DATA_2 type",
        }, method='NEW')
        section_info.add_info(variable_info)

        self.compare_dict_and_log(result.section_info[1].to_dict(),
                                  section_info.to_dict())

    def test_new_function(self):
        rst_files = ["single_function.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        mod_files = ["new_function.mod"]
        mod_files = ["{}/{}".format(self.data_dir, f) for f in mod_files]

        analyzer = AnalyzerWithModFile(mod_files)
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 2)

        self.log("First section:")

        section_info = SectionInfo()

        function_info = FunctionInfo("function")
        function_info.from_dict({
            "type": "function",
            "name": "function_1",
            "description": "function_1 description",
            "module": "module.a",
            "parameters": ["arg_1", "arg_2=\"test\"", "arg_3=1234"],
            "parameter_details": [{
                "type": "parameter",
                "name": "arg_1",
                "description": "function_1 arg_1 description",
                "data_type": "function_1 arg_1 type",
            },
            {
                "type": "parameter",
                "name": "arg_2",
                "description": "function_1 arg_2 description",
                "data_type": "function_1 arg_2 type",
            },
            {
                "type": "parameter",
                "name": "arg_3",
                "description": "function_1 arg_3 description",
                "data_type": "function_1 arg_3 type",
            }],
            "return": {
                "type": "return",
                "description": "function_1 return description",
                "data_type": "function_1 return type",
            }
        }, method='NEW')
        section_info.add_info(function_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())


        self.log("Second section:")

        section_info = SectionInfo()

        function_info = FunctionInfo("function")
        function_info.from_dict({
            "type": "function",
            "name": "function_2",
            "description": "function_2 description",
            "module": "module.a",
            "parameters": ["arg_1", "arg_2=TEST"],
            "parameter_details": [{
                "type": "parameter",
                "name": "arg_1",
                "description": "function_2 arg_1 description",
                "data_type": "function_2 arg_1 type",
            },
            {
                "type": "parameter",
                "name": "arg_2",
                "description": "function_2 arg_2 description",
                "data_type": "function_2 arg_2 type",
            }],
            "return": {
                "type": "return",
                "description": "function_2 return description",
                "data_type": "function_2 return type",
            }
        }, method='NEW')
        section_info.add_info(function_info)

        self.compare_dict_and_log(result.section_info[1].to_dict(),
                                  section_info.to_dict())

    def test_new_class(self):
        rst_files = ["single_class.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        mod_files = ["new_class.mod"]
        mod_files = ["{}/{}".format(self.data_dir, f) for f in mod_files]

        analyzer = AnalyzerWithModFile(mod_files)
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 2)

        self.log("First section:")

        section_info = SectionInfo()

        class_info = ClassInfo()
        class_info.from_dict({
            "type": "class",
            "name": "ClassA",
            "module": "module.a",
            "description": "ClassA description",
            "attributes": [{
                "type": "attribute",
                "name": "attr_1",
                "description": "attr_1 description",
                "class": "ClassA",
                "module": "module.a",
                "data_type": "attr_1 type",
            },
            {
                "type": "attribute",
                "name": "data_1",
                "description": "data_1 description",
                "class": "ClassA",
                "module": "module.a",
                "data_type": "data_1 type",
            }],
            "methods": [{
                "type": "method",
                "name": "method_1",
                "description": "method_1 description",
                "class": "ClassA",
                "module": "module.a",
                "parameters": ["arg_1", "arg_2=\"test\""],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "method_1 arg_1 description",
                    "data_type": "method_1 arg_1 type",
                },
                {
                    "type": "parameter",
                    "name": "arg_2",
                    "description": "method_1 arg_2 description",
                    "data_type": "method_1 arg_2 type",
                }],
                "return": {
                    "type": "return",
                    "description": "method_1 return description",
                    "data_type": "method_1 return type",
                }
            },
            {
                "type": "classmethod",
                "name": "classmethod_1",
                "description": "classmethod_1 description",
                "class": "ClassA",
                "module": "module.a",
                "parameters": ["arg_1", "arg_2=123"],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "classmethod_1 arg_1 description",
                    "data_type": "classmethod_1 arg_1 type",
                },
                {
                    "type": "parameter",
                    "name": "arg_2",
                    "description": "classmethod_1 arg_2 description",
                    "data_type": "classmethod_1 arg_2 type",
                }],
                "return": {
                    "type": "return",
                    "description": "classmethod_1 return description",
                    "data_type": "classmethod_1 return type",
                }
            },
            {
                "type": "staticmethod",
                "name": "staticmethod_1",
                "description": "staticmethod_1 description",
                "class": "ClassA",
                "module": "module.a",
                "parameters": ["arg_1", "arg_2=(0, 0)"],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "staticmethod_1 arg_1 description",
                    "data_type": "staticmethod_1 arg_1 type",
                },
                {
                    "type": "parameter",
                    "name": "arg_2",
                    "description": "staticmethod_1 arg_2 description",
                    "data_type": "staticmethod_1 arg_2 type",
                }],
                "return": {
                    "type": "return",
                    "description": "staticmethod_1 return description",
                    "data_type": "staticmethod_1 return type",
                }
            },
            {
                "type": "staticmethod",
                "name": "function_1",
                "description": "function_1 description",
                "class": "ClassA",
                "module": "module.a",
                "parameters": ["arg_1", "arg_2=MAX_INT"],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "function_1 arg_1 description",
                    "data_type": "function_1 arg_1 type",
                },
                {
                    "type": "parameter",
                    "name": "arg_2",
                    "description": "function_1 arg_2 description",
                    "data_type": "function_1 arg_2 type",
                }],
                "return": {
                    "type": "return",
                    "description": "function_1 return description",
                    "data_type": "function_1 return type",
                }
            }]
        }, method='NEW')
        section_info.add_info(class_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())

        self.log("Second section:")

        section_info = SectionInfo()

        class_info = ClassInfo()
        class_info.from_dict({
            "type": "class",
            "name": "ClassB",
            "module": "module.a",
            "description": "ClassB description",
            "attributes": [{
                "type": "attribute",
                "name": "attr_1",
                "description": "attr_1 description",
                "class": "ClassB",
                "module": "module.a",
                "data_type": "attr_1 type",
            }],
            "methods": [{
                "type": "method",
                "name": "method_1",
                "description": "method_1 description",
                "class": "ClassB",
                "module": "module.a",
                "parameters": [],
                "parameter_details": [],
                "return": {
                    "type": "return",
                    "description": "method_1 return description",
                    "data_type": "method_1 return type",
                }
            },
            {
                "type": "classmethod",
                "name": "classmethod_1",
                "description": "classmethod_1 description",
                "class": "ClassB",
                "module": "module.a",
                "parameters": ["arg_1"],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "classmethod_1 arg_1 description",
                    "data_type": "classmethod_1 arg_1 type",
                }]
            },
            {
                "type": "staticmethod",
                "name": "staticmethod_1",
                "description": "staticmethod_1 description",
                "class": "ClassB",
                "module": "module.a",
                "parameters": ["arg_1", "arg_2=(0, 0)"],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "staticmethod_1 arg_1 description",
                    "data_type": "staticmethod_1 arg_1 type",
                },
                {
                    "type": "parameter",
                    "name": "arg_2",
                    "description": "staticmethod_1 arg_2 description",
                    "data_type": "staticmethod_1 arg_2 type",
                }]
            }]
        }, method='NEW')
        section_info.add_info(class_info)

        self.compare_dict_and_log(result.section_info[1].to_dict(),
                                  section_info.to_dict())

    def test_append_constant(self):
        rst_files = ["multiple_constants.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        mod_files = ["append_constant.mod"]
        mod_files = ["{}/{}".format(self.data_dir, f) for f in mod_files]

        analyzer = AnalyzerWithModFile(mod_files)
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 1)

        section_info = SectionInfo()

        variable_info = VariableInfo("constant")
        variable_info.from_dict({
            "type": "constant",
            "name": "DATA_1",
            "description": "DATA_1 description",
            "module": "module.a",
            "data_type": "DATA_1 type",
        }, method='NEW')
        section_info.add_info(variable_info)

        variable_info = VariableInfo("constant")
        variable_info.from_dict({
            "type": "constant",
            "name": "DATA_2",
            "module": "module.a",
            "data_type": "DATA_2 type",
        }, method='NEW')
        section_info.add_info(variable_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())

    def test_append_function(self):
        rst_files = ["multiple_functions.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        mod_files = ["append_function.mod"]
        mod_files = ["{}/{}".format(self.data_dir, f) for f in mod_files]

        analyzer = AnalyzerWithModFile(mod_files)
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 1)

        section_info = SectionInfo()

        function_info = FunctionInfo("function")
        function_info.from_dict({
            "type": "function",
            "name": "function_1",
            "description": "function_1 description",
            "module": "module.a",
            "parameters": ["arg_1", "arg_2"],
            "parameter_details": [{
                "type": "parameter",
                "name": "arg_1",
                "description": "function_1 arg_1 description",
                "data_type": "function_1 arg_1 type",
            },
            {
                "type": "parameter",
                "name": "arg_2",
                "description": "function_1 arg_2 description",
                "data_type": "function_1 arg_2 type",
            }],
            "return": {
                "type": "return",
                "description": "function_1 return description",
                "data_type": "function_1 return type",
            }
        }, method='NEW')
        section_info.add_info(function_info)

        function_info = FunctionInfo("function")
        function_info.from_dict({
            "type": "function",
            "name": "method_1",
            "description": "method_1 description",
            "module": "module.a",
            "parameters": ["arg_1=10"],
            "parameter_details": [{
                "type": "parameter",
                "name": "arg_1",
                "description": "method_1 arg_1 description",
                "data_type": "method_1 arg_1 type",
            }],
            "return": {
                "type": "return",
                "description": "method_1 return description",
                "data_type": "method_1 return type",
            }
        }, method='NEW')
        section_info.add_info(function_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())

    def test_append_class(self):
        rst_files = ["single_class.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        mod_files = ["append_class.mod"]
        mod_files = ["{}/{}".format(self.data_dir, f) for f in mod_files]

        analyzer = AnalyzerWithModFile(mod_files)
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 1)

        section_info = SectionInfo()

        class_info = ClassInfo()
        class_info.from_dict({
            "type": "class",
            "name": "ClassA",
            "module": "module.a",
            "description": "ClassA description",
            "attributes": [{
                "type": "attribute",
                "name": "attr_1",
                "description": "attr_1 description",
                "class": "ClassA",
                "module": "module.a",
                "data_type": "attr_1 type",
            },
            {
                "type": "attribute",
                "name": "data_1",
                "description": "data_1 description",
                "class": "ClassA",
                "module": "module.a",
                "data_type": "data_1 type",
            },
            {
                "name": "attr_2",
                "type": "attribute",
                "description": "attr_2 description",
                "class": "ClassA",
                "module": "module.a",
                "data_type": "attr_2 type",
            }],
            "methods": [{
                "type": "method",
                "name": "method_1",
                "description": "method_1 description",
                "class": "ClassA",
                "module": "module.a",
                "parameters": ["arg_1", "arg_2=\"test\""],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "method_1 arg_1 description",
                    "data_type": "method_1 arg_1 type",
                },
                {
                    "type": "parameter",
                    "name": "arg_2",
                    "description": "method_1 arg_2 description",
                    "data_type": "method_1 arg_2 type",
                }],
                "return": {
                    "type": "return",
                    "description": "method_1 return description",
                    "data_type": "method_1 return type",
                }
            },
            {
                "type": "classmethod",
                "name": "classmethod_1",
                "description": "classmethod_1 description",
                "class": "ClassA",
                "module": "module.a",
                "parameters": ["arg_1", "arg_2=123"],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "classmethod_1 arg_1 description",
                    "data_type": "classmethod_1 arg_1 type",
                },
                {
                    "type": "parameter",
                    "name": "arg_2",
                    "description": "classmethod_1 arg_2 description",
                    "data_type": "classmethod_1 arg_2 type",
                }],
                "return": {
                    "type": "return",
                    "description": "classmethod_1 return description",
                    "data_type": "classmethod_1 return type",
                }
            },
            {
                "type": "staticmethod",
                "name": "staticmethod_1",
                "description": "staticmethod_1 description",
                "class": "ClassA",
                "module": "module.a",
                "parameters": ["arg_1", "arg_2=(0, 0)"],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "staticmethod_1 arg_1 description",
                    "data_type": "staticmethod_1 arg_1 type",
                },
                {
                    "type": "parameter",
                    "name": "arg_2",
                    "description": "staticmethod_1 arg_2 description",
                    "data_type": "staticmethod_1 arg_2 type",
                }],
                "return": {
                    "type": "return",
                    "description": "staticmethod_1 return description",
                    "data_type": "staticmethod_1 return type",
                }
            },
            {
                "type": "staticmethod",
                "name": "function_1",
                "description": "function_1 description",
                "class": "ClassA",
                "module": "module.a",
                "parameters": ["arg_1", "arg_2=MAX_INT"],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "function_1 arg_1 description",
                    "data_type": "function_1 arg_1 type",
                },
                {
                    "type": "parameter",
                    "name": "arg_2",
                    "description": "function_1 arg_2 description",
                    "data_type": "function_1 arg_2 type",
                }],
                "return": {
                    "type": "return",
                    "description": "function_1 return description",
                    "data_type": "function_1 return type",
                }
            },
            {
                "name": "method_2",
                "type": "function",
                "description": "method_2 description",
                "module": "module.a",
                "parameters": ["arg_1"],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "method_2 arg_1 description",
                    "data_type": "method_2 arg_1 type",
                }],
                "return": {
                    "type": "return",
                    "description": "method_2 return description",
                    "data_type": "method_2 return type",
                }
            }]
        }, method='NEW')
        section_info.add_info(class_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())

    def test_update_constant(self):
        rst_files = ["single_constant.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        mod_files = ["update_constant.mod"]
        mod_files = ["{}/{}".format(self.data_dir, f) for f in mod_files]

        analyzer = AnalyzerWithModFile(mod_files)
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 1)

        section_info = SectionInfo()

        variable_info = VariableInfo("constant")
        variable_info.from_dict({
            "type": "constant",
            "name": "DATA_1",
            "module": "module.a",
            "description": "DATA_1 description",
            "data_type": "DATA_1 type updated",
        }, method='NEW')
        section_info.add_info(variable_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())

    def test_update_function(self):
        rst_files = ["single_function.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        mod_files = ["update_function.mod"]
        mod_files = ["{}/{}".format(self.data_dir, f) for f in mod_files]

        analyzer = AnalyzerWithModFile(mod_files)
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 1)

        section_info = SectionInfo()

        function_info = FunctionInfo("function")
        function_info.from_dict({
            "type": "function",
            "name": "function_1",
            "description": "function_1 description updated",
            "module": "module.a",
            "parameters": ["arg_1", "arg_2=\"test\"", "arg_3=12345"],
            "parameter_details": [{
                "type": "parameter",
                "name": "arg_1",
                "description": "function_1 arg_1 description updated",
                "data_type": "function_1 arg_1 type",
            },
            {
                "type": "parameter",
                "name": "arg_2",
                "description": "function_1 arg_2 description",
                "data_type": "function_1 arg_2 type",
            },
            {
                "type": "parameter",
                "name": "arg_3",
                "description": "function_1 arg_3 description",
                "data_type": "function_1 arg_3 type",
            }],
            "return": {
                "type": "return",
                "description": "function_1 return description",
                "data_type": "function_1 return type updated",
            }
        }, method='NEW')
        section_info.add_info(function_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())

    def test_update_class(self):
        rst_files = ["single_class.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        mod_files = ["update_class.mod"]
        mod_files = ["{}/{}".format(self.data_dir, f) for f in mod_files]

        analyzer = AnalyzerWithModFile(mod_files)
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 1)

        section_info = SectionInfo()

        class_info = ClassInfo()
        class_info.from_dict({
            "type": "class",
            "name": "ClassA",
            "module": "module.a",
            "description": "ClassA description updated",
            "attributes": [{
                "type": "attribute",
                "name": "attr_1",
                "description": "attr_1 description",
                "class": "ClassA",
                "module": "module.a",
                "data_type": "attr_1 type updated",
            },
            {
                "type": "attribute",
                "name": "data_1",
                "description": "data_1 description",
                "class": "ClassA",
                "module": "module.a",
                "data_type": "data_1 type",
            }],
            "methods": [{
                "type": "method",
                "name": "method_1",
                "description": "method_1 description updated",
                "class": "ClassA",
                "module": "module.a",
                "parameters": ["arg_1", "arg_2=\"test2\""],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "method_1 arg_1 description",
                    "data_type": "method_1 arg_1 type updated",
                },
                {
                    "type": "parameter",
                    "name": "arg_2",
                    "description": "method_1 arg_2 description",
                    "data_type": "method_1 arg_2 type",
                }],
                "return": {
                    "type": "return",
                    "description": "method_1 return description updated",
                    "data_type": "method_1 return type",
                }
            },
            {
                "type": "classmethod",
                "name": "classmethod_1",
                "description": "classmethod_1 description",
                "class": "ClassA",
                "module": "module.a",
                "parameters": ["arg_1", "arg_2=123"],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "classmethod_1 arg_1 description",
                    "data_type": "classmethod_1 arg_1 type",
                },
                {
                    "type": "parameter",
                    "name": "arg_2",
                    "description": "classmethod_1 arg_2 description",
                    "data_type": "classmethod_1 arg_2 type",
                }],
                "return": {
                    "type": "return",
                    "description": "classmethod_1 return description",
                    "data_type": "classmethod_1 return type",
                }
            },
            {
                "type": "staticmethod",
                "name": "staticmethod_1",
                "description": "staticmethod_1 description",
                "class": "ClassA",
                "module": "module.a",
                "parameters": ["arg_1", "arg_2=(0, 0)"],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "staticmethod_1 arg_1 description",
                    "data_type": "staticmethod_1 arg_1 type",
                },
                {
                    "type": "parameter",
                    "name": "arg_2",
                    "description": "staticmethod_1 arg_2 description",
                    "data_type": "staticmethod_1 arg_2 type",
                }],
                "return": {
                    "type": "return",
                    "description": "staticmethod_1 return description",
                    "data_type": "staticmethod_1 return type",
                }
            },
            {
                "type": "staticmethod",
                "name": "function_1",
                "description": "function_1 description",
                "class": "ClassA",
                "module": "module.a",
                "parameters": ["arg_1", "arg_2=MAX_INT"],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "arg_1",
                    "description": "function_1 arg_1 description",
                    "data_type": "function_1 arg_1 type",
                },
                {
                    "type": "parameter",
                    "name": "arg_2",
                    "description": "function_1 arg_2 description",
                    "data_type": "function_1 arg_2 type",
                }],
                "return": {
                    "type": "return",
                    "description": "function_1 return description",
                    "data_type": "function_1 return type",
                }
            }]
        }, method='NEW')
        section_info.add_info(class_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())


class BpyModuleAnalyzerTest(common.FakeBpyModuleTestBase):

    name = "BpyModuleAnalyzerTest"
    module_name = __module__
    data_dir = os.path.abspath("{}/analyzer_test_data".format(os.path.dirname(__file__)))

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def compare_dict_and_log(self, d1, d2):
        json1 = json.dumps(d1, indent=4).split("\n")
        json2 = json.dumps(d2, indent=4).split("\n")
        diff = difflib.unified_diff(json1, json2)
        self.log("\n".join(diff))
        self.assertDictEqual(d1, d2)

    def test_add_bpy_ops_override_parameters(self):
        rst_files = ["add_bpy_ops_override_parameters.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        analyzer = BpyModuleAnalyzer([])
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 1)

        section_info = SectionInfo()

        function_info = FunctionInfo("function")
        function_info.from_dict({
            "type": "function",
            "name": "function_1",
            "description": "function_1 description",
            "module": "bpy.ops",
            "parameters": ["override_context=None", "execution_context=None", "undo=None", "*", "arg_1"],
            "parameter_details": [{
                "type": "parameter",
                "name": "override_context",
                "description": "",
                "data_type": "dict, bpy.types.Context",
            },
            {
                "type": "parameter",
                "name": "execution_context",
                "description": "",
                "data_type": "str, int",
            },
            {
                "type": "parameter",
                "name": "undo",
                "description": "",
                "data_type": "bool",
            },
            {
                "type": "parameter",
                "name": "arg_1",
                "description": "function_1 arg_1 description",
                "data_type": "function_1 arg_1 type",
            }]
        }, method='NEW')
        section_info.add_info(function_info)

        function_info = FunctionInfo("function")
        function_info.from_dict({
            "type": "function",
            "name": "function_2",
            "description": "function_2 description",
            "module": "bpy.ops",
            "parameters": ["override_context=None", "execution_context=None", "undo=None"],
            "parameter_details": [{
                "type": "parameter",
                "name": "override_context",
                "description": "",
                "data_type": "dict, bpy.types.Context",
            },
            {
                "type": "parameter",
                "name": "execution_context",
                "description": "",
                "data_type": "str, int",
            },
            {
                "type": "parameter",
                "name": "undo",
                "description": "",
                "data_type": "bool",
            }]
        }, method='NEW')
        section_info.add_info(function_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info.to_dict())

    def test_make_bpy_context_variable(self):
        rst_files = ["make_bpy_context_variable_1.rst", "make_bpy_context_variable_2.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        analyzer = BpyModuleAnalyzer([])
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 3)

        section_info_bpy_types = SectionInfo()

        class_info = ClassInfo()
        class_info.from_dict({
            "type": "class",
            "name": "Context",
            "module": "bpy.types",
            "description": "context",
            "attributes": [{
                "type": "attribute",
                "name": "attr_1",
                "description": "attr_1 description",
                "class": "Context",
                "module": "bpy.types",
                "data_type": "attr_1 type",
            },
            {
                "type": "attribute",
                "name": "attr_2",
                "description": "attr_2 description",
                "class": "Context",
                "module": "bpy.types",
                "data_type": "attr_2 type",
            }],
            "methods": []
        }, method='NEW')
        section_info_bpy_types.add_info(class_info)

        section_info_bpy_context = SectionInfo()

        variable_info = VariableInfo("constant")
        variable_info.from_dict({
            "type": "constant",
            "name": "context",
            "description": "",
            "module": "bpy",
            "data_type": "bpy.types.Context",
        }, method='NEW')
        section_info_bpy_context.add_info(variable_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info_bpy_types.to_dict())
        self.assertEqual(len(result.section_info[1].info_list), 0)
        self.compare_dict_and_log(result.section_info[2].to_dict(),
                                  section_info_bpy_context.to_dict())

    def test_tweak_bpy_types_classes(self):
        rst_files = ["tweak_bpy_types_classes_1.rst", "tweak_bpy_types_classes_2.rst"]
        rst_files = ["{}/{}".format(self.data_dir, f) for f in rst_files]

        analyzer = BpyModuleAnalyzer([])
        result = analyzer.analyze(rst_files)

        self.assertEqual(len(result.section_info), 2)

        section_info_bpy_prop_collection = SectionInfo()

        class_info = ClassInfo()
        class_info.from_dict({
            "type": "class",
            "name": "bpy_prop_collection",
            "module": "bpy.types",
            "description": "bpy_prop_collection description",
            "base_classes": [
                "typing.Generic['GenericType']",
            ],
            "attributes": [],
            "methods": [{
                "type": "method",
                "name": "__getitem__",
                "description": "",
                "class": "bpy_prop_collection",
                "module": "bpy.types",
                "parameters": ["key"],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "key",
                    "description": "",
                    "data_type": "int, str",
                }],
                "return": {
                    "type": "return",
                    "description": "",
                    "data_type": "'GenericType'",
                }
            },
            {
                "type": "method",
                "name": "__setitem__",
                "description": "",
                "class": "bpy_prop_collection",
                "module": "bpy.types",
                "parameters": ["key", "value"],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "key",
                    "description": "",
                    "data_type": "int, str",
                },
                {
                    "type": "parameter",
                    "name": "value",
                    "description": "",
                    "data_type": "'GenericType'",
                }]
            }]
        }, method='NEW')
        section_info_bpy_prop_collection.add_info(class_info)

        section_info_bpy_struct = SectionInfo()

        class_info = ClassInfo()
        class_info.from_dict({
            "type": "class",
            "name": "bpy_struct",
            "module": "bpy.types",
            "description": "bpy_struct description",
            "base_classes": [],
            "attributes": [],
            "methods": [{
                "type": "method",
                "name": "__getitem__",
                "description": "",
                "class": "bpy_struct",
                "module": "bpy.types",
                "parameters": ["key"],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "key",
                    "description": "",
                    "data_type": "int, str",
                }],
                "return": {
                    "type": "return",
                    "description": "",
                    "data_type": "'typing.Any'",
                }
            },
            {
                "type": "method",
                "name": "__setitem__",
                "description": "",
                "class": "bpy_struct",
                "module": "bpy.types",
                "parameters": ["key", "value"],
                "parameter_details": [{
                    "type": "parameter",
                    "name": "key",
                    "description": "",
                    "data_type": "int, str",
                },
                {
                    "type": "parameter",
                    "name": "value",
                    "description": "",
                    "data_type": "'typing.Any'",
                }]
            }]
        }, method='NEW')
        section_info_bpy_struct.add_info(class_info)

        self.compare_dict_and_log(result.section_info[0].to_dict(),
                                  section_info_bpy_prop_collection.to_dict())
        self.compare_dict_and_log(result.section_info[1].to_dict(),
                                  section_info_bpy_struct.to_dict())