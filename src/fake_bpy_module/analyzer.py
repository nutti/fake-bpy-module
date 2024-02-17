import re
from typing import List, Dict
import json
import copy
from docutils import nodes
from docutils.core import publish_doctree

from .common import (
    BuiltinDataType,
    CustomDataType,
    IntermidiateDataType,
    ModifierDataType,
    ParameterDetailInfo,
    ReturnInfo,
    VariableInfo,
    FunctionInfo,
    ClassInfo,
    SectionInfo,
)
from .utils import (
    output_log,
    LOG_LEVEL_DEBUG,
    LOG_LEVEL_NOTICE,
    LOG_LEVEL_WARN,
)
from .docutils_based import analyzer, transformers, compat, configuration


REGEX_SUB_LINE_SPACES = re.compile(r"\s+")


# pylint: disable=R0903
class AnalysisResult:
    def __init__(self):
        self.section_info: List['SectionInfo'] = []


def _add_getitem_and_setitem_delitem(
        class_info: 'ClassInfo', dtype: str, elem_access_type: str):
    info = FunctionInfo("method")
    info.set_name("__getitem__")
    info.set_parameters(["key"])
    param_detail_info = ParameterDetailInfo()
    param_detail_info.set_name("key")
    param_detail_info.set_description("")
    param_detail_info.set_data_type(IntermidiateDataType(elem_access_type))
    info.set_parameter_details([param_detail_info])
    info.set_class(class_info.name())
    info.set_module(class_info.module())
    return_info = ReturnInfo()
    return_info.set_description("")
    return_info.set_data_type(CustomDataType(dtype, skip_refine=True))
    info.set_return(return_info)
    class_info.add_method(info)

    info = FunctionInfo("method")
    info.set_name("__setitem__")
    info.set_parameters(["key", "value"])
    param_detail_info_key = ParameterDetailInfo()
    param_detail_info_key.set_name("key")
    param_detail_info_key.set_description("")
    param_detail_info_key.set_data_type(IntermidiateDataType(elem_access_type))
    param_detail_info_value = ParameterDetailInfo()
    param_detail_info_value.set_name("value")
    param_detail_info_value.set_description("")
    param_detail_info_value.set_data_type(CustomDataType(
        dtype, skip_refine=True))
    info.set_parameter_details([
        param_detail_info_key, param_detail_info_value])
    info.set_class(class_info.name())
    info.set_module(class_info.module())
    class_info.add_method(info)

    info = FunctionInfo("method")
    info.set_name("__delitem__")
    info.set_parameters(["key"])
    param_detail_info_key = ParameterDetailInfo()
    param_detail_info_key.set_name("key")
    param_detail_info_key.set_description("")
    param_detail_info_key.set_data_type(IntermidiateDataType(elem_access_type))
    info.set_parameter_details([param_detail_info_key])
    info.set_class(class_info.name())
    info.set_module(class_info.module())
    return_info = ReturnInfo()
    return_info.set_description("")
    return_info.set_data_type(CustomDataType(dtype, skip_refine=True))
    info.set_return(return_info)
    class_info.add_method(info)


def _add_iter_next_len(class_info: 'ClassInfo', dtype: str):
    info = FunctionInfo("method")
    info.set_name("__iter__")
    info.set_parameters([])
    info.set_parameter_details([])
    info.set_class(class_info.name())
    info.set_module(class_info.module())
    return_info = ReturnInfo()
    return_info.set_description("")
    return_info.set_data_type(CustomDataType(
        dtype, ModifierDataType("typing.Iterator"), skip_refine=True))
    info.set_return(return_info)
    class_info.add_method(info)

    info = FunctionInfo("method")
    info.set_name("__next__")
    info.set_parameters([])
    info.set_parameter_details([])
    info.set_class(class_info.name())
    info.set_module(class_info.module())
    return_info = ReturnInfo()
    return_info.set_description("")
    return_info.set_data_type(CustomDataType(dtype, skip_refine=True))
    info.set_return(return_info)
    class_info.add_method(info)

    info = FunctionInfo("method")
    info.set_name("__len__")
    info.set_parameters([])
    info.set_parameter_details([])
    info.set_class(class_info.name())
    info.set_module(class_info.module())
    return_info = ReturnInfo()
    return_info.set_description("")
    return_info.set_data_type(BuiltinDataType("int"))
    info.set_return(return_info)
    class_info.add_method(info)


