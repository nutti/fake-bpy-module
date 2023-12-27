import shutil
import filecmp
import os
import json

from fake_bpy_module.analyzer import (  # pylint: disable=E0401
    BaseAnalyzer,
)
from fake_bpy_module.generator import (     # pylint: disable=E0401
    CodeWriterIndent,
    CodeWriter,
    PyCodeGenerator,
    PyInterfaceGenerator,
    GenerationInfoByTarget,
    GenerationInfoByRule,
    Dependency,
    PackageGeneratorConfig,
    PackageGenerationRule,
    PackageAnalyzer,
    PackageGenerator,
)
from fake_bpy_module.common import (    # pylint: disable=E0401
    DataTypeMetadata,
    BuiltinDataType,
    CustomDataType,
    CustomModifierDataType,
    MixinDataType,
    ModifierDataType,
    VariableInfo,
    FunctionInfo,
    ParameterDetailInfo,
    ReturnInfo,
    ClassInfo,
)
from . import common


class CodeWriterIndentTest(common.FakeBpyModuleTestBase):

    name = "CodeWriterIndentTest"
    module_name = __module__

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


class CodeWriterTest(common.FakeBpyModuleTestBase):

    name = "CodeWriterTest"
    module_name = __module__
    data_dir = os.path.abspath(
        f"{os.path.dirname(__file__)}/generator_test_data")

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

            writer.format(style_config="pep8")
            writer.write(f)

        expect_file_path = f"{self.data_dir}/code_writer_test_normal.py"
        actual_file_path = self.output_file_path
        with open(actual_file_path, "r", encoding="utf-8") as f:
            self.log(f.read())
        self.assertTrue(filecmp.cmp(expect_file_path, actual_file_path))

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

            writer.format(style_config="pep8")
            writer.write(f)

        expect_file_path = \
            f"{self.data_dir}/code_writer_test_with_code_indent.py"
        actual_file_path = self.output_file_path
        with open(actual_file_path, "r", encoding="utf-8") as f:
            self.log(f.read())
        self.assertTrue(filecmp.cmp(expect_file_path, actual_file_path))

    def test_with_reset(self):
        with open(self.output_file_path, "w", newline="\n",
                  encoding="utf-8") as f:
            writer = CodeWriter()

            writer.addln("import fake")
            writer.reset()

            writer.addln("import module_1")

            writer.new_line(2)
            writer.addln("b: bool = False")

            writer.format(style_config="pep8")
            writer.write(f)

        expect_file_path = f"{self.data_dir}/code_writer_test_with_reset.py"
        actual_file_path = self.output_file_path
        with open(actual_file_path, "r", encoding="utf-8") as f:
            self.log(f.read())
        self.assertTrue(filecmp.cmp(expect_file_path, actual_file_path))


