import re
from pathlib import Path

from docutils import nodes
from docutils.core import publish_doctree

from fake_bpy_module.utils import LOG_LEVEL_DEBUG, output_log

from . import directives, readers, roles
from .nodes import SourceFilenameNode

REGEX_SUB_LINE_SPACES = re.compile(r"\s+")


def analyze(rst_files: list[str]) -> list[nodes.document]:
    rst_files = [f.replace("\\", "/") for f in rst_files]
    analyzer = BaseAnalyzer()

    return analyzer.analyze(rst_files)


class BaseAnalyzer:
    def __init__(self) -> None:
        directives.register_directives()
        roles.register_roles()

        self.mod_documents: list[nodes.document] = []

    def _analyze_by_file(self, filename: str) -> nodes.document:
        output_log(LOG_LEVEL_DEBUG, f"Analyze file: {filename}")
        with Path(filename).open("r", encoding="utf-8") as f:
            contents = f.read()

        settings_overrides = {
            "exit_status_level": 2,
            "halt_level": 2,
            "line_length_limit": 20000,
        }

        print(f"@@@@@@@ {filename}")

        document: nodes.document = publish_doctree(
            contents, settings_overrides=settings_overrides,
            reader=readers.BpyRstDocsReader())

        document.insert(0, SourceFilenameNode(text=Path(filename).name))

        print(document.pformat())

        return document

    def analyze(self, filenames: list) -> list[nodes.document]:
        documents: list[nodes.document] = []
        for f in filenames:
            document = self._analyze_by_file(f)
            documents.append(document)

        return documents