class BaseAnalyzer:
    def __init__(self):
        analyzer.directives.register_directives()
        analyzer.roles.register_roles()

        self.target: str = None         # "blender" or "upbge"
        self.target_version: str = None    # Ex: "2.80"

    def set_target_version(self, version: str):
        self.target_version = version

    def set_target(self, target: str):
        self.target = target

    def _target(self) -> str:
        return self.target

    def _cleanup_string(self, line: str) -> str:
        return REGEX_SUB_LINE_SPACES.sub(
            " ", line.replace(":class:", "").strip()
        )

    def _modify(self, doc_list: List[nodes.document]) -> AnalysisResult:
        result = AnalysisResult()
        for doc in doc_list:
            doc.transformer.add_transform(
                transformers.BaseClassFinder, 1,
                document=doc)
            doc.transformer.add_transform(
                transformers.AttributeToDataTransformer, 2,
                document=doc)
            doc.transformer.apply_transforms()

            section_info: SectionInfo = SectionInfo()
            writer = compat.FakeBpyModuleImmWriter(
                doc, section_info)
            writer.translate()

            result.section_info.append(section_info)

        return result

    def _analyze_by_file(self, filename: str) -> nodes.document:
        with open(filename, "r", encoding="utf-8") as f:
            contents = f.read()

        configuration.set_target(self.target)
        configuration.set_target_version(self.target_version)

        settings_overrides = {
            "exit_status_level": 2,
            "halt_level": 2,
            "line_length_limit": 20000,
        }
        document: nodes.document = publish_doctree(
            contents, settings_overrides=settings_overrides,
            reader=analyzer.readers.BpyRstDocsReader())

        return document

    def analyze_internal(self, filenames: list) -> List[nodes.document]:
        files_to_exclude = []

        documents: List[nodes.document] = []
        for f in filenames:
            exclude = False
            for ex in files_to_exclude:
                if f.endswith(ex):
                    exclude = True
                    break
            if exclude:
                continue

            document = self._analyze_by_file(f)
            documents.append(document)

        return documents

    def analyze(self, filenames: list) -> AnalysisResult:
        documents = self.analyze_internal(filenames)
        result = self._modify(documents)

        return result


class AnalyzerWithModFile(BaseAnalyzer):
    def __init__(self, mod_files: List[str]):
        super().__init__()
        self._mod_files: List[str] = mod_files

    def _modify_with_mod_files(self, result: 'AnalysisResult'):
        for mod_file in self._mod_files:
            self._modify_with_mod_file(mod_file, result)

    def _modify_with_mod_file(self, mod_file: str, result: 'AnalysisResult'):
        with open(mod_file, encoding="utf-8") as f:
            data = json.load(f)

            # Process "remove" field
            #   - Remove item if the same item exists in AnalysisResult.
            if "remove" in data.keys():
                for item in data["remove"]:
                    for section in result.section_info:
                        remove_list = []
                        for info in section.info_list:
                            if ("type" not in item) or \
                                    info.type() != item["type"]:
                                continue
                            if ("name" not in item) or \
                                    info.name() != item["name"]:
                                continue
                            if (("module" in item) and
                                    (info.module() == item["module"])) or \
                               (("module" not in item) and
                                    (info.module() is None)):
                                remove_list.append(info)
                        for rm in remove_list:
                            section.info_list.remove(rm)
                            output_log(
                                LOG_LEVEL_NOTICE,
                                f"{rm.name()} (type={rm.type()}) is removed")

            # Process "new" field
            #   - Add item if the same item doesn't exist in AnalysisResult.
            if "new" in data.keys():
                new_section = SectionInfo()
                for item in data["new"]:

                    # check if entry is already registered
                    has_entry = False
                    for section in result.section_info:
                        for info in section.info_list:
                            if ("type" not in item) or \
                                    info.type() != item["type"]:
                                continue
                            if ("name" not in item) or \
                                    info.name() != item["name"]:
                                continue
                            if ("module" not in item) or \
                                    info.module() != item["module"]:
                                continue
                            has_entry = True
                            break
                        if has_entry:
                            break

                    if not has_entry:
                        if item["type"] == "constant":
                            new_v = VariableInfo("constant")
                            new_v.from_dict(item, 'NEW')
                            new_section.info_list.append(new_v)
                        elif item["type"] == "function":
                            new_f = FunctionInfo("function")
                            new_f.from_dict(item, 'NEW')
                            new_section.info_list.append(new_f)
                        elif item["type"] == "class":
                            new_c = ClassInfo()
                            new_c.from_dict(item, 'NEW')
                            new_section.info_list.append(new_c)
                        else:
                            raise RuntimeError(
                                f"Unsupported Type: {item['type']}")
                    else:
                        output_log(LOG_LEVEL_WARN,
                                   f"{item['name']} is already registered")

                result.section_info.append(new_section)

            # Process "append" field
            #   - Add item's field if the same exists in AnalysisResult.
            #   - Value of item's field must be None.
            if "append" in data.keys():
                for item in data["append"]:
                    for section in result.section_info:
                        for info in section.info_list:
                            if ("type" not in item) or \
                                    info.type() != item["type"]:
                                continue
                            if ("name" not in item) or \
                                    info.name() != item["name"]:
                                continue
                            if ("module" not in item) or \
                                    info.module() != item["module"]:
                                continue
                            info.from_dict(item, 'APPEND')

            # Process "update" field
            #   - Update item's field if the same exists in AnalysisResult.
            #   - Value of item's field can be None or some values.
            if "update" in data.keys():
                for item in data["update"]:
                    for section in result.section_info:
                        for info in section.info_list:
                            if ("type" not in item) or \
                                    info.type() != item["type"]:
                                continue
                            if ("name" not in item) or \
                                    info.name() != item["name"]:
                                continue
                            if ("module" not in item) or \
                                    info.module() != item["module"]:
                                continue
                            info.from_dict(item, 'UPDATE')

    def _modify(self, doc_list: List[nodes.document]) -> AnalysisResult:
        result = super()._modify(doc_list)
        self._modify_with_mod_files(result)

        return result


