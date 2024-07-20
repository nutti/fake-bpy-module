from docutils import nodes

from .base_class_fixture import BaseClassFixture
from .bpy_context_variable_converter import BpyContextVariableConverter
from .bpy_module_tweaker import BpyModuleTweaker
from .cannonical_data_type_rewriter import CannonicalDataTypeRewriter
from .code_document_refiner import CodeDocumentRefiner
from .data_type_refiner import DataTypeRefiner
from .default_value_filler import DefaultValueFiller
from .dependency_builder import DependencyBuilder
from .duplication_remover import DuplicationRemover
from .first_title_remover import FirstTitleRemover
from .format_validator import FormatValidator
from .mod_applier import ModApplier
from .module_level_attribute_fixture import ModuleLevelAttributeFixture
from .module_name_fixture import ModuleNameFixture
from .rst_specific_node_cleaner import RstSpecificNodeCleaner
from .same_module_merger import SameModuleMerger
from .self_rewriter import SelfRewriter
from .target_file_combiner import TargetFileCombiner
from .transformer_base import TransformerBase


def transform(documents: list[nodes.document],
              mod_files: list[str]) -> list[nodes.document]:
    t = Transformer([
        # Must before base_class_fixture
        "module_name_fixture",
        "first_title_remover",
        "rst_specific_node_cleaner",

        "base_class_fixture",

        # Must after base_class_fixture
        "same_module_merger",
        "module_level_attribute_fixture",
        "bpy_module_tweaker",
        "bpy_context_variable_converter",
        "mod_applier",
        "format_validator",

        # Must after mod_applier
        "target_file_combiner",
        "data_type_refiner",

        # Must after data_type_refiner
        "duplication_remover",
        "default_value_filler",
        "cannonical_data_type_rewriter",
        "self_rewriter",
        "dependency_builder",
        "code_document_refiner",
    ], {
        "mod_applier": {
            "mod_files": mod_files
        }
    })

    return t.transform(documents)


class Transformer:
    def __init__(self, transform_kinds: list[str],
                 parameters: dict | None = None) -> None:
        self.transform_kinds: list[str] = transform_kinds
        self.init_parameters: dict = {}
        if parameters is not None:
            self.init_parameters = parameters
        self.transformers: list[TransformerBase] = []

    def get_transformers(self) -> list[TransformerBase]:
        return self.transformers

    def transform(self, documents: list[nodes.document],
                  parameters: dict | None = None) -> list[nodes.document]:
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
            BpyContextVariableConverter.name(): {
                "class": BpyContextVariableConverter,
            },
            BpyModuleTweaker.name(): {
                "class": BpyModuleTweaker,
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
            DuplicationRemover.name(): {
                "class": DuplicationRemover,
            },
            CannonicalDataTypeRewriter.name(): {
                "class": CannonicalDataTypeRewriter,
            },
            CodeDocumentRefiner.name(): {
                "class": CodeDocumentRefiner,
            },
            SameModuleMerger.name(): {
                "class": SameModuleMerger,
            },
            SelfRewriter.name(): {
                "class": SelfRewriter,
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