class GeneratorsTest(common.FakeBpyModuleTestBase):

    name = "GeneratorsTest"
    module_name = __module__
    data_dir = os.path.abspath(
        f"{os.path.dirname(__file__)}/generator_test_data")

    def setUp(self):
        super().setUp()

        self.output_dir = "fake_bpy_module_test_tmp"
        self.output_file_path = f"{self.output_dir}/generator_test_output"
        os.makedirs(self.output_dir, exist_ok=False)

    def tearDown(self):
        super().tearDown()

        shutil.rmtree(self.output_dir)

    def _create_constant_info(self):
        data_type = BuiltinDataType("int")
        info = VariableInfo("constant")
        info.set_name("constant_1")
        info.set_description("constant_1 description")
        info.set_module("module_1")
        info.set_data_type(data_type)

        return info

    def _create_function_info(self):
        info = FunctionInfo("function")
        info.set_name("function_1")
        info.set_parameters(["param_1=10", "param_2=[]", "param_3=4.5"])
        info.set_description("function_1 description")
        info.set_module("module_1")

        metadata_1 = DataTypeMetadata()
        metadata_1.optional = True
        metadata_1.variable_kind = 'FUNC_ARG'
        metadata_1.default_value = "10"
        metadata_1.never_none = True
        param_data_type_1 = BuiltinDataType("int")
        param_data_type_1.set_metadata(metadata_1)
        param_info_1 = ParameterDetailInfo()
        param_info_1.set_name("param_1")
        param_info_1.set_description("param_1 description")
        param_info_1.set_data_type(param_data_type_1)

        metadata_2 = DataTypeMetadata()
        metadata_2.variable_kind = 'FUNC_ARG'
        metadata_2.default_value = "[]"
        metadata_2.never_none = True
        param_data_type_2 = CustomDataType(
            "ClassA", modifier=ModifierDataType("list"))
        param_data_type_2.set_metadata(metadata_2)
        param_info_2 = ParameterDetailInfo()
        param_info_2.set_name("param_2")
        param_info_2.set_description("param_2 description")
        param_info_2.set_data_type(param_data_type_2)

        metadata_3 = DataTypeMetadata()
        metadata_3.optional = True
        metadata_3.variable_kind = 'FUNC_ARG'
        metadata_3.default_value = "4.5"
        param_data_type_3 = BuiltinDataType("float")
        param_data_type_3.set_metadata(metadata_3)
        param_info_3 = ParameterDetailInfo()
        param_info_3.set_name("param_3")
        param_info_3.set_description("param_3 description")
        param_info_3.set_data_type(param_data_type_3)

        info.set_parameter_details([param_info_1, param_info_2, param_info_3])

        return_data_type = BuiltinDataType("bool")
        return_info = ReturnInfo()
        return_info.set_description("return description")
        return_info.set_data_type(return_data_type)

        info.set_return(return_info)

        return info

    def _create_base_class_1_info(self):
        base_class_info_1 = ClassInfo()
        base_class_info_1.set_name("BaseClassA")
        base_class_info_1.set_module("module_1")
        base_class_info_1.set_description("BaseClassA description")

        return base_class_info_1

    def _create_base_class_2_info(self):
        base_class_info_2 = ClassInfo()
        base_class_info_2.set_name("BaseClassB")
        base_class_info_2.set_module("module_1")
        base_class_info_2.set_description("BaseClassB description")

        return base_class_info_2

    def _create_class_info(self):
        info = ClassInfo()
        info.set_name("ClassA")
        info.set_module("module_1")
        info.set_description("ClassA description")

        data_type_1 = BuiltinDataType("str")
        data_type_2 = CustomDataType(
            "custom_data_type", modifier=ModifierDataType("set"))
        mixin_data_type = MixinDataType([data_type_1, data_type_2])
        attr_info_1 = VariableInfo("attribute")
        attr_info_1.set_name("attr_1")
        attr_info_1.set_description("attr_1 description")
        attr_info_1.set_data_type(mixin_data_type)
        attr_info_1.set_class("ClassA")
        attr_info_1.set_module("module_1")

        info.set_attributes([attr_info_1])

        method_info_1 = FunctionInfo("method")
        method_info_1.set_name("method_1")
        method_info_1.set_parameters(["param_1"])
        method_info_1.set_description("method_1 description")
        method_info_1.set_module("module_1")
        method_info_1.set_class("ClassA")

        metadata = DataTypeMetadata()
        metadata.variable_kind = 'FUNC_ARG'
        metadata.default_value = "0"
        metadata.never_none = True
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

        return info

    def test_generate(self):
        info = GenerationInfoByTarget()

        info.name = "module_1"
        info.data.append(self._create_constant_info())
        info.data.append(self._create_function_info())
        info.data.append(self._create_base_class_1_info())
        info.data.append(self._create_base_class_2_info())
        info.data.append(self._create_class_info())
        info.child_modules.append("submodule_1")

        dep = Dependency()
        dep.mod_name = "module_2"
        dep.add_type("Class1")
        dep.add_type("Class2")
        info.dependencies.append(dep)

        dep = Dependency()
        dep.mod_name = ".submodule_2"
        dep.add_type("ClassZ")
        info.dependencies.append(dep)

        info.external_modules.append("os")

        generator_types = [
            {
                "generator": PyCodeGenerator(),
                "file_ext": "py"
            },
            {
                "generator": PyInterfaceGenerator(),
                "file_ext": "pyi"
            }
        ]

        for type_ in generator_types:
            generator = type_["generator"]
            generator.generate(self.output_file_path, info, "pep8")

            expect_file_path = \
                f"{self.data_dir}/base_generator_test_generate." + \
                f"{type_['file_ext']}"
            actual_file_path = f"{self.output_file_path}.{type_['file_ext']}"
            with open(actual_file_path, "r", encoding="utf-8") as f:
                self.log(f.read())
            self.assertTrue(filecmp.cmp(expect_file_path, actual_file_path))

    def test_generate_custom_modifier(self):
        info = GenerationInfoByTarget()
        info.name = "bpy.types"

        bpy_struct_info = ClassInfo()
        bpy_struct_info.set_name("bpy_prop_collection")
        bpy_struct_info.set_module("bpy.types")
        bpy_struct_info.add_base_class(CustomDataType(
            "GenericType", ModifierDataType("Generic"), skip_refine=True))
        info.data.append(bpy_struct_info)

        attr_info = VariableInfo("attribute")
        attr_info.set_name("attr_1")
        attr_info.set_description("attr_1 description")
        attr_info.set_data_type(CustomDataType(
            "ClassB", CustomModifierDataType("bpy.types.bpy_prop_collection")))
        attr_info.set_class("ClassA")
        attr_info.set_module("bpy.types")

        class_info = ClassInfo()
        class_info.set_name("ClassA")
        class_info.set_module("bpy.types")
        class_info.add_attribute(attr_info)
        info.data.append(class_info)

        dep = Dependency()
        dep.mod_name = "bpy.types"
        dep.add_type("bpy_prop_collection")
        dep.add_type("ClassB")
        info.dependencies.append(dep)

        info.external_modules.append("os")

        generator_types = [
            {
                "generator": PyCodeGenerator(),
                "file_ext": "py"
            },
            {
                "generator": PyInterfaceGenerator(),
                "file_ext": "pyi"
            }
        ]

        for type_ in generator_types:
            generator = type_["generator"]
            generator.generate(self.output_file_path, info, "pep8")

            expect_file_path = \
                f"{self.data_dir}/" + \
                "base_generator_test_generate_custom_modifier." + \
                f"{type_['file_ext']}"
            actual_file_path = f"{self.output_file_path}.{type_['file_ext']}"
            with open(actual_file_path, "r", encoding="utf-8") as f:
                self.log(f.read())
            self.assertTrue(filecmp.cmp(expect_file_path, actual_file_path))

    def test_dump_json(self):
        info = GenerationInfoByTarget()

        info.name = "module_1"
        info.data.append(self._create_constant_info())
        info.data.append(self._create_function_info())
        info.data.append(self._create_base_class_1_info())
        info.data.append(self._create_base_class_2_info())
        info.data.append(self._create_class_info())
        info.child_modules.append("submodule_1")

        dep = Dependency()
        dep.mod_name = "module_2"
        dep.add_type("Class1")
        dep.add_type("Class2")
        info.dependencies.append(dep)

        dep = Dependency()
        dep.mod_name = ".submodule_2"
        dep.add_type("ClassZ")
        info.dependencies.append(dep)

        info.external_modules.append("os")

        generator = PyCodeGenerator()
        generator.dump_json(self.output_file_path, info)

        expect_file_path = \
            f"{self.data_dir}/base_generator_test_dump_json.json"
        with open(expect_file_path, "r", encoding="utf-8") as f:
            expect_data = {"data": json.load(f)}
        actual_file_path = self.output_file_path
        with open(actual_file_path, "r", encoding="utf-8") as f:
            actual_data = {"data": json.load(f)}
        self.assertDictEqual(expect_data, actual_data)

    def test_pre_process(self):
        info = GenerationInfoByTarget()

        info.name = "module_1"
        info.data.append(self._create_constant_info())
        info.data.append(self._create_function_info())
        info.data.append(self._create_base_class_1_info())
        info.data.append(self._create_base_class_2_info())
        info.data.append(self._create_class_info())
        info.child_modules.append("submodule_1")

        dep = Dependency()
        dep.mod_name = "module_2"
        dep.add_type("Class1")
        dep.add_type("Class2")
        info.dependencies.append(dep)

        dep = Dependency()
        dep.mod_name = ".submodule_2"
        dep.add_type("ClassZ")
        info.dependencies.append(dep)

        info.external_modules.append("os")

        generator = PyCodeGenerator()
        processed_info = generator.pre_process("module_1", info)

        self.assertEqual(info.name, processed_info.name)
        self.assertEqual(info.child_modules, processed_info.child_modules)
        self.assertEqual(info.dependencies, processed_info.dependencies)
        self.assertEqual(
            info.external_modules, processed_info.external_modules)
        self.assertEqual(info.data, processed_info.data)


