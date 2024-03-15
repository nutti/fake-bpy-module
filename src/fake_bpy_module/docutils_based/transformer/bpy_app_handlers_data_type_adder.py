from docutils import nodes

from .transformer_base import TransformerBase
from ..analyzer.nodes import (
    DataTypeListNode,
    DataTypeNode,
    ModuleNode,
    DataNode,
    NameNode,
)
from ..common import get_first_child


class BpyAppHandlersDataTypeAdder(TransformerBase):

    def _apply(self, document: nodes.document):
        module_node = get_first_child(document, ModuleNode)
        if module_node:
            name_node = module_node.element(NameNode)
            if name_node.astext() == "bpy.app.handlers":
                data_nodes = document.findall(DataNode)
                for data_node in data_nodes:
                    name_node = data_node.element(NameNode)
                    if name_node.astext() == "persistent":
                        continue
                    data_type_list_node = data_node.element(DataTypeListNode)
                    data_type_list_node.insert(0, DataTypeNode(
                        text="list of callable[`bpy.types.Scene`]"))

    def apply(self, **kwargs):
        for document in self.documents:
            self._apply(document)
