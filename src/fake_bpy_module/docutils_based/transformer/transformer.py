from typing import List
from docutils import nodes

from .transformer_base import TransformerBase
from .base_class_fixture import BaseClassFixture
from .bpy_app_handlers_data_type_adder import BpyAppHandlersDataTypeAdder
from .bpy_context_variable_converter import BpyContextVariableConverter
from .bpy_ops_override_parameters_adder import BpyOpsOverrideParameterAdder
from .bpy_types_class_baseclass_rebaser import BpyTypesClassBaseClassRebaser
from .format_validator import FormatValidator
from .mod_applier import ModApplier
from .module_level_attribute_fixture import ModuleLevelAttributeFixture
from .rst_specific_node_cleaner import RstSpecificNodeCleaner

# TODO: set optional flag from parameter description
# TODO: https://github.com/nutti/fake-bpy-module/issues/139
# TODO: test_bge_support_no_module


class Transformer:
    def __init__(self, transform_kinds: List[str], parameters: dict = None):
        self.transform_kinds: List[str] = transform_kinds
        self.init_parameters: dict = {}
        if parameters is not None:
            self.init_parameters = parameters
        self.transformers: List[TransformerBase] = []

    def get_transformers(self) -> List[TransformerBase]:
        return self.transformers

    def transform(self, documents: List[nodes.document],
                  parameters: dict = None):
        transformer_specs = {
            "base_class_fixture": {
                "class": BaseClassFixture,
                "priority": 1,
            },
            "rst_specific_node_cleaner": {
                "class": RstSpecificNodeCleaner,
                "priority": 2,
            },
            "module_level_attribute_fixture": {
                "class": ModuleLevelAttributeFixture,
                "priority": 3,
            },
            "bpy_app_handlers_data_type_adder": {
                "class": BpyAppHandlersDataTypeAdder,
                "priority": 4,
            },
            "bpy_ops_override_parameters_adder": {
                "class": BpyOpsOverrideParameterAdder,
                "priority": 5,
            },
            "bpy_types_class_baseclass_rebaser": {
                "class": BpyTypesClassBaseClassRebaser,
                "priority": 6,
            },
            "bpy_context_variable_converter": {
                "class": BpyContextVariableConverter,
                "priority": 7,
            },
            "mod_applier": {
                "class": ModApplier,
                "priority": 8,
            },
            "format_validator": {
                "class": FormatValidator,
                "priority": 999
            }
        }

        transform_kinds = sorted(
            self.transform_kinds,
            key=lambda kind: transformer_specs[kind]["priority"])

        self.transformers = []
        for kind in transform_kinds:
            spec = transformer_specs[kind]
            init_params = {}
            if kind in self.init_parameters:
                init_params = self.init_parameters[kind]
            apply_params = {}
            if parameters is not None:
                if kind in parameters:
                    apply_params = parameters[kind]
            transformer_class = spec["class"]
            transformer = transformer_class(documents, **init_params)
            transformer.apply(**apply_params)
            self.transformers.append(transformer)

        return documents