class DependencyTest(common.FakeBpyModuleTestBase):

    name = "DependencyTest"
    module_name = __module__

    def test_all(self):
        dep = Dependency()

        dep.mod_name = "module_1"
        dep.add_type("ClassA")
        dep.add_type("ClassB")

        self.assertEqual(dep.mod_name, "module_1")
        self.assertEqual(len(dep.type_lists), 2)
        self.assertEqual(dep.type_lists, ["ClassA", "ClassB"])


class GenerationInfoByTargetTest(common.FakeBpyModuleTestBase):

    name = "GenerationInfoByTargetTest"
    module_name = __module__

    def _create_constant_info(self):
        data_type = BuiltinDataType("int")
        info = VariableInfo("constant")
        info.set_name("constant_1")
        info.set_description("constant_1 description")
        info.set_module("module_1")
        info.set_data_type(data_type)

        return info

    def test_all(self):
        info = GenerationInfoByTarget()

        info.name = "module_1"
        info.child_modules.append("submodule_1")
        info.child_modules.append("submodule_2")

        constant_info = self._create_constant_info()
        info.data.append(constant_info)

        dep_1 = Dependency()
        dep_1.mod_name = "module_1"
        dep_1.add_type("Class1")
        dep_1.add_type("Class2")
        info.dependencies.append(dep_1)

        dep_2 = Dependency()
        dep_2.mod_name = "module_2"
        dep_2.add_type("ClassZ")
        info.dependencies.append(dep_2)

        info.external_modules.append("os")

        self.assertEqual(info.name, "module_1")
        self.assertEqual(info.child_modules, ["submodule_1", "submodule_2"])
        self.assertEqual(info.data, [constant_info])
        self.assertEqual(info.dependencies, [dep_1, dep_2])
        self.assertEqual(info.external_modules, ["sys", "typing", "os"])


