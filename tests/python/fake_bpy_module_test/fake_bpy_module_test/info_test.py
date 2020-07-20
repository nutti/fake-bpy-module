from . import common
from fake_bpy_module.common import (
    DataType,
    UnknownDataType,
    IntermidiateDataType,
    BuiltinDataType,
    ModifierDataType,
    CustomDataType,
    MixinDataType,
    Info,
    ParameterDetailInfo,
    ReturnInfo,
    VariableInfo,
    FunctionInfo,
    ClassInfo,
    SectionInfo,
)


class DataTypeTest(common.FakeBpyModuleTestBase):

    name = "DataTypeTest"
    module_name = __module__

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_all(self):
        data_type = DataType()

        with self.assertRaises(NotImplementedError):
            data_type.type()
        with self.assertRaises(NotImplementedError):
            data_type.has_modifier()
        with self.assertRaises(NotImplementedError):
            data_type.modifier()
        with self.assertRaises(NotImplementedError):
            data_type.data_type()
        with self.assertRaises(NotImplementedError):
            data_type.to_string()


class UnknownDataTypeTest(common.FakeBpyModuleTestBase):

    name = "UnknownDataTypeTest"
    module_name = __module__

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_all(self):
        data_type = UnknownDataType()

        self.assertEqual(data_type.type(), 'UNKNOWN')
        with self.assertRaises(RuntimeError):
            data_type.has_modifier()
        with self.assertRaises(RuntimeError):
            data_type.modifier()
        with self.assertRaises(RuntimeError):
            data_type.data_type()
        self.assertEqual(data_type.to_string(), "")


class IntermidiateDataTypeTest(common.FakeBpyModuleTestBase):

    name = "IntermidiateDataTypeTest"
    module_name = __module__

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_all(self):
        data_type = IntermidiateDataType("data_type_1")

        self.assertEqual(data_type.type(), 'INTERMIDIATE')
        with self.assertRaises(RuntimeError):
            data_type.has_modifier()
        with self.assertRaises(RuntimeError):
            data_type.modifier()
        with self.assertRaises(RuntimeError):
            data_type.data_type()
        self.assertEqual(data_type.to_string(), "data_type_1")


class BuiltinDataTypeTest(common.FakeBpyModuleTestBase):

    name = "BuiltinDataTypeTest"
    module_name = __module__

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_valid_data_type_without_modifier(self):
        data_type = BuiltinDataType("int")

        self.assertEqual(data_type.type(), 'BUILTIN')
        self.assertFalse(data_type.has_modifier())
        self.assertIsNone(data_type.modifier())
        self.assertEqual(data_type.data_type(), "int")
        self.assertEqual(data_type.to_string(), "int")

    def test_valid_data_type_with_modifier(self):
        data_type = BuiltinDataType("float", modifier="list")

        self.assertEqual(data_type.type(), 'BUILTIN')
        self.assertTrue(data_type.has_modifier())
        self.assertEqual(data_type.modifier(), "list")
        self.assertEqual(data_type.data_type(), "float")
        self.assertEqual(data_type.to_string(), "typing.List[float]")

    def test_invalid_data_type(self):
        with self.assertRaises(ValueError):
            BuiltinDataType("invalid_data_type")

    def test_invalid_modifier(self):
        with self.assertRaises(ValueError):
            BuiltinDataType("float", modifier="invalid_modifier")


class ModifierDataTypeTest(common.FakeBpyModuleTestBase):

    name = "ModifierDataTypeTest"
    module_name = __module__

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_valid_modifier(self):
        data_type = ModifierDataType("dict")

        self.assertEqual(data_type.type(), 'MODIFIER')
        with self.assertRaises(RuntimeError):
            data_type.has_modifier()
        self.assertEqual(data_type.modifier(), "dict")
        with self.assertRaises(RuntimeError):
            data_type.data_type()
        self.assertEqual(data_type.to_string(), "dict")

    def test_invalid_modifier(self):
        with self.assertRaises(ValueError):
            ModifierDataType("invalid_modifier")


class CustomDataTypeTest(common.FakeBpyModuleTestBase):

    name = "CustomDataTypeTest"
    module_name = __module__

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_valid_without_modifier(self):
        data_type = CustomDataType("custom_data_type")

        self.assertEqual(data_type.type(), 'CUSTOM')
        self.assertFalse(data_type.has_modifier())
        self.assertIsNone(data_type.modifier())
        self.assertEqual(data_type.data_type(), "custom_data_type")
        self.assertEqual(data_type.to_string(), "'custom_data_type'")

    def test_valid_with_modifier(self):
        data_type = CustomDataType("custom_data_type", modifier="set")

        self.assertEqual(data_type.type(), 'CUSTOM')
        self.assertTrue(data_type.has_modifier())
        self.assertEqual(data_type.modifier(), "set")
        self.assertEqual(data_type.data_type(), "custom_data_type")
        self.assertEqual(data_type.to_string(), "typing.Set['custom_data_type']")

    def test_invalid_modifier(self):
        with self.assertRaises(ValueError):
            CustomDataType("custom_data_type", modifier="invalid_modifier")


class MixinDataTypeTest(common.FakeBpyModuleTestBase):

    name = "MixinDataTypeTest"
    module_name = __module__

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_single_data_type(self):
        data_type_1 = BuiltinDataType("float")

        with self.assertRaises(ValueError):
            mixin_data_type = MixinDataType([data_type_1])

    def test_multiple_data_type(self):
        data_type_1 = BuiltinDataType("str")
        data_type_2 = CustomDataType("custom_data_type", modifier="set")
        mixin_data_type = MixinDataType([data_type_1, data_type_2])

        self.assertEqual(mixin_data_type.type(), 'MIXIN')
        self.assertSetEqual(set(mixin_data_type.data_types()), {data_type_1, data_type_2})
        self.assertEqual(mixin_data_type.to_string(), "typing.Union[str, typing.Set['custom_data_type']]")

        data_type_3 = ModifierDataType("list")
        mixin_data_type.set_data_type(0, data_type_3)
        self.assertSetEqual(set(mixin_data_type.data_types()), {data_type_3, data_type_2})
        self.assertEqual(mixin_data_type.to_string(), "typing.Union[list, typing.Set['custom_data_type']]")


