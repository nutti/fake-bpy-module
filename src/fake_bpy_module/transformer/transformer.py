from typing import List
from docutils import nodes

from .transformer_base import TransformerBase
from .base_class_fixture import BaseClassFixture
from .bpy_app_handlers_data_type_adder import BpyAppHandlersDataTypeAdder
from .bpy_context_variable_converter import BpyContextVariableConverter
from .bpy_ops_override_parameters_adder import BpyOpsOverrideParameterAdder
from .bpy_types_class_base_class_rebaser import BpyTypesClassBaseClassRebaser
from .cannonical_data_type_rewriter import CannonicalDataTypeRewriter
from .code_document_refiner import CodeDocumentRefiner
from .data_type_refiner import DataTypeRefiner
from .default_value_filler import DefaultValueFiller
from .dependency_builder import DependencyBuilder
from .format_validator import FormatValidator
from .mod_applier import ModApplier
from .module_level_attribute_fixture import ModuleLevelAttributeFixture
from .module_name_fixture import ModuleNameFixture
from .rst_specific_node_cleaner import RstSpecificNodeCleaner
from .target_file_combiner import TargetFileCombiner
from .first_title_remover import FirstTitleRemover


def transform(documents: List[nodes.document], mod_files: List[str]) -> List[nodes.document]:
    t = Transformer([
        "module_name_fixture",
        "first_title_remover",
        "base_class_fixture",
        "rst_specific_node_cleaner",
        "module_level_attribute_fixture",
        "bpy_app_handlers_data_type_adder",
        "bpy_ops_override_parameters_adder",
        "bpy_types_class_base_class_rebaser",
        "bpy_context_variable_converter",
        "mod_applier",
        "format_validator",

        "target_file_combiner",
        "data_type_refiner",
        "default_value_filler",
        "cannonical_data_type_rewriter",
        "dependency_builder",
        "code_document_refiner",
    ], {
        "mod_applier": {
            "mod_files": mod_files
        }
    })
    documents = t.transform(documents)

    return documents


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
            BaseClassFixture.name(): {
                "class": BaseClassFixture,
            },
            RstSpecificNodeCleaner.name(): {
                "class": RstSpecificNodeCleaner,
            },
            ModuleLevelAttributeFixture.name(): {
                "class": ModuleLevelAttributeFixture,
            },
            BpyAppHandlersDataTypeAdder.name(): {
                "class": BpyAppHandlersDataTypeAdder,
            },
            BpyOpsOverrideParameterAdder.name(): {
                "class": BpyOpsOverrideParameterAdder,
            },
            BpyTypesClassBaseClassRebaser.name(): {
                "class": BpyTypesClassBaseClassRebaser,
            },
            BpyContextVariableConverter.name(): {
                "class": BpyContextVariableConverter,
            },
            ModApplier.name(): {
                "class": ModApplier,
            },
            ModuleNameFixture.name(): {
                "class": ModuleNameFixture,
            },
            DataTypeRefiner.name(): {
                "class": DataTypeRefiner,
            },
            DefaultValueFiller.name(): {
                "class": DefaultValueFiller,
            },
            DependencyBuilder.name(): {
                "class": DependencyBuilder,
            },
            CannonicalDataTypeRewriter.name(): {
                "class": CannonicalDataTypeRewriter,
            },
            CodeDocumentRefiner.name(): {
                "class": CodeDocumentRefiner,
            },
            TargetFileCombiner.name(): {
                "class": TargetFileCombiner,
            },
            FirstTitleRemover.name(): {
                "class": FirstTitleRemover,
            },
            FormatValidator.name(): {
                "class": FormatValidator,
            },
        }

        self.transformers = []
        for kind in self.transform_kinds:
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