class GenerationInfoByRuleTest(common.FakeBpyModuleTestBase):

    name = "GenerationInfoByRuleTest"
    module_name = __module__

    def test_all(self):
        info = GenerationInfoByRule()

        with self.assertRaises(RuntimeError):
            info.get_target("target_1")

        target_1 = info.get_or_create_target("target_1")
        self.assertEqual(info.get_target("target_1"), target_1)
        self.assertEqual(info.get_or_create_target("target_1"), target_1)

        target_2 = info.create_target("target_2/__init__")
        self.assertEqual(info.get_target("target_2/__init__"), target_2)
        self.assertEqual(
            info.get_or_create_target("target_2/__init__"), target_2)

        target_3 = info.create_target("target_2/sub")
        info.update_target("target_2/sub", target_3)
        self.assertEqual(info.get_target("target_2/sub"), target_3)

        self.assertEqual(
            list(info.targets()),
            ["target_1", "target_2/__init__", "target_2/sub"])


class PackageGeneratorConfigTest(common.FakeBpyModuleTestBase):

    name = "PackageGeneratorConfigTest"
    module_name = __module__

    def test_all(self):
        config = PackageGeneratorConfig()

        config.output_dir = "./test"
        config.os = "Windows"
        config.style_format = "none"
        config.dump = True
        config.target = "upbge"
        config.target_version = "2.80"
        config.mod_version = "2.80"

        self.assertEqual(config.output_dir, "./test")
        self.assertEqual(config.os, "Windows")
        self.assertEqual(config.style_format, "none")
        self.assertTrue(config.dump)
        self.assertEqual(config.target, "upbge")
        self.assertEqual(config.target_version, "2.80")
        self.assertEqual(config.mod_version, "2.80")


class PackageGenerationRuleTest(common.FakeBpyModuleTestBase):

    name = "PackageGenerationRuleTest"
    module_name = __module__

    def test_all(self):
        analyzer = BaseAnalyzer()
        generator = PyCodeGenerator()

        rule = PackageGenerationRule(
            "rule", ["a.rst", "b.rst"], analyzer, generator)

        self.assertEqual(rule.name(), "rule")
        self.assertEqual(rule.target_files(), ["a.rst", "b.rst"])
        self.assertEqual(rule.analyzer(), analyzer)
        self.assertEqual(rule.generator(), generator)


