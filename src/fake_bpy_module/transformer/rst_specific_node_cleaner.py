from typing import Self

from docutils import nodes

from fake_bpy_module.analyzer.nodes import CodeDocumentNode, CodeNode
from fake_bpy_module.utils import append_child

from .transformer_base import TransformerBase


class RstSpecificNodeCleaner(TransformerBase):

    def _replace(self, from_node: nodes.Node, to_node: nodes.Node) -> None:
        parent = from_node.parent
        index = from_node.parent.index(from_node)
        parent.remove(from_node)
        parent.insert(index, to_node)

    def _apply(self, document: nodes.document) -> None:
        # Move to the upper node under the section node.
        for section_node in document.traverse(nodes.section):
            parent = section_node.parent
            index = parent.index(section_node)
            for i, child in enumerate(section_node.children[:]):
                parent.insert(index + i + 1, child)
                section_node.remove(child)

        # Make CodeDocumentNode from RST specific nodes.
        for node in document.children[:]:
            if isinstance(
                    node, nodes.title | nodes.paragraph | nodes.bullet_list |
                    nodes.enumerated_list | nodes.definition_list |
                    nodes.block_quote | nodes.line_block | nodes.literal_block |
                    nodes.section | nodes.field_list | nodes.note |
                    nodes.warning | nodes.target | CodeNode):
                code_doc_node = CodeDocumentNode()
                self._replace(node, code_doc_node)
                append_child(code_doc_node, node)

    @classmethod
    def name(cls: type[Self]) -> str:
        return "rst_specific_node_cleaner"

    def apply(self, **kwargs: dict) -> None:  # noqa: ARG002
        for document in self.documents:
            self._apply(document)
