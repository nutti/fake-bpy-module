import re
import typing
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
    BaseClassListNode,
    BaseClassNode,
    make_data_type_node,
)

from ..utils import (
    find_children,
    get_first_child,
    output_log,
    LOG_LEVEL_WARN,
    LOG_LEVEL_DEBUG,
)


class BpyTypesClassBaseClassRebaser(TransformerBase):
    def _apply(self, document: nodes.document):
        module_node = get_first_child(document, ModuleNode)
        if module_node is None:
            return

        name_node = module_node.element(NameNode)
        if not name_node.astext().startswith("bpy.types"):
            return

        parent_to_child: typing.Dict[str, str] = {}
        class_name_to_class_node: typing.Dict[str, ClassNode] = {}
        class_nodes = find_children(document, ClassNode)
        for class_node in class_nodes:
            class_name = class_node.element(NameNode).astext()
            class_name_to_class_node[class_name] = class_node

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
                        parent_to_child[m.group(1)] = m.group(2)

        for parent, child in parent_to_child.items():
            if parent == child:
                output_log(
                    LOG_LEVEL_WARN, f"Parent and child is same ({parent})")
                continue
            output_log(
                LOG_LEVEL_DEBUG,
                f"Inheritance changed (Parent: {parent}, Child: {child})")

            class_node = class_name_to_class_node[parent]
            bc_list_node = class_node.element(BaseClassListNode)

            bc_node = BaseClassNode.create_template()
            dtype_list_node = bc_node.element(DataTypeListNode)
            dtype_list_node.append_child(make_data_type_node(
                f"`bpy_prop_collection` of `{child}`, (readonly)"))
            bc_list_node.append_child(bc_node)

    @classmethod
    def name(cls) -> str:
        return "bpy_types_class_base_class_rebaser"

    def apply(self, **kwargs):
        for document in self.documents:
            self._apply(document)
