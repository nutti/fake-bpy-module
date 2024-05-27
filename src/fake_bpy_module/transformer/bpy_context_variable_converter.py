from docutils import nodes

from .transformer_base import TransformerBase
from ..analyzer.nodes import (
    ModuleNode,
    NameNode,
    ClassNode,
    DataNode,
    DataTypeListNode,
    AttributeListNode,
    AttributeNode,
    make_data_type_node,
)
from ..utils import append_child, get_first_child, find_children, output_log, LOG_LEVEL_WARN


# TODO: Move to BpyModuleTweaker.
class BpyContextVariableConverter(TransformerBase):
    @classmethod
    def name(cls) -> str:
        return "bpy_context_variable_converter"

    def apply(self, **kwargs):
        bpy_module_document: nodes.document = None
        bpy_context_module_document: nodes.document = None
        bpy_context_class_node: ClassNode = None
        for document in self.documents:
            if (bpy_module_document is not None and
                    bpy_context_module_document is not None and
                    bpy_context_class_node is not None):
                break

            module_node = get_first_child(document, ModuleNode)
            if module_node is None:
                continue

            module_name_node = module_node.element(NameNode)
            if module_name_node.astext() == "bpy":
                bpy_module_document = document
            elif module_name_node.astext() == "bpy.context":
                bpy_context_module_document = document
            elif module_name_node.astext() == "bpy.types":
                class_nodes = find_children(document, ClassNode)
                for class_node in class_nodes:
                    class_name_node = class_node.element(NameNode)
                    if class_name_node.astext() == "Context":
                        bpy_context_class_node = class_node
                        break

        if bpy_module_document is None:
            output_log(LOG_LEVEL_WARN, "Failed to find bpy module")
            return

        if bpy_context_module_document is None:
            output_log(LOG_LEVEL_WARN, "Failed to find bpy.context module")
            return

        if bpy_context_class_node is None:
            output_log(LOG_LEVEL_WARN, "Failed to find bpy.types.Context class")
            return

        # Remove the bpy.context module document.
        self.documents.remove(bpy_context_module_document)

        # Move all data nodes to the bpy.types.Context class node.
        data_nodes = find_children(bpy_context_module_document, DataNode)
        attr_list_node = bpy_context_class_node.element(AttributeListNode)
        for data_node in data_nodes:
            attr_node = AttributeNode()
            for c in data_node.children:
                attr_node.append_child(c)
            attr_list_node.append_child(attr_node)

        # Add the context variable to the bpy module.
        data_node = DataNode.create_template()
        data_node.element(NameNode).add_text("context")
        data_node.element(DataTypeListNode).append_child(make_data_type_node("`bpy.types.Context`"))
        append_child(bpy_module_document, data_node)
