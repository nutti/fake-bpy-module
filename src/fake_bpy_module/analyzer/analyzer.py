import os
import re
from typing import List
from docutils import nodes
from docutils.core import publish_doctree

from . import directives
from . import readers
from . import roles
from .nodes import SourceFilenameNode
from ..utils import output_log, LOG_LEVEL_DEBUG

REGEX_SUB_LINE_SPACES = re.compile(r"\s+")


def analyze(rst_files: List[str]) -> List[nodes.document]:
    rst_files = [f.replace("\\", "/") for f in rst_files]
    analyzer = BaseAnalyzer()
    documents = analyzer.analyze(rst_files)

    return documents


class BaseAnalyzer:
    def __init__(self):
        directives.register_directives()
        roles.register_roles()

        self.mod_documents: List[nodes.document] = []

    def _analyze_by_file(self, filename: str) -> nodes.document:
        output_log(LOG_LEVEL_DEBUG, f"Analyze file: {filename}")
        with open(filename, "r", encoding="utf-8") as f:
            contents = f.read()

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