class InfoTest(common.FakeBpyModuleTestBase):

    name = "InfoTest"
    module_name = __module__

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_is_assinable(self):
        info = Info()
        data = {
            "key_1": "value_1",
            "key_2": "value_2",
        }

        self.assertTrue(info.is_assignable(None, data, "key_1", 'NEW'))
        self.assertFalse(info.is_assignable(None, data, "key_3", 'NEW'))
        self.assertTrue(info.is_assignable(None, data, "key_2", 'APPEND'))
        self.assertFalse(info.is_assignable("variable", data, "key_1", 'APPEND'))
        self.assertFalse(info.is_assignable(None, data, "key_3", 'APPEND'))
        self.assertTrue(info.is_assignable(None, data, "key_2", 'UPDATE'))
        self.assertFalse(info.is_assignable(None, data, "key_3", 'UPDATE'))
        with self.assertRaises(RuntimeError):
            info.is_assignable(None, data, "key_1", 'INVALID_METHOD')

    def test_is_data_type_assignable(self):
        info = Info()
        data = {
            "key_1": BuiltinDataType("int"),
            "key_2": ModifierDataType("dict"),
        }

        self.assertTrue(info.is_data_type_assinable(None, data, "key_1", 'NEW'))
        self.assertFalse(info.is_data_type_assinable(None, data, "key_3", 'NEW'))
        self.assertTrue(info.is_data_type_assinable(UnknownDataType(), data, "key_1", 'APPEND'))
        self.assertFalse(info.is_data_type_assinable("variable", data, "key_1", 'APPEND'))
        self.assertFalse(info.is_data_type_assinable(UnknownDataType(), data, "key_3", 'APPEND'))
        self.assertTrue(info.is_data_type_assinable(None, data, "key_1", 'UPDATE'))
        self.assertFalse(info.is_data_type_assinable(None, data, "key_3", 'UPDATE'))
        with self.assertRaises(RuntimeError):
            info.is_data_type_assinable(None, data, "key_1", 'INVALID_METHOD')

    def test_other_methods(self):
        info = Info()

        with self.assertRaises(NotImplementedError):
            info.name()
        with self.assertRaises(NotImplementedError):
            info.module()
        with self.assertRaises(RuntimeError):
            info.type()
        with self.assertRaises(NotImplementedError):
            info.to_dict()
        with self.assertRaises(NotImplementedError):
            info.from_dict({}, "")


class ParameterDetailTest(common.FakeBpyModuleTestBase):

    name = "ParameterDetailTest"
    module_name = __module__

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_setter_getter_methods(self):
        data_type = BuiltinDataType("int")
        info = ParameterDetailInfo()
        info.set_name("param_1")
        info.set_description("param_1 description")
        info.set_data_type(data_type)

        self.assertEqual(info.type(), "parameter")
        self.assertEqual(info.name(), "param_1")
        self.assertEqual(info.description(), "param_1 description")
        self.assertEqual(info.data_type(), data_type)

        with self.assertRaises(NotImplementedError):
            info.module()

    def test_append_description(self):
        data_type = BuiltinDataType("int")
        info = ParameterDetailInfo()
        info.set_description("param_1 description")

        self.assertEqual(info.description(), "param_1 description")

        info.append_description(" appended")
        info.append_description(" more")

        self.assertEqual(info.description(), "param_1 description appended more")

    def test_to_dict(self):
        data_type = BuiltinDataType("int")
        info = ParameterDetailInfo()
        info.set_name("param_1")
        info.set_description("param_1 description")
        info.set_data_type(data_type)

        expect = {
            "type": "parameter",
            "name": "param_1",
            "description": "param_1 description",
            "data_type": "int",
        }
        actual = info.to_dict()

        self.assertDictEqual(expect, actual)

    def test_from_dict_method_new(self):
        data = {
            "type": "parameter",
            "name": "param_1",
            "description": "param_1 description",
            "data_type": "int",
        }

        info = ParameterDetailInfo()
        info.from_dict(data, method='NEW')

        self.assertEqual(info.name(), "param_1")
        self.assertEqual(info.description(), "param_1 description")
        self.assertEqual(info.data_type().to_string(), "int")
        self.assertDictEqual(info.to_dict(), data)

    def test_from_dict_method_append(self):
        info = ParameterDetailInfo()
        info.set_name("param_1")

        data = {
            "type": "parameter",
            "description": "param_1 description",
            "data_type": "int",
        }
        info.from_dict(data, method='APPEND')

        self.assertEqual(info.name(), "param_1")
        self.assertEqual(info.description(), "param_1 description")
        self.assertEqual(info.data_type().to_string(), "int")

        expect = {
            "type": "parameter",
            "name": "param_1",
            "description": "param_1 description",
            "data_type": "int",
        }
        actual = info.to_dict()
        self.assertDictEqual(expect, actual)

    def test_from_dict_method_update(self):
        data_type = BuiltinDataType("float")
        info = ParameterDetailInfo()
        info.set_name("param_1")
        info.set_description("param_1 description")
        info.set_data_type(data_type)

        data = {
            "type": "parameter",
            "description": "param_1 description updated",
            "data_type": "int",
        }
        info.from_dict(data, method='UPDATE')

        self.assertEqual(info.name(), "param_1")
        self.assertEqual(info.description(), "param_1 description updated")
        self.assertEqual(info.data_type().to_string(), "int")

        expect = {
            "type": "parameter",
            "name": "param_1",
            "description": "param_1 description updated",
            "data_type": "int",
        }
        actual = info.to_dict()
        self.assertDictEqual(expect, actual)


