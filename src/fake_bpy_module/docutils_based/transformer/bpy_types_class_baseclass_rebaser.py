import re
from docutils import nodes

from .transformer_base import TransformerBase
from ..analyzer.nodes import (
    DataTypeListNode,
    DataTypeNode,
    ModuleNode,
    NameNode,
    ClassNode,
    AttributeListNode,
    AttributeNode,
)

from ..common import find_children, get_first_child


class BpyTypesClassBaseClassRebaser(TransformerBase):
    def _apply(self, document: nodes.document):
        module_node = get_first_child(document, ModuleNode)
        if module_node is None:
            return

        name_node = module_node.element(NameNode)
        if not name_node.astext().startswith("bpy.types"):
            return

        class_nodes = find_children(document, ClassNode)
        for class_node in class_nodes:
            attr_node_list = class_node.element(AttributeListNode)
            attr_nodes = find_children(attr_node_list, AttributeNode)
            for attr_node in attr_nodes:
                dtype_list_node = attr_node.element(DataTypeListNode)
                dtype_nodes = find_children(dtype_list_node, DataTypeNode)
                for dtype_node in dtype_nodes:
                    text_node = get_first_child(dtype_node, nodes.Text)
                    dtype_str = text_node.astext()
                    if m := re.match(
                            r"^`([a-zA-Z0-9]+)` `bpy_prop_collection` of `"
                            r"([a-zA-Z0-9]+)`, \(readonly\)$", dtype_str):
                        dtype_node.remove(text_node)
                        dtype_node.insert(0, nodes.Text(
                            f"`bpy_prop_collection` of `{m.group(2)}`, "
                            "(readonly)"))

    def apply(self, **kwargs):
        for document in self.documents:
            self._apply(document)