class PackageAnalyzerTest(common.FakeBpyModuleTestBase):

    name = "PackageAnalyzerTest"
    module_name = __module__
    data_dir = os.path.abspath(
        f"{os.path.dirname(__file__)}/generator_test_data")

    def setUp(self):
        super().setUp()

        self.output_base_dir = "fake_bpy_module_test_tmp"
        self.output_dir = f"{self.output_base_dir}/output"
        os.makedirs(self.output_dir, exist_ok=False)

    def tearDown(self):
        super().tearDown()

        shutil.rmtree(self.output_base_dir)

    def test_single_rule(self):
        rule_rst_files = [
            f"{self.data_dir}/package_analyzer_test_single_rule.rst",
        ]

        config = PackageGeneratorConfig()
        config.output_dir = self.output_dir
        config.os = "Linux"
        config.style_format = "none"
        config.dump = True
        config.target = "blender"
        config.target_version = "2.80"
        config.mod_version = "2.80"

        analyzer = BaseAnalyzer()
        generator = PyCodeGenerator()
        rule = PackageGenerationRule("rule", rule_rst_files,
                                     analyzer, generator)

        pkg_analyzer = PackageAnalyzer(config, [rule])
        pkg_analyzer.analyze()

        pkg_struct = pkg_analyzer.package_structure()
        self.assertDictEqual(pkg_struct.to_dict(), {
            "name": None,
            "children": [
                {
                    "name": "module_abc",
                    "children": [],
                }
            ]
        })

        entries = pkg_analyzer.entry_points()
        actual_entries = {e.fullname() for e in entries}
        expect_entries = {
            "module_abc.Class123",
        }
        self.assertSetEqual(expect_entries, actual_entries)

        gen_info = pkg_analyzer.generation_info()
        self.assertEqual(len(gen_info.keys()), 1)
        actual_rule = None
        actual_gen_info = None
        for k in gen_info.keys():
            if k.name() == "rule":
                actual_rule = k
                actual_gen_info = gen_info[k]
        self.assertIsNotNone(actual_rule)
        self.assertIsNotNone(actual_gen_info)

        self.assertEqual(
            set(actual_gen_info.targets()), {"module_abc/__init__"})

        target_module_abc = actual_gen_info.get_target(
            "module_abc/__init__")
        self.assertEqual(len(target_module_abc.data), 1)
        self.assertEqual(target_module_abc.data[0].type(), "class")
        self.assertEqual(target_module_abc.data[0].name(), "Class123")
        self.assertEqual(len(target_module_abc.child_modules), 0)
        self.assertEqual(len(target_module_abc.dependencies), 0)

    def test_multiple_rules(self):
        rule_1_rst_files = [
            f"{self.data_dir}/package_analyzer_test_multiple_rules_1_a.rst",
            f"{self.data_dir}/package_analyzer_test_multiple_rules_1_b.rst",
        ]
        rule_2_rst_files = [
            f"{self.data_dir}/package_analyzer_test_multiple_rules_2.rst",
        ]

        config = PackageGeneratorConfig()
        config.output_dir = f"{self.output_dir}/output"
        config.os = "Linux"
        config.style_format = "none"
        config.dump = True
        config.target = "blender"
        config.target_version = "2.80"
        config.mod_version = None

        analyzer = BaseAnalyzer()
        generator = PyCodeGenerator()
        rule_1 = PackageGenerationRule("rule_1", rule_1_rst_files,
                                       analyzer, generator)

        analyzer = BaseAnalyzer()
        generator = PyCodeGenerator()
        rule_2 = PackageGenerationRule("rule_2", rule_2_rst_files,
                                       analyzer, generator)

        pkg_analyzer = PackageAnalyzer(config, [rule_1, rule_2])
        pkg_analyzer.analyze()

        pkg_struct = pkg_analyzer.package_structure()
        self.assertDictEqual(pkg_struct.to_dict(), {
            "name": None,
            "children": [
                {
                    "name": "module_1",
                    "children": [
                        {
                            "name": "submodule_1",
                            "children": [],
                        }
                    ]
                },
                {
                    "name": "module_2",
                    "children": [],
                }
            ]
        })

        entries = pkg_analyzer.entry_points()
        actual_entries = {e.fullname() for e in entries}
        expect_entries = {
            "module_1.ClassA",
            "module_1.submodule_1.BaseClass1",
            "module_1.submodule_1.function_1",
            "module_1.submodule_1.DATA_1",
            "module_2.function_1",
        }
        self.assertSetEqual(expect_entries, actual_entries)

        gen_info = pkg_analyzer.generation_info()
        self.assertEqual(len(gen_info.keys()), 2)
        actual_rule_1 = None
        actual_rule_2 = None
        actual_gen_info_1 = None
        actual_gen_info_2 = None
        for k in gen_info.keys():
            if k.name() == "rule_1":
                actual_rule_1 = k
                actual_gen_info_1 = gen_info[k]
            elif k.name() == "rule_2":
                actual_rule_2 = k
                actual_gen_info_2 = gen_info[k]
        self.assertIsNotNone(actual_rule_1)
        self.assertIsNotNone(actual_rule_2)
        self.assertIsNotNone(actual_gen_info_1)
        self.assertIsNotNone(actual_gen_info_2)

        self.assertEqual(
            set(actual_gen_info_1.targets()),
            {"module_1/__init__", "module_1/submodule_1/__init__"})
        self.assertEqual(
            set(actual_gen_info_2.targets()), {"module_2/__init__"})

        target_module_1 = actual_gen_info_1.get_target("module_1/__init__")
        self.assertEqual(len(target_module_1.data), 1)
        self.assertEqual(target_module_1.data[0].type(), "class")
        self.assertEqual(target_module_1.data[0].name(), "ClassA")
        self.assertEqual(target_module_1.child_modules, ["submodule_1"])
        self.assertEqual(len(target_module_1.dependencies), 1)
        self.assertEqual(
            target_module_1.dependencies[0].mod_name, "module_1.submodule_1")
        self.assertEqual(
            target_module_1.dependencies[0].type_lists, ["BaseClass1"])

        target_module_1_submodule_1 = actual_gen_info_1.get_target(
            "module_1/submodule_1/__init__")
        self.assertEqual(len(target_module_1_submodule_1.data), 3)
        self.assertEqual(target_module_1_submodule_1.data[0].type(), "class")
        self.assertEqual(
            target_module_1_submodule_1.data[0].name(), "BaseClass1")
        self.assertEqual(
            target_module_1_submodule_1.data[1].type(), "function")
        self.assertEqual(
            target_module_1_submodule_1.data[1].name(), "function_1")
        self.assertEqual(
            target_module_1_submodule_1.data[2].type(), "constant")
        self.assertEqual(target_module_1_submodule_1.data[2].name(), "DATA_1")
        self.assertEqual(len(target_module_1_submodule_1.child_modules), 0)
        self.assertEqual(len(target_module_1_submodule_1.dependencies), 0)

        target_module_2 = actual_gen_info_2.get_target("module_2/__init__")
        self.assertEqual(len(target_module_2.data), 1)
        self.assertEqual(target_module_2.data[0].type(), "function")
        self.assertEqual(target_module_2.data[0].name(), "function_1")
        self.assertEqual(len(target_module_2.child_modules), 0)
        self.assertEqual(len(target_module_2.dependencies), 2)
        self.assertEqual(target_module_2.dependencies[0].mod_name, "module_1")
        self.assertEqual(
            target_module_2.dependencies[0].type_lists, ["ClassA"])
        self.assertEqual(
            target_module_2.dependencies[1].mod_name, "module_1.submodule_1")
        self.assertEqual(
            target_module_2.dependencies[1].type_lists, ["BaseClass1"])

    def test_exceptional_rule(self):
        rule_rst_files = [
            f"{self.data_dir}/package_analyzer_test_exceptional_rule.rst",
        ]

        config = PackageGeneratorConfig()
        config.output_dir = self.output_dir
        config.os = "Linux"
        config.style_format = "none"
        config.dump = True
        config.target = "blender"
        config.target_version = "2.80"
        config.mod_version = None

        analyzer = BaseAnalyzer()
        generator = PyCodeGenerator()
        rule = PackageGenerationRule("rule", rule_rst_files,
                                     analyzer, generator)

        pkg_analyzer = PackageAnalyzer(config, [rule])
        pkg_analyzer.analyze()

        pkg_struct = pkg_analyzer.package_structure()
        self.assertDictEqual(pkg_struct.to_dict(), {
            "name": None,
            "children": [
                {
                    "name": "module_exceptional",
                    "children": [],
                }
            ]
        })

        entries = pkg_analyzer.entry_points()
        actual_entries = {e.fullname() for e in entries}
        expect_entries = {
            "module_exceptional.ClassExp",
            "module_exceptional.function_with_type_hint",
        }
        self.assertSetEqual(expect_entries, actual_entries)

        gen_info = pkg_analyzer.generation_info()
        self.assertEqual(len(gen_info.keys()), 1)
        actual_rule = None
        actual_gen_info = None
        for k in gen_info.keys():
            if k.name() == "rule":
                actual_rule = k
                actual_gen_info = gen_info[k]
        self.assertIsNotNone(actual_rule)
        self.assertIsNotNone(actual_gen_info)

        self.assertEqual(
            set(actual_gen_info.targets()), {"module_exceptional/__init__"})

        target_module_abc = actual_gen_info.get_target(
            "module_exceptional/__init__")
        self.assertEqual(len(target_module_abc.data), 2)
        self.assertEqual(target_module_abc.data[0].type(), "class")
        self.assertEqual(target_module_abc.data[0].name(), "ClassExp")
        self.assertEqual(target_module_abc.data[1].type(), "function")
        self.assertEqual(
            target_module_abc.data[1].name(), "function_with_type_hint")
        self.assertEqual(len(target_module_abc.child_modules), 0)
        self.assertEqual(len(target_module_abc.dependencies), 0)


