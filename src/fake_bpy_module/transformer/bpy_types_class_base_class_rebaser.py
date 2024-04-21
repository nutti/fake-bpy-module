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
    make_data_type_node,
)

from ..utils import find_children, get_first_child


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
                    dtype_str = dtype_node.astext()
                    if m := re.match(
                            r"^`([a-zA-Z0-9]+)` `bpy_prop_collection` of `"
                            r"([a-zA-Z0-9]+)`, \(readonly\)$", dtype_str):
                        index = dtype_list_node.index(dtype_node)
                        dtype_list_node.remove(dtype_node)
                        new_dtype_node = make_data_type_node(
                            f"`bpy_prop_collection` of `{m.group(2)}`, (readonly)")
                        new_dtype_node.attributes = dtype_node.attributes
                        dtype_list_node.insert(index, new_dtype_node)

    @classmethod
    def name(cls) -> str:
        return "bpy_types_class_base_class_rebaser"

    def apply(self, **kwargs):
        for document in self.documents:
            self._apply(document)