class ReturnInfoTest(common.FakeBpyModuleTestBase):

    name = "ReturnInfo"
    module_name = __module__

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_setter_getter_methods(self):
        data_type = BuiltinDataType("int")
        info = ReturnInfo()
        info.set_description("return description")
        info.set_data_type(data_type)

        self.assertEqual(info.type(), "return")
        self.assertEqual(info.description(), "return description")
        self.assertEqual(info.data_type(), data_type)

        with self.assertRaises(NotImplementedError):
            info.name()
        with self.assertRaises(NotImplementedError):
            info.module()

    def test_append_description(self):
        data_type = BuiltinDataType("int")
        info = ReturnInfo()
        info.set_description("return description")

        self.assertEqual(info.description(), "return description")

        info.append_description(" appended")
        info.append_description(" more")

        self.assertEqual(info.description(), "return description appended more")

    def test_to_dict(self):
        data_type = BuiltinDataType("int")
        info = ReturnInfo()
        info.set_description("return description")
        info.set_data_type(data_type)

        expect = {
            "type": "return",
            "description": "return description",
            "data_type": "int",
        }
        actual = info.to_dict()

        self.assertDictEqual(expect, actual)

    def test_from_dict_method_new(self):
        data = {
            "type": "return",
            "description": "return description",
            "data_type": "int",
        }

        info = ReturnInfo()
        info.from_dict(data, method='NEW')

        self.assertEqual(info.description(), "return description")
        self.assertEqual(info.data_type().to_string(), "int")
        self.assertDictEqual(info.to_dict(), data)

    def test_from_dict_method_append(self):
        info = ReturnInfo()

        data = {
            "type": "return",
            "description": "return description",
            "data_type": "int",
        }
        info.from_dict(data, method='APPEND')

        self.assertEqual(info.description(), "return description")
        self.assertEqual(info.data_type().to_string(), "int")

        expect = {
            "type": "return",
            "description": "return description",
            "data_type": "int",
        }
        actual = info.to_dict()
        self.assertDictEqual(expect, actual)

    def test_from_dict_method_update(self):
        data_type = BuiltinDataType("float")
        info = ReturnInfo()
        info.set_description("return description")
        info.set_data_type(data_type)

        data = {
            "type": "return",
            "description": "return description updated",
            "data_type": "int",
        }
        info.from_dict(data, method='UPDATE')

        self.assertEqual(info.description(), "return description updated")
        self.assertEqual(info.data_type().to_string(), "int")

        expect = {
            "type": "return",
            "description": "return description updated",
            "data_type": "int",
        }
        actual = info.to_dict()
        self.assertDictEqual(expect, actual)


class VariableInfoTest(common.FakeBpyModuleTestBase):

    name = "VariableInfoTest"
    module_name = __module__

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_setter_getter_methods(self):
        data_type = BuiltinDataType("int")
        info = VariableInfo("constant")
        info.set_name("constant_1")
        info.set_description("constant_1 description")
        info.set_class("ClassA")
        info.set_module("module.a")
        info.set_data_type(data_type)

        self.assertEqual(info.type(), "constant")
        self.assertEqual(info.name(), "constant_1")
        self.assertEqual(info.data_type(), data_type)
        self.assertEqual(info.description(), "constant_1 description")
        self.assertEqual(info.module(), "module.a")

    def test_append_description(self):
        data_type = BuiltinDataType("int")
        info = VariableInfo("constant")
        info.set_description("constant_1 description")

        self.assertEqual(info.description(), "constant_1 description")

        info.append_description(" appended")
        info.append_description(" more")

        self.assertEqual(info.description(), "constant_1 description appended more")

    def test_to_dict(self):
        data_type = BuiltinDataType("int")
        info = VariableInfo("attribute")
        info.set_name("attribute_1")
        info.set_description("attribute_1 description")
        info.set_class("ClassA")
        info.set_module("module.a")
        info.set_data_type(data_type)

        expect = {
            "type": "attribute",
            "name": "attribute_1",
            "description": "attribute_1 description",
            "class": "ClassA",
            "module": "module.a",
            "data_type": "int",
        }
        actual = info.to_dict()

        self.assertDictEqual(expect, actual)

    def test_from_dict_method_new(self):
        data = {
            "type": "attribute",
            "name": "attribute_1",
            "description": "attribute_1 description",
            "class": "ClassA",
            "module": "module.a",
            "data_type": "int",
        }

        info = VariableInfo("attribute")
        info.from_dict(data, method='NEW')

        self.assertEqual(info.name(), "attribute_1")
        self.assertEqual(info.description(), "attribute_1 description")
        self.assertEqual(info.module(), "module.a")
        self.assertEqual(info.data_type().to_string(), "int")
        self.assertDictEqual(info.to_dict(), data)

    def test_from_dict_method_append(self):
        info = VariableInfo("constant")
        info.set_name("constant_1")

        data = {
            "type": "constant",
            "description": "constant_1 description",
            "data_type": "int",
        }
        info.from_dict(data, method='APPEND')

        self.assertEqual(info.name(), "constant_1")
        self.assertEqual(info.description(), "constant_1 description")
        self.assertEqual(info.data_type().to_string(), "int")

        expect = {
            "type": "constant",
            "name": "constant_1",
            "description": "constant_1 description",
            "module": "",
            "class": "",
            "data_type": "int",
        }
        actual = info.to_dict()
        self.assertDictEqual(expect, actual)

    def test_from_dict_method_update(self):
        data_type = BuiltinDataType("float")
        info = VariableInfo("attribute")
        info.set_name("attribute_1")
        info.set_description("attribute_1 description")
        info.set_data_type(data_type)

        data = {
            "type": "attribute",
            "data_type": "int",
            "module": "module.a",
            "class": "ClassA",
        }
        info.from_dict(data, method='UPDATE')

        self.assertEqual(info.data_type().to_string(), "int")
        self.assertEqual(info.module(), "module.a")

        expect = {
            "type": "attribute",
            "name": "attribute_1",
            "description": "attribute_1 description",
            "data_type": "int",
            "module": "module.a",
            "class": "ClassA",
        }
        actual = info.to_dict()
        self.assertDictEqual(expect, actual)