class BpyModuleAnalyzer(AnalyzerWithModFile):

    def _add_bpy_app_handlers_type(self, result: 'AnalysisResult'):
        for section in result.section_info:
            for info in section.info_list:
                if not re.match(r"^bpy.app.handlers", info.module()):
                    continue
                if info.type() != "constant":
                    continue
                if info.name() == "persistent":
                    continue

                var_info: VariableInfo = info
                var_info.set_data_type(CustomDataType(
                    "bpy.types.Scene", ModifierDataType("listcallable"),
                    modifier_add_info={
                        "arguments": ["bpy.types.Scene"],
                    },
                    skip_refine=True))

    def _add_bpy_ops_override_parameters(self, result: 'AnalysisResult'):
        for section in result.section_info:
            for info in section.info_list:
                if not re.match(r"^bpy.ops", info.module()):
                    continue
                if info.type() != "function":
                    continue

                func_info: 'FunctionInfo' = info

                func_info.add_parameter("override_context=None", 0)
                param_detail = ParameterDetailInfo()
                param_detail.set_name("override_context")
                param_detail.set_data_type(IntermidiateDataType(
                    "dict, bpy.types.Context"))
                func_info.add_parameter_detail(param_detail, 0)

                func_info.add_parameter("execution_context=None", 1)
                param_detail = ParameterDetailInfo()
                param_detail.set_name("execution_context")
                param_detail.set_data_type(IntermidiateDataType("str, int"))
                func_info.add_parameter_detail(param_detail, 1)

                func_info.add_parameter("undo=None", 2)
                param_detail = ParameterDetailInfo()
                param_detail.set_name("undo")
                param_detail.set_data_type(IntermidiateDataType("bool"))
                func_info.add_parameter_detail(param_detail, 2)

                if len(func_info.parameters()) >= 4:
                    func_info.add_parameter("*", 3)

    def _make_bpy_context_variable(self, result: 'AnalysisResult'):
        bpy_context_module_infos: List['VariableInfo'] = []
        bpy_context_class_info: 'ClassInfo' = None
        for section in result.section_info:
            info_list_copied = copy.copy(section.info_list)
            for info in info_list_copied:
                if info.module() == "bpy.context":
                    bpy_context_module_infos.append(info)
                    section.info_list.remove(info)
                if info.module() == "bpy.types" and \
                        info.type() == "class" and info.name() == "Context":
                    bpy_context_class_info = info

        if bpy_context_class_info is None:
            output_log(LOG_LEVEL_WARN, "Failed to find bpy.types.Context")
            return

        attribute_names = [
            attr.name() for attr in bpy_context_class_info.attributes()]
        for info_to_add in bpy_context_module_infos:
            if info_to_add.type() != "constant":
                raise Exception(f"{info_to_add.name()} (module: "
                                f"{info_to_add.module()}) must be constant")
            if info_to_add.name() in attribute_names:
                output_log(LOG_LEVEL_WARN,
                           f"Attribute {info_to_add.name()} has already "
                           "registered in bpy.types.Context")
                continue
            var_info = VariableInfo("attribute")
            var_info.set_name(info_to_add.name())
            var_info.set_module(bpy_context_class_info.module())
            var_info.set_description(info_to_add.description())
            var_info.set_class(bpy_context_class_info.name())
            var_info.set_data_type(info_to_add.data_type())
            bpy_context_class_info.add_attribute(var_info)

        info = VariableInfo("constant")
        info.set_name("context")
        info.set_module("bpy")
        info.set_data_type(IntermidiateDataType("bpy.types.Context"))
        section = SectionInfo()
        section.add_info(info)
        result.section_info.append(section)

    def _change_bpy_types_class_inheritance(self, result: 'AnalysisResult'):
        type_to_class_info = {}
        for section in result.section_info:
            for info in section.info_list:
                if not re.match(r"^bpy.types", info.module()):
                    continue
                if info.type() != "class":
                    continue
                type_to_class_info[info.name()] = info

        parent_to_child = {}
        for class_info in type_to_class_info.values():
            for attr in class_info.attributes():
                m = re.match(
                    r"^`([a-zA-Z0-9]+)` `bpy_prop_collection` of `"
                    r"([a-zA-Z0-9]+)`, \(readonly\)$",
                    attr.data_type().to_string())
                if m:
                    parent_to_child[m.group(1)] = m.group(2)

        for parent, child in parent_to_child.items():
            if parent == child:
                output_log(
                    LOG_LEVEL_WARN, f"Parent and child is same ({parent})")
                continue
            output_log(
                LOG_LEVEL_DEBUG,
                f"Inheritance changed (Parent: {parent}, Child: {child})")
            info = type_to_class_info[parent]
            info.add_base_class(IntermidiateDataType(
                f"`bpy_prop_collection` of `{child}`, (readonly)"))

    def _tweak_bpy_types_classes(self, result: 'AnalysisResult'):
        for section in result.section_info:
            for info in section.info_list:
                if not re.match(r"^bpy.types", info.module()):
                    continue
                if info.type() != "class":
                    continue
                if info.name() in ("bpy_prop_collection", "bpy_prop_array"):
                    # class bpy_prop_collection(Generic[GenericType]):
                    #     def __getitem__(self, key: Union[str, int])
                    #         -> GenericType:
                    #     def __setitem__(self, key: Union[str, int],
                    #                     value: GenericType):
                    #     def __delitem__(self, key: Union[str, int])
                    #         -> GenericType:
                    _add_getitem_and_setitem_delitem(
                        info, "GenericType", "int, str")
                    _add_iter_next_len(info, "GenericType")
                    info.add_base_class(
                        CustomDataType(
                            "GenericType", ModifierDataType("Generic"),
                            skip_refine=True))
                elif info.name() == "bpy_struct":
                    # class bpy_struct():
                    #     def __getitem__(self, key: Union[str, int]) -> Any:
                    #     def __setitem__(self, key: Union[str, int],
                    #                     value: Any):
                    #     def __delitem__(self, key: Union[str, int]) -> Any:
                    _add_getitem_and_setitem_delitem(
                        info, "typing.Any", "int, str")

    def _modify(self, doc_list: List[nodes.document]) -> AnalysisResult:
        result = super()._modify(doc_list)
        self._add_bpy_app_handlers_type(result)
        self._add_bpy_ops_override_parameters(result)
        self._make_bpy_context_variable(result)

        self._change_bpy_types_class_inheritance(result)

        # After this, we could not infer data types as ItermidiateDataType
        self._tweak_bpy_types_classes(result)

        return result


class BmeshModuleAnalyzer(AnalyzerWithModFile):

    def _tweak_bmesh_types_classes(self, result: 'AnalysisResult'):
        seq_to_type: Dict[str, str] = {
            "BMElemSeq": "GenericType",
            "BMVertSeq": "BMVert",
            "BMEdgeSeq": "BMEdge",
            "BMLoopSeq": "BMLoop",
            "BMFaceSeq": "BMFace",
        }

        for section in result.section_info:
            for info in section.info_list:
                if not re.match(r"^bmesh.types", info.module()):
                    continue
                if info.type() != "class":
                    continue
                if info.name() in seq_to_type:
                    _add_getitem_and_setitem_delitem(
                        info, seq_to_type[info.name()], "int")
                    _add_iter_next_len(info, seq_to_type[info.name()])

    def _modify(self, doc_list: List[nodes.document]) -> AnalysisResult:
        result = super()._modify(doc_list)

        # After this, we could not infer data types as ItermidiateDataType
        self._tweak_bmesh_types_classes(result)

        return result
