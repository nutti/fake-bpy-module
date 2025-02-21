from docutils import nodes

from fake_bpy_module.analyzer.nodes import AttributeNode, DataNode
from fake_bpy_module.utils import append_child, find_children

from .transformer_base import TransformerBase


class ModuleLevelAttributeFixture(TransformerBase):
    def _apply(self, document: nodes.document) -> None:
        attribute_nodes = find_children(document, AttributeNode)

        nodes_to_remove = []
        nodes_to_add = []
        for attr_node in attribute_nodes:
            data_node = DataNode()
            for c in attr_node.children:
                data_node.append_child(c)

            nodes_to_remove.append(attr_node)
            nodes_to_add.append(data_node)

        for node in nodes_to_remove:
            node.parent.remove(node)
        for node in nodes_to_add:
            append_child(document, node)

    @classmethod
    def name(cls) -> str:
        return "module_level_attribute_fixture"

    def apply(self, **kwargs: dict) -> None:  # noqa: ARG002
        for document in self.documents:
            self._apply(document)