class FunctionInfoTest(common.FakeBpyModuleTestBase):

    name = "FunctionInfoTest"
    module_name = __module__

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_setter_getter_methods_case_1(self):
        info = FunctionInfo("function")
        info.set_name("function_1")
        info.set_parameters(["param_1", "param_2"])
        info.set_description("function_1 description")
        info.set_module("module.a")

        param_data_type_1 = BuiltinDataType("int")
        param_info_1 = ParameterDetailInfo()
        param_info_1.set_name("param_1")
        param_info_1.set_description("param_1 description")
        param_info_1.set_data_type(param_data_type_1)

        param_data_type_2 = BuiltinDataType("float")
        param_info_2 = ParameterDetailInfo()
        param_info_2.set_name("param_2")
        param_info_2.set_description("param_2 description")
        param_info_2.set_data_type(param_data_type_2)

        info.set_parameter_details([param_info_1, param_info_2])

        return_data_type = BuiltinDataType("bool")
        return_info = ReturnInfo()
        return_info.set_description("return description")
        return_info.set_data_type(return_data_type)

        info.set_return(return_info)

        self.assertEqual(info.type(), "function")
        self.assertEqual(info.name(), "function_1")
        self.assertEqual(len(info.parameters()), 2)
        self.assertSetEqual(set(info.parameters()), {"param_1", "param_2"})
        self.assertEqual(info.parameter(0), "param_1")
        self.assertEqual(info.parameter(1), "param_2")
        self.assertEqual(len(info.parameter_details()), 2)
        self.assertSetEqual(set(info.parameter_details()), {param_info_1, param_info_2})
        self.assertEqual(info.return_(), return_info)
        self.assertEqual(info.module(), "module.a")
        self.assertEqual(info.description(), "function_1 description")

    def test_setter_getter_methods_case_2(self):
        info = FunctionInfo("method")
        info.set_name("method_1")
        info.add_parameter("param_1")
        info.add_parameters(["param_2", "param_3", "param_4"])
        info.set_parameter(1, "param_5")
        info.remove_parameter(3)
        info.set_description("method_1 description")
        info.set_class("ClassA")
        info.set_module("module.a")

        param_data_type_1 = BuiltinDataType("int")
        param_info_1 = ParameterDetailInfo()
        param_info_1.set_name("param_1")
        param_info_1.set_description("param_1 description")
        param_info_1.set_data_type(param_data_type_1)
        info.add_parameter_detail(param_info_1)

        param_data_type_2 = BuiltinDataType("float")
        param_info_2 = ParameterDetailInfo()
        param_info_2.set_name("param_5")
        param_info_2.set_description("param_5 description")
        param_info_2.set_data_type(param_data_type_2)

        param_data_type_3 = BuiltinDataType("bool")
        param_info_3 = ParameterDetailInfo()
        param_info_3.set_name("param_3")
        param_info_3.set_description("param_3 description")
        param_info_3.set_data_type(param_data_type_3)

        info.add_parameter_details([param_info_2, param_info_3])

        info.append_description(" appended")
        info.append_description(" more")

        self.assertEqual(info.type(), "method")
        self.assertEqual(info.name(), "method_1")
        self.assertEqual(len(info.parameters()), 3)
        self.assertSetEqual(set(info.parameters()), {"param_1", "param_5", "param_3"})
        self.assertEqual(info.parameter(0), "param_1")
        self.assertEqual(info.parameter(1), "param_5")
        self.assertEqual(info.parameter(2), "param_3")
        self.assertEqual(len(info.parameter_details()), 3)
        self.assertSetEqual(set(info.parameter_details()), {param_info_1, param_info_2, param_info_3})
        self.assertEqual(info.module(), "module.a")
        self.assertEqual(info.description(), "method_1 description appended more")

    def test_to_dict(self):
        info = FunctionInfo("function")
        info.set_name("function_1")
        info.set_parameters(["param_1", "param_2"])
        info.set_description("function_1 description")
        info.set_class("ClassA")
        info.set_module("module.a")

        param_data_type_1 = BuiltinDataType("int")
        param_info_1 = ParameterDetailInfo()
        param_info_1.set_name("param_1")
        param_info_1.set_description("param_1 description")
        param_info_1.set_data_type(param_data_type_1)

        param_data_type_2 = BuiltinDataType("float")
        param_info_2 = ParameterDetailInfo()
        param_info_2.set_name("param_2")
        param_info_2.set_description("param_2 description")
        param_info_2.set_data_type(param_data_type_2)

        info.set_parameter_details([param_info_1, param_info_2])

        return_data_type = BuiltinDataType("bool")
        return_info = ReturnInfo()
        return_info.set_description("return description")
        return_info.set_data_type(return_data_type)

        info.set_return(return_info)

        expect = {
            "type": "function",
            "name": "function_1",
            "description": "function_1 description",
            "class": "ClassA",
            "module": "module.a",
            "parameters": ["param_1", "param_2"],
            "parameter_details": [
                {
                    "type": "parameter",
                    "name": "param_1",
                    "description": "param_1 description",
                    "data_type": "int",
                },
                {
                    "type": "parameter",
                    "name": "param_2",
                    "description": "param_2 description",
                    "data_type": "float",
                }
            ],
            "return": {
                "type": "return",
                "description": "return description",
                "data_type": "bool",
            },
        }
        actual = info.to_dict()

        self.assertDictEqual(expect, actual)

    def test_from_dict_method_new(self):
        data = {
            "type": "function",
            "name": "function_1",
            "description": "function_1 description",
            "class": "",
            "module": "module.a",
            "parameters": ["param_1", "param_2"],
            "parameter_details": [
                {
                    "type": "parameter",
                    "name": "param_1",
                    "description": "param_1 description",
                    "data_type": "int",
                },
                {
                    "type": "parameter",
                    "name": "param_2",
                    "description": "param_2 description",
                    "data_type": "float",
                }
            ],
            "return": {
                "type": "return",
                "description": "return description",
                "data_type": "bool",
            },
        }

        info = FunctionInfo("function")
        info.from_dict(data, method='NEW')

        self.assertEqual(info.name(), "function_1")
        self.assertEqual(len(info.parameters()), 2)
        self.assertSetEqual(set(info.parameters()), {"param_1", "param_2"})
        self.assertEqual(info.parameter(0), "param_1")
        self.assertEqual(info.parameter(1), "param_2")
        self.assertEqual(len(info.parameter_details()), 2)
        self.assertEqual(info.parameter_details()[0].name(), "param_1")
        self.assertEqual(info.parameter_details()[0].description(), "param_1 description")
        self.assertEqual(info.parameter_details()[0].data_type().to_string(), "int")
        self.assertEqual(info.parameter_details()[1].name(), "param_2")
        self.assertEqual(info.parameter_details()[1].description(), "param_2 description")
        self.assertEqual(info.parameter_details()[1].data_type().to_string(), "float")
        self.assertEqual(info.module(), "module.a")
        self.assertEqual(info.description(), "function_1 description")
        self.assertEqual(info.return_().description(), "return description")
        self.assertEqual(info.return_().data_type().to_string(), "bool")
        self.assertDictEqual(info.to_dict(), data)

    def test_from_dict_method_append(self):
        info = FunctionInfo("function")
        info.set_name("function_1")
        info.set_parameters(["param_1", "param_2"])
        info.set_module("module.a")

        param_data_type_1 = BuiltinDataType("int")
        param_info_1 = ParameterDetailInfo()
        param_info_1.set_name("param_1")
        param_info_1.set_description("param_1 description")
        param_info_1.set_data_type(param_data_type_1)

        param_data_type_2 = BuiltinDataType("float")
        param_info_2 = ParameterDetailInfo()
        param_info_2.set_name("param_2")
        param_info_2.set_data_type(param_data_type_2)

        info.set_parameter_details([param_info_1, param_info_2])

        data = {
            "type": "function",
            "name": "function_1",
            "module": "module.a",
            "description": "function_1 description",
            "parameters": ["param_3"],
            "parameter_details": [
                {
                    "type": "parameter",
                    "name": "param_2",
                    "description": "param_2 description updated",
                },
                {
                    "type": "parameter",
                    "name": "param_3",
                    "description": "param_3 description",
                    "data_type": "bool",
                }
            ],
            "return": {
                "type": "return",
                "description": "return description",
                "data_type": "bool",
            }
        }
        info.from_dict(data, method='APPEND')

        self.assertEqual(info.name(), "function_1")
        self.assertEqual(len(info.parameters()), 3)
        self.assertSetEqual(set(info.parameters()), {"param_1", "param_2", "param_3"})
        self.assertEqual(info.parameter(0), "param_1")
        self.assertEqual(info.parameter(1), "param_2")
        self.assertEqual(info.parameter(2), "param_3")
        self.assertEqual(len(info.parameter_details()), 3)
        self.assertEqual(info.parameter_details()[0].name(), "param_1")
        self.assertEqual(info.parameter_details()[0].description(), "param_1 description")
        self.assertEqual(info.parameter_details()[0].data_type().to_string(), "int")
        self.assertEqual(info.parameter_details()[1].name(), "param_2")
        self.assertEqual(info.parameter_details()[1].description(), "param_2 description updated")
        self.assertEqual(info.parameter_details()[1].data_type().to_string(), "float")
        self.assertEqual(info.parameter_details()[2].name(), "param_3")
        self.assertEqual(info.parameter_details()[2].description(), "param_3 description")
        self.assertEqual(info.parameter_details()[2].data_type().to_string(), "bool")
        self.assertEqual(info.module(), "module.a")
        self.assertEqual(info.description(), "function_1 description")
        self.assertEqual(info.return_().description(), "return description")
        self.assertEqual(info.return_().data_type().to_string(), "bool")

        expect = {
            "type": "function",
            "name": "function_1",
            "description": "function_1 description",
            "class": "",
            "module": "module.a",
            "parameters": ["param_1", "param_2", "param_3"],
            "parameter_details": [
                {
                    "type": "parameter",
                    "name": "param_1",
                    "description": "param_1 description",
                    "data_type": "int",
                },
                {
                    "type": "parameter",
                    "name": "param_2",
                    "description": "param_2 description updated",
                    "data_type": "float",
                },
                {
                    "type": "parameter",
                    "name": "param_3",
                    "description": "param_3 description",
                    "data_type": "bool",
                }
            ],
            "return": {
                "type": "return",
                "description": "return description",
                "data_type": "bool",
            },
        }
        actual = info.to_dict()
        self.assertDictEqual(expect, actual)

    def test_from_dict_method_update(self):
        info = FunctionInfo("function")
        info.set_name("function_1")
        info.set_parameters(["param_1", "param_2"])
        info.set_module("module.a")

        param_data_type_1 = BuiltinDataType("int")
        param_info_1 = ParameterDetailInfo()
        param_info_1.set_name("param_1")
        param_info_1.set_description("param_1 description")
        param_info_1.set_data_type(param_data_type_1)

        param_data_type_2 = BuiltinDataType("float")
        param_info_2 = ParameterDetailInfo()
        param_info_2.set_name("param_2")
        param_info_2.set_description("param_2 description")
        param_info_2.set_data_type(param_data_type_2)

        info.set_parameter_details([param_info_1, param_info_2])

        return_data_type = BuiltinDataType("bool")
        return_info = ReturnInfo()
        return_info.set_description("return description")
        return_info.set_data_type(return_data_type)

        info.set_return(return_info)

        data = {
            "type": "function",
            "name": "function_1",
            "module": "module.a",
            "description": "function_1 description updated",
            "parameters": ["param_1", "param_2", "param_3"],
            "parameter_details": [
                {
                    "type": "parameter",
                    "name": "param_1",
                    "description": "param_1 description updated",
                    "data_type": "float",
                }
            ],
            "return": {
                "type": "return",
                "description": "return description updated",
                "data_type": "custom_data_type",
            }
        }
        info.from_dict(data, method='UPDATE')

        self.assertEqual(info.name(), "function_1")
        self.assertEqual(len(info.parameters()), 3)
        self.assertSetEqual(set(info.parameters()), {"param_1", "param_2", "param_3"})
        self.assertEqual(info.parameter(0), "param_1")
        self.assertEqual(info.parameter(1), "param_2")
        self.assertEqual(info.parameter(2), "param_3")
        self.assertEqual(len(info.parameter_details()), 2)
        self.assertEqual(info.parameter_details()[0].name(), "param_1")
        self.assertEqual(info.parameter_details()[0].description(), "param_1 description updated")
        self.assertEqual(info.parameter_details()[0].data_type().to_string(), "float")
        self.assertEqual(info.parameter_details()[1].name(), "param_2")
        self.assertEqual(info.parameter_details()[1].description(), "param_2 description")
        self.assertEqual(info.parameter_details()[1].data_type().to_string(), "float")
        self.assertEqual(info.module(), "module.a")
        self.assertEqual(info.description(), "function_1 description updated")
        self.assertEqual(info.return_().description(), "return description updated")
        self.assertEqual(info.return_().data_type().to_string(), "custom_data_type")

        expect = {
            "type": "function",
            "name": "function_1",
            "description": "function_1 description updated",
            "class": "",
            "module": "module.a",
            "parameters": ["param_1", "param_2", "param_3"],
            "parameter_details": [
                {
                    "type": "parameter",
                    "name": "param_1",
                    "description": "param_1 description updated",
                    "data_type": "float",
                },
                {
                    "type": "parameter",
                    "name": "param_2",
                    "description": "param_2 description",
                    "data_type": "float",
                }
            ],
            "return": {
                "type": "return",
                "description": "return description updated",
                "data_type": "custom_data_type",
            },
        }
        actual = info.to_dict()
        self.assertDictEqual(expect, actual)


