from pathlib import Path
from typing import Self

from docutils import nodes

from fake_bpy_module import config
from fake_bpy_module.analyzer.nodes import (
    ModuleNode,
    NameNode,
    SourceFilenameNode,
)
from fake_bpy_module.utils import get_first_child

from .transformer_base import TransformerBase


class ModuleNameFixture(TransformerBase):

    def _no_module(self, document: nodes.document) -> bool:
        module_node = get_first_child(document, ModuleNode)
        if module_node is not None:
            return False

        source_filename = get_first_child(document, SourceFilenameNode).astext()
        if config.get_target() == "upbge":
            if source_filename.startswith("bge.types."):
                module_node = ModuleNode.create_template()
                path = Path(source_filename)
                root = path.parent / path.stem
                module_node.element(NameNode).add_text(str(root))
                document.insert(0, module_node)
                return False

        return True

    @classmethod
    def name(cls: type[Self]) -> str:
        return "module_name_fixture"

    def apply(self, **kwargs: dict) -> None:  # noqa: ARG002
        for document in self.documents[:]:
            if self._no_module(document):
                self.documents.remove(document)
