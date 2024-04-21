import pathlib
from typing import List

from docutils import nodes

from ..analyzer.nodes import (
    TargetFileNode,
)
from ..transformer import transformer
from ..utils import get_first_child

from ..analyzer.analyzer import (
    BaseAnalyzer,
)
from .writers import BaseWriter


class PackageGeneratorConfig:
    def __init__(self):
        self.output_dir: str = "./out"
        self.os: str = "Linux"
        self.style_format: str = "ruff"
        self.dump: bool = False
        self.target: str = "blender"
        self.target_version: str = None
        self.mod_version: str = None
        self.output_format: str = "pyi"


class PackageGenerationRule:
    def __init__(self, name: str, target_files: List[str],
                 analyzer: BaseAnalyzer, generator: BaseWriter):
        self._name: str = name      # Rule
        self._target_files: List[str] = target_files
        self._analyzer: BaseAnalyzer = analyzer
        self._generator: BaseWriter = generator

    def name(self) -> str:
        return self._name

    def target_files(self) -> List[str]:
        return self._target_files

    def analyzer(self) -> BaseAnalyzer:
        return self._analyzer

    def generator(self) -> BaseWriter:
        return self._generator


class PackageAnalyzer:
    def __init__(
            self, config: 'PackageGeneratorConfig',
            rules: List['PackageGenerationRule']):
        self._config: 'PackageGeneratorConfig' = config
        self._rules: List['PackageGenerationRule'] = rules

    def _analyze(self) -> List[nodes.document]:
        result: List[nodes.document] = []
        for rule in self._rules:
            result.extend(self._analyze_by_rule(rule))

        return result

    def _apply_pre_transform(self, documents: List[nodes.document],
                             mod_files: List[str]) -> List[nodes.document]:
        t = transformer.Transformer([
            "first_title_remover",
            "base_class_fixture",
            "rst_specific_node_cleaner",
            "module_level_attribute_fixture",
            "bpy_app_handlers_data_type_adder",
            "bpy_ops_override_parameters_adder",
            "bpy_types_class_base_class_rebaser",
            "bpy_context_variable_converter",
            "mod_applier",
            "format_validator"
        ], {
            "mod_applier": {
                "mod_files": mod_files
            }
        })
        documents = t.transform(documents)

        return documents

    def _analyze_by_rule(
            self, rule: 'PackageGenerationRule') -> List[nodes.document]:
        # replace windows path separator
        target_files = [f.replace("\\", "/") for f in rule.target_files()]
        # analyze all .rst files
        rule.analyzer().set_target(self._config.target)
        rule.analyzer().set_target_version(self._config.target_version)
        documents = rule.analyzer().analyze(target_files)
        documents = self._apply_pre_transform(documents, rule.analyzer().mod_files)

        return documents

    def _apply_post_transform(
            self, documents: List[nodes.document]) -> List[nodes.document]:
        t = transformer.Transformer([
            "target_file_combiner",
            "data_type_refiner",
            "default_value_filler",
            "cannonical_data_type_rewriter",
            "dependency_builder",
            "code_document_refiner",
        ])
        documents = t.transform(documents)

        return documents

    def analyze(self):
        documents = self._analyze()
        self._apply_post_transform(documents)

        return documents


class PackageGenerator:
    def __init__(self, config: 'PackageGeneratorConfig'):
        self._config: 'PackageGeneratorConfig' = config
        self._rules: List['PackageGenerationRule'] = []

    # create module directories/files
    def _create_empty_modules(self, documents: List[nodes.document]):
        for doc in documents:
            target_filename = get_first_child(doc, TargetFileNode).astext()
            dir_path = self._config.output_dir + "/" + target_filename[:target_filename.rfind("/")]
            pathlib.Path(dir_path).mkdir(parents=True, exist_ok=True)
            self._create_py_typed_file(dir_path)

    def _generate(self, rule: PackageGenerationRule, documents: List[nodes.document]):
        for doc in documents:
            # TODO: Move to the generator
            target_filename = get_first_child(doc, TargetFileNode).astext()

            rule.generator().write(
                f"{self._config.output_dir}/{target_filename}", doc,
                self._config.style_format)

    def _create_py_typed_file(self, directory: str):
        filename = f"{directory}/py.typed"
        with open(filename, "w", encoding="utf-8", newline="\n") as file:
            file.write("")

    def add_rule(self, rule: 'PackageGenerationRule'):
        self._rules.append(rule)

    def generate(self):
        analyzer = PackageAnalyzer(self._config, self._rules)
        documents = analyzer.analyze()

        self._create_empty_modules(documents)
        self._generate(self._rules[0], documents)
