import os
import re
from typing import List
from docutils import nodes
from docutils.core import publish_doctree

from .. import config
from . import directives
from . import readers
from . import roles
from .nodes import SourceFilenameNode
from ..utils import output_log, LOG_LEVEL_DEBUG
from ..config import PackageGenerationConfig

REGEX_SUB_LINE_SPACES = re.compile(r"\s+")


def analyze(rst_files: List[str], gen_config: PackageGenerationConfig) -> List[nodes.document]:
    rst_files = [f.replace("\\", "/") for f in rst_files]
    analyzer = BaseAnalyzer()
    analyzer.set_target(gen_config.target)
    analyzer.set_target_version(gen_config.target_version)
    documents = analyzer.analyze(rst_files)

    return documents


class BaseAnalyzer:
    def __init__(self):
        directives.register_directives()
        roles.register_roles()

        self.target: str = None         # "blender" or "upbge"
        self.target_version: str = None    # Ex: "2.80"
        self.mod_documents: List[nodes.document] = []

    def set_target_version(self, version: str):
        self.target_version = version

    def set_target(self, target: str):
        self.target = target

    def _target(self) -> str:
        return self.target

    def _analyze_by_file(self, filename: str) -> nodes.document:
        output_log(LOG_LEVEL_DEBUG, f"Analyze file: {filename}")
        with open(filename, "r", encoding="utf-8") as f:
            contents = f.read()

        config.set_target(self.target)
        config.set_target_version(self.target_version)

        settings_overrides = {
            "exit_status_level": 2,
            "halt_level": 2,
            "line_length_limit": 20000,
        }
        document: nodes.document = publish_doctree(
            contents, settings_overrides=settings_overrides,
            reader=readers.BpyRstDocsReader())

        document.insert(0, SourceFilenameNode(text=os.path.basename(filename)))

        return document

    def analyze(self, filenames: list) -> List[nodes.document]:
        documents: List[nodes.document] = []
        for f in filenames:
            document = self._analyze_by_file(f)
            documents.append(document)

        return documents
