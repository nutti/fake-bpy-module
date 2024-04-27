import os
from docutils import nodes

from .transformer_base import TransformerBase
from ..analyzer.nodes import (
    ModuleNode,
    SourceFilenameNode,
    NameNode,
)
from ..utils import get_first_child
from .. import configuration


class ModuleNameFixture(TransformerBase):

    def _no_module(self, document: nodes.document):
        module_node = get_first_child(document, ModuleNode)
        if module_node is not None:
            return False

        source_filename = get_first_child(document, SourceFilenameNode).astext()
        if configuration.get_target() == "upbge":
            if source_filename.startswith("bge.types."):
                module_node = ModuleNode.create_template()
                module_node.element(NameNode).add_text(
                    os.path.splitext(os.path.basename(source_filename))[0])
                document.insert(0, module_node)
                return False

        return True

    @classmethod
    def name(cls) -> str:
        return "module_name_fixture"

    def apply(self, **kwargs):
        for document in self.documents[:]:
            if self._no_module(document):
                self.documents.remove(document)