class ClassInfoTest(common.FakeBpyModuleTestBase):

    name = "ClassInfoTest"
    module_name = __module__

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_setter_getter_methods_case_1(self):
        info = ClassInfo()
        info.set_name("ClassA")
        info.set_module("module.a")
        info.set_description("ClassA description")

        attr_data_type_1 = BuiltinDataType("int")
        attr_info_1 = VariableInfo("attribute")
        attr_info_1.set_name("attr_1")
        attr_info_1.set_description("attr_1 description")
        attr_info_1.set_data_type(attr_data_type_1)
        attr_info_1.set_class("ClassA")
        attr_info_1.set_module("module.a")

        attr_data_type_2 = BuiltinDataType("float")
        attr_info_2 = VariableInfo("attribute")
        attr_info_2.set_name("attr_2")
        attr_info_2.set_description("attr_2 description")
        attr_info_2.set_data_type(attr_data_type_2)
        attr_info_2.set_class("ClassA")
        attr_info_2.set_module("module.a")

        info.set_attributes([attr_info_1, attr_info_2])

        method_info_1 = FunctionInfo("method")
        method_info_1.set_name("method_1")
        method_info_1.set_parameters([])
        method_info_1.set_description("method_1 description")
        method_info_1.set_module("module.a")
        method_info_1.set_class("ClassA")

        method_info_2 = FunctionInfo("method")
        method_info_2.set_name("method_2")
        method_info_2.set_parameters([])
        method_info_2.set_description("method_2 description")
        method_info_2.set_module("module.a")
        method_info_2.set_class("ClassA")

        info.set_methods([method_info_1, method_info_2])

        base_class_1 = CustomDataType("BaseClassA")
        base_class_2 = CustomDataType("BaseClassB")

        info.add_base_classes([base_class_1, base_class_2])

        base_class_3 = CustomDataType("BaseClassC")

        info.set_base_class(1, base_class_3)

        self.assertEqual(info.type(), "class")
        self.assertEqual(info.name(), "ClassA")
        self.assertEqual(info.module(), "module.a")
        self.assertEquals(info.attributes(), [attr_info_1, attr_info_2])
        self.assertEqual(info.description(), "ClassA description")
        self.assertEquals(info.methods(), [method_info_1, method_info_2])
        self.assertEquals(info.base_classes(), [base_class_1, base_class_3])

    def test_setter_getter_methods_case_2(self):
        info = ClassInfo()
        info.set_name("ClassA")
        info.set_module("module.a")
        info.set_description("ClassA description")

        info.append_description(" appended")
        info.append_description(" more")

        attr_data_type_1 = BuiltinDataType("int")
        attr_info_1 = VariableInfo("attribute")
        attr_info_1.set_name("attr_1")
        attr_info_1.set_description("attr_1 description")
        attr_info_1.set_data_type(attr_data_type_1)
        attr_info_1.set_class("ClassA")
        attr_info_1.set_module("module.a")

        attr_data_type_2 = BuiltinDataType("float")
        attr_info_2 = VariableInfo("attribute")
        attr_info_2.set_name("attr_2")
        attr_info_2.set_description("attr_2 description")
        attr_info_2.set_data_type(attr_data_type_2)
        attr_info_2.set_class("ClassA")
        attr_info_2.set_module("module.a")

        info.add_attributes([attr_info_1, attr_info_2])

        attr_data_type_3 = BuiltinDataType("bool")
        attr_info_3 = VariableInfo("attribute")
        attr_info_3.set_name("attr_3")
        attr_info_3.set_description("attr_3 description")
        attr_info_3.set_data_type(attr_data_type_3)
        attr_info_3.set_class("ClassA")
        attr_info_3.set_module("module.a")

        info.add_attribute(attr_info_3)

        method_info_1 = FunctionInfo("method")
        method_info_1.set_name("method_1")
        method_info_1.set_parameters([])
        method_info_1.set_description("method_1 description")
        method_info_1.set_module("module.a")
        method_info_1.set_class("ClassA")

        method_info_2 = FunctionInfo("method")
        method_info_2.set_name("method_2")
        method_info_2.set_parameters([])
        method_info_2.set_description("method_2 description")
        method_info_2.set_module("module.a")
        method_info_2.set_class("ClassA")

        info.add_methods([method_info_1, method_info_2])

        method_info_3 = FunctionInfo("method")
        method_info_3.set_name("method_3")
        method_info_3.set_parameters([])
        method_info_3.set_description("method_3 description")
        method_info_3.set_module("module.a")
        method_info_3.set_class("ClassA")

        info.add_method(method_info_3)

        base_class_1 = CustomDataType("BaseClassA")

        info.add_base_class(base_class_1)

        self.assertEqual(info.type(), "class")
        self.assertEqual(info.name(), "ClassA")
        self.assertEqual(info.module(), "module.a")
        self.assertEquals(info.attributes(), [attr_info_1, attr_info_2, attr_info_3])
        self.assertEqual(info.description(), "ClassA description appended more")
        self.assertEquals(info.methods(), [method_info_1, method_info_2, method_info_3])
        self.assertEquals(info.base_classes(), [base_class_1])

    def test_to_dict(self):
        info = ClassInfo()
        info.set_name("ClassA")
        info.set_module("module.a")
        info.set_description("ClassA description")

        attr_data_type_1 = BuiltinDataType("float")
        attr_info_1 = VariableInfo("attribute")
        attr_info_1.set_name("attr_1")
        attr_info_1.set_description("attr_1 description")
        attr_info_1.set_data_type(attr_data_type_1)
        attr_info_1.set_class("ClassA")
        attr_info_1.set_module("module.a")

        info.set_attributes([attr_info_1])

        method_info_1 = FunctionInfo("method")
        method_info_1.set_name("method_1")
        method_info_1.set_parameters(["param_1"])
        method_info_1.set_description("method_1 description")
        method_info_1.set_module("module.a")
        method_info_1.set_class("ClassA")

        param_data_type_1 = BuiltinDataType("int")
        param_info_1 = ParameterDetailInfo()
        param_info_1.set_name("param_1")
        param_info_1.set_description("param_1 description")
        param_info_1.set_data_type(param_data_type_1)
        method_info_1.add_parameter_detail(param_info_1)

        info.set_methods([method_info_1])

        base_class_1 = CustomDataType("BaseClassA")
        base_class_2 = CustomDataType("BaseClassB")

        info.add_base_classes([base_class_1, base_class_2])

        expect = {
            "type": "class",
            "name": "ClassA",
            "description": "ClassA description",
            "module": "module.a",
            "attributes": [
                {
                    "type": "attribute",
                    "name": "attr_1",
                    "description": "attr_1 description",
                    "data_type": "float",
                    "class": "ClassA",
                    "module": "module.a",
                }
            ],
            "methods": [
                {
                    "type": "method",
                    "name": "method_1",
                    "parameters": ["param_1"],
                    "description": "method_1 description",
                    "module": "module.a",
                    "class": "ClassA",
                    "parameter_details": [
                        {
                            "type": "parameter",
                            "name": "param_1",
                            "description": "param_1 description",
                            "data_type": "int",
                        }
                    ],
                    "return": {
                        "type": "return",
                        "data_type": "",
                        "description": "",
                    }
                }
            ],
            "base_classes": ["'BaseClassA'", "'BaseClassB'"]
        }
        actual = info.to_dict()

        self.assertDictEqual(expect, actual)

    def test_from_dict_method_new(self):
        data = {
            "type": "class",
            "name": "ClassA",
            "description": "ClassA description",
            "module": "module.a",
            "base_classes": ["BaseClassA"],
            "attributes": [
                {
                    "type": "attribute",
                    "name": "attr_1",
                    "description": "attr_1 description",
                    "data_type": "int",
                    "class": "ClassA",
                    "module": "module.a",
                }
            ],
            "methods": [
                {
                    "type": "method",
                    "name": "method_1",
                    "parameters": ["param_1"],
                    "description": "method_1 description",
                    "module": "module.a",
                    "parameter_details": [
                        {
                            "type": "parameter",
                            "name": "param_1",
                            "description": "param_1 description",
                            "data_type": "float",
                        }
                    ],
                    "return": {
                        "type": "return",
                        "data_type": "bool",
                        "description": "return description",
                    }
                }
            ]
        }

        info = ClassInfo()
        info.from_dict(data, method='NEW')

        self.assertEqual(info.name(), "ClassA")
        self.assertEqual(info.description(), "ClassA description")
        self.assertEqual(info.module(), "module.a")
        self.assertEqual(len(info.base_classes()), 1)
        self.assertEqual(info.base_classes()[0].to_string(), "BaseClassA")
        self.assertEqual(len(info.attributes()), 1)
        self.assertEqual(info.attributes()[0].name(), "attr_1")
        self.assertEqual(info.attributes()[0].description(), "attr_1 description")
        self.assertEqual(info.attributes()[0].data_type().to_string(), "int")
        self.assertEqual(info.attributes()[0].module(), "module.a")
        self.assertEqual(len(info.methods()), 1)
        self.assertEqual(info.methods()[0].name(), "method_1")
        self.assertEquals(info.methods()[0].parameters(), ["param_1"])
        self.assertEqual(info.methods()[0].description(), "method_1 description")
        self.assertEqual(info.methods()[0].module(), "module.a")
        self.assertEqual(len(info.methods()[0].parameter_details()), 1)
        self.assertEqual(info.methods()[0].parameter_details()[0].name(), "param_1")
        self.assertEqual(info.methods()[0].parameter_details()[0].description(), "param_1 description")
        self.assertEqual(info.methods()[0].parameter_details()[0].data_type().to_string(), "float")
        self.assertEqual(info.methods()[0].return_().description(), "return description")
        self.assertEqual(info.methods()[0].return_().data_type().to_string(), "bool")

    def test_from_dict_method_append(self):
        info = ClassInfo()
        info.set_name("ClassA")
        info.set_module("module.a")
        info.add_base_class(CustomDataType("BaseClassA"))

        attr_info_1 = VariableInfo("attribute")
        attr_info_1.set_name("attr_1")
        attr_info_1.set_class("ClassA")
        attr_info_1.set_module("module.a")

        info.set_attributes([attr_info_1])

        method_info_1 = FunctionInfo("method")
        method_info_1.set_name("method_1")
        method_info_1.set_module("module.a")
        method_info_1.set_class("ClassA")

        info.set_methods([method_info_1])

        data = {
            "type": "class",
            "name": "ClassA",
            "module": "module.a",
            "description": "ClassA description",
            "attributes": [
                {
                    "type": "attribute",
                    "name": "attr_1",
                    "module": "module.a",
                    "class": "ClassA",
                    "description": "attr_1 description",
                    "data_type": "float",
                },
                {
                    "type": "attribute",
                    "name": "attr_2",
                    "module": "module.a",
                    "class": "ClassA",
                    "description": "attr_2 description",
                    "data_type": "int",
                }
            ],
            "methods": [
                {
                    "type": "method",
                    "name": "method_1",
                    "module": "module.a",
                    "class": "ClassA",
                    "description": "method_1 description",
                },
                {
                    "type": "method",
                    "name": "method_2",
                    "module": "module.a",
                    "class": "ClassA",
                    "description": "method_2 description",
                }
            ]
        }
        info.from_dict(data, method='APPEND')

        self.assertEqual(info.name(), "ClassA")
        self.assertEqual(info.description(), "ClassA description")
        self.assertEqual(info.module(), "module.a")
        self.assertEqual(len(info.base_classes()), 1)
        self.assertEqual(info.base_classes()[0].to_string(), "'BaseClassA'")
        self.assertEqual(len(info.attributes()), 2)
        self.assertEqual(info.attributes()[0].name(), "attr_1")
        self.assertEqual(info.attributes()[0].description(), "attr_1 description")
        self.assertEqual(info.attributes()[0].data_type().to_string(), "float")
        self.assertEqual(info.attributes()[0].module(), "module.a")
        self.assertEqual(info.attributes()[1].name(), "attr_2")
        self.assertEqual(info.attributes()[1].description(), "attr_2 description")
        self.assertEqual(info.attributes()[1].data_type().to_string(), "int")
        self.assertEqual(info.attributes()[1].module(), "module.a")
        self.assertEqual(len(info.methods()), 2)
        self.assertEqual(info.methods()[0].name(), "method_1")
        self.assertEquals(info.methods()[0].parameters(), [])
        self.assertEqual(info.methods()[0].description(), "method_1 description")
        self.assertEqual(info.methods()[0].module(), "module.a")
        self.assertEqual(info.methods()[1].name(), "method_2")
        self.assertEquals(info.methods()[1].parameters(), [])
        self.assertEqual(info.methods()[1].description(), "method_2 description")
        self.assertEqual(info.methods()[1].module(), "module.a")

        expect = {
            "type": "class",
            "name": "ClassA",
            "description": "ClassA description",
            "module": "module.a",
            "base_classes": ["'BaseClassA'"],
            "attributes": [
                {
                    "type": "attribute",
                    "name": "attr_1",
                    "description": "attr_1 description",
                    "data_type": "float",
                    "class": "ClassA",
                    "module": "module.a",
                },
                {
                    "type": "attribute",
                    "name": "attr_2",
                    "description": "attr_2 description",
                    "data_type": "int",
                    "class": "ClassA",
                    "module": "module.a",
                }
            ],
            "methods": [
                {
                    "type": "method",
                    "name": "method_1",
                    "module": "module.a",
                    "class": "ClassA",
                    "description": "method_1 description",
                    "parameter_details": [],
                    "parameters": [],
                    "return": {
                        "type": "return",
                        "data_type": "",
                        "description": "",
                    }
                },
                {
                    "type": "method",
                    "name": "method_2",
                    "module": "module.a",
                    "class": "ClassA",
                    "description": "method_2 description",
                    "parameter_details": [],
                    "parameters": [],
                    "return": {
                        "type": "return",
                        "data_type": "",
                        "description": "",
                    }
                }
            ]
        }
        actual = info.to_dict()
        self.assertDictEqual(expect, actual)

    def test_from_dict_method_update(self):
        info = ClassInfo()
        info.set_name("ClassA")
        info.set_module("module.a")
        info.set_description("ClassA description")
        info.add_base_class(CustomDataType("BaseClassA"))

        attr_info_1 = VariableInfo("attribute")
        attr_info_1.set_name("attr_1")
        attr_info_1.set_class("ClassA")
        attr_info_1.set_module("module.a")
        attr_info_1.set_description("attr_1 description")

        info.set_attributes([attr_info_1])

        method_info_1 = FunctionInfo("method")
        method_info_1.set_name("method_1")
        method_info_1.set_module("module.a")
        method_info_1.set_class("ClassA")
        method_info_1.set_description("method_1 description")

        info.set_methods([method_info_1])

        data = {
            "type": "class",
            "name": "ClassA",
            "module": "module.a",
            "description": "ClassA description updated",
            "attributes": [
                {
                    "type": "attribute",
                    "name": "attr_1",
                    "module": "module.a",
                    "class": "ClassA",
                    "description": "attr_1 description updated",
                    "data_type": "float",
                }
            ],
            "methods": [
                {
                    "type": "method",
                    "name": "method_1",
                    "module": "module.a",
                    "class": "ClassA",
                    "description": "method_1 description updated",
                }
            ]
        }
        info.from_dict(data, method='UPDATE')

        self.assertEqual(info.name(), "ClassA")
        self.assertEqual(info.description(), "ClassA description updated")
        self.assertEqual(info.module(), "module.a")
        self.assertEqual(len(info.base_classes()), 1)
        self.assertEqual(info.base_classes()[0].to_string(), "'BaseClassA'")
        self.assertEqual(len(info.attributes()), 1)
        self.assertEqual(info.attributes()[0].name(), "attr_1")
        self.assertEqual(info.attributes()[0].description(), "attr_1 description updated")
        self.assertEqual(info.attributes()[0].data_type().to_string(), "float")
        self.assertEqual(info.attributes()[0].module(), "module.a")
        self.assertEqual(len(info.methods()), 1)
        self.assertEqual(info.methods()[0].name(), "method_1")
        self.assertEquals(info.methods()[0].parameters(), [])
        self.assertEqual(info.methods()[0].description(), "method_1 description updated")
        self.assertEqual(info.methods()[0].module(), "module.a")

        expect = {
            "type": "class",
            "name": "ClassA",
            "description": "ClassA description updated",
            "module": "module.a",
            "base_classes": ["'BaseClassA'"],
            "attributes": [
                {
                    "type": "attribute",
                    "name": "attr_1",
                    "description": "attr_1 description updated",
                    "data_type": "float",
                    "class": "ClassA",
                    "module": "module.a",
                }
            ],
            "methods": [
                {
                    "type": "method",
                    "name": "method_1",
                    "module": "module.a",
                    "class": "ClassA",
                    "description": "method_1 description updated",
                    "parameter_details": [],
                    "parameters": [],
                    "return": {
                        "type": "return",
                        "data_type": "",
                        "description": "",
                    }
                }
            ]
        }
        actual = info.to_dict()
        self.assertDictEqual(expect, actual)


class SectionInfoTest(common.FakeBpyModuleTestBase):

    name = "SectionInfoTest"
    module_name = __module__

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_to_dict(self):
        info = SectionInfo()

        func_info = FunctionInfo("function")
        func_info.set_name("function_1")
        func_info.set_description("function_1 description")
        func_info.set_module("module.a")

        info.add_info(func_info)

        const_info = VariableInfo("constant")
        const_info.set_name("constant_1")
        const_info.set_description("constant_1 description")
        const_info.set_data_type(BuiltinDataType("float"))

        info.add_info(const_info)

        expect = {
            "info_list": [
                {
                    "type": "function",
                    "name": "function_1",
                    "module": "module.a",
                    "class": "",
                    "description": "function_1 description",
                    "parameter_details": [],
                    "parameters": [],
                    "return": {
                        "type": "return",
                        "data_type": "",
                        "description": "",
                    }
                },
                {
                    "type": "constant",
                    "name": "constant_1",
                    "description": "constant_1 description",
                    "data_type": "float",
                    "module": "",
                    "class": "",
                }
            ]
        }

        self.assertDictEqual(expect, info.to_dict())