class PackageGeneratorTest(common.FakeBpyModuleTestBase):

    name = "PackageGeneratorTest"
    module_name = __module__
    data_dir = os.path.abspath(
        f"{os.path.dirname(__file__)}/generator_test_data")

    def setUp(self):
        super().setUp()

        self.output_base_dir = "fake_bpy_module_test_tmp"
        self.output_dir = f"{self.output_base_dir}/output"
        os.makedirs(self.output_dir, exist_ok=False)

    def tearDown(self):
        super().tearDown()

        shutil.rmtree(self.output_base_dir)

    def __is_py_typed_exist(self, filepath: str) -> bool:
        if not os.path.isfile(filepath):
            return False
        return os.path.getsize(filepath) == 0

    def test_single_rules(self):
        rule_rst_files = [
            f"{self.data_dir}/package_analyzer_test_single_rule.rst",
        ]

        config = PackageGeneratorConfig()
        config.output_dir = self.output_dir
        config.os = "Linux"
        config.style_format = "pep8"
        config.dump = True
        config.target = "blender"
        config.target_version = "2.80"
        config.mod_version = "2.80"

        pkg_generator = PackageGenerator(config)

        analyzer = BaseAnalyzer()
        generator = PyCodeGenerator()
        rule = PackageGenerationRule(
            "rule", rule_rst_files, analyzer, generator)

        pkg_generator.add_rule(rule)
        pkg_generator.generate()

        expect_files_dir = \
            f"{self.data_dir}/package_generator_test_single_rule"
        actual_files_dir = self.output_dir

        py_files = [
            "module_abc/__init__.py",
        ]
        for file_ in py_files:
            expect_file_path = f"{expect_files_dir}/{file_}"
            actual_file_path = f"{actual_files_dir}/{file_}"
            with open(actual_file_path, "r", encoding="utf-8") as f:
                self.log(f"============= {actual_file_path} =============")
                self.log(f.read())
            self.assertTrue(filecmp.cmp(expect_file_path, actual_file_path))

        json_files = [
            "module_abc/__init__-dump.json",
        ]
        for file_ in json_files:
            expect_file_path = f"{expect_files_dir}/{file_}"
            actual_file_path = f"{actual_files_dir}/{file_}"
            with open(expect_file_path, "r", encoding="utf-8") as f:
                expect_json = {"data": json.load(f)}
            with open(actual_file_path, "r", encoding="utf-8") as f:
                self.log(f"============= {actual_file_path} =============")
                data = json.load(f)
                self.log(str(data))
                actual_json = {"data": data}
            self.assertDictEqual(expect_json, actual_json)

        self.assertFalse(self.__is_py_typed_exist(
            f"{self.output_dir}/py.typed"))

    def test_multiple_rules(self):
        rule_1_rst_files = [
            f"{self.data_dir}/package_analyzer_test_multiple_rules_1_a.rst",
            f"{self.data_dir}/package_analyzer_test_multiple_rules_1_b.rst",
        ]
        rule_2_rst_files = [
            f"{self.data_dir}/package_analyzer_test_multiple_rules_2.rst",
        ]

        config = PackageGeneratorConfig()
        config.output_dir = self.output_dir
        config.os = "Linux"
        config.style_format = "pep8"
        config.dump = True
        config.target = "blender"
        config.target_version = "2.80"
        config.mod_version = None

        pkg_generator = PackageGenerator(config)

        analyzer = BaseAnalyzer()
        generator = PyCodeGenerator()
        rule_1 = PackageGenerationRule("rule_1", rule_1_rst_files,
                                       analyzer, generator)

        analyzer = BaseAnalyzer()
        generator = PyCodeGenerator()
        rule_2 = PackageGenerationRule("rule_2", rule_2_rst_files,
                                       analyzer, generator)

        pkg_generator.add_rule(rule_1)
        pkg_generator.add_rule(rule_2)
        pkg_generator.generate()

        expect_files_dir = \
            f"{self.data_dir}/package_generator_test_multiple_rules"
        actual_files_dir = self.output_dir

        py_files = [
            "module_1/__init__.py",
            "module_1/submodule_1/__init__.py",
            "module_2/__init__.py",
        ]
        for file_ in py_files:
            expect_file_path = f"{expect_files_dir}/{file_}"
            actual_file_path = f"{actual_files_dir}/{file_}"
            with open(actual_file_path, "r", encoding="utf-8") as f:
                self.log(f"============= {actual_file_path} =============")
                self.log(f.read())
            self.assertTrue(filecmp.cmp(expect_file_path, actual_file_path))

        json_files = [
            "module_1/__init__-dump.json",
            "module_1/submodule_1/__init__-dump.json",
            "module_2/__init__-dump.json",
        ]
        for file_ in json_files:
            expect_file_path = f"{expect_files_dir}/{file_}"
            actual_file_path = f"{actual_files_dir}/{file_}"
            with open(expect_file_path, "r", encoding="utf-8") as f:
                expect_json = {"data": json.load(f)}
            with open(actual_file_path, "r", encoding="utf-8") as f:
                self.log(f"============= {actual_file_path} =============")
                data = json.load(f)
                self.log(str(data))
                actual_json = {"data": data}
            self.assertDictEqual(expect_json, actual_json)

        self.assertFalse(self.__is_py_typed_exist(
            f"{self.output_dir}/py.typed"))

        py_typed_filepath = f"{self.output_dir}/module_1/py.typed"
        self.assertTrue(self.__is_py_typed_exist(py_typed_filepath))

    def test_exceptional_rules(self):
        rule_rst_files = [
            f"{self.data_dir}/package_analyzer_test_exceptional_rule.rst",
        ]

        config = PackageGeneratorConfig()
        config.output_dir = self.output_dir
        config.os = "Linux"
        config.style_format = "pep8"
        config.dump = True
        config.target = "blender"
        config.target_version = "2.80"
        config.mod_version = None

        pkg_generator = PackageGenerator(config)

        analyzer = BaseAnalyzer()
        generator = PyCodeGenerator()
        rule = PackageGenerationRule(
            "rule", rule_rst_files, analyzer, generator)

        pkg_generator.add_rule(rule)
        pkg_generator.generate()

        expect_files_dir = \
            f"{self.data_dir}/package_generator_test_exceptional_rule"
        actual_files_dir = self.output_dir

        py_files = [
            "module_exceptional/__init__.py",
        ]
        for file_ in py_files:
            expect_file_path = f"{expect_files_dir}/{file_}"
            actual_file_path = f"{actual_files_dir}/{file_}"
            with open(actual_file_path, "r", encoding="utf-8") as f:
                self.log(f"============= {actual_file_path} =============")
                self.log(f.read())
            self.assertTrue(filecmp.cmp(expect_file_path, actual_file_path))

        json_files = [
            "module_exceptional/__init__-dump.json",
        ]
        for file_ in json_files:
            expect_file_path = f"{expect_files_dir}/{file_}"
            actual_file_path = f"{actual_files_dir}/{file_}"
            with open(expect_file_path, "r", encoding="utf-8") as f:
                expect_json = {"data": json.load(f)}
            with open(actual_file_path, "r", encoding="utf-8") as f:
                self.log(f"============= {actual_file_path} =============")
                data = json.load(f)
                self.log(str(data))
                actual_json = {"data": data}
            self.assertDictEqual(expect_json, actual_json)

        self.assertFalse(self.__is_py_typed_exist(
            f"{self.output_dir}/py.typed"))
