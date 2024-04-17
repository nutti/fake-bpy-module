from docutils import nodes

from .transformer_base import TransformerBase
from ..analyzer.nodes import (
    CodeDocumentNode,
    CodeNode,
)
from ..utils import append_child


class RstSpecificNodeCleaner(TransformerBase):

    def _replace(self, from_node: nodes.Node, to_node: nodes.Node):
        parent = from_node.parent
        index = from_node.parent.index(from_node)
        parent.remove(from_node)
        parent.insert(index, to_node)

    def _apply(self, document: nodes.document):
        # Move to the upper node under the section node.
        for section_node in document.traverse(nodes.section):
            parent = section_node.parent
            index = parent.index(section_node)
            for i, child in enumerate(section_node.children[:]):
                parent.insert(index + i + 1, child)
                section_node.remove(child)

        # Make CodeDocumentNode from RST specific nodes.
        for node in document.children[:]:
            if isinstance(node, (
                    nodes.title,
                    nodes.paragraph,
                    nodes.bullet_list,
                    nodes.enumerated_list,
                    nodes.definition_list,
                    nodes.block_quote,
                    nodes.line_block,
                    nodes.literal_block,
                    nodes.section,
                    nodes.field_list,
                    nodes.note,
                    nodes.warning,
                    nodes.target,
                    CodeNode)):
                code_doc_node = CodeDocumentNode()
                self._replace(node, code_doc_node)
                append_child(code_doc_node, node)

    @classmethod
    def name(cls) -> str:
        return "rst_specific_node_cleaner"

    def apply(self, **kwargs):
        for document in self.documents:
            self._apply(document)
