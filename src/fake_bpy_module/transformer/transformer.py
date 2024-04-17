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
from .dependency_builder import DependencyBuilder
from .format_validator import FormatValidator
from .mod_applier import ModApplier
from .module_level_attribute_fixture import ModuleLevelAttributeFixture
from .rst_specific_node_cleaner import RstSpecificNodeCleaner
from .target_file_combiner import TargetFileCombiner
from .first_title_remover import FirstTitleRemover

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
            DataTypeRefiner.name(): {
                "class": DataTypeRefiner,
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
