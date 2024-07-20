from typing import Self

from docutils import nodes

from fake_bpy_module.analyzer.nodes import (
    ArgumentListNode,
    ArgumentNode,
    AttributeListNode,
    AttributeNode,
    ClassNode,
    DataTypeListNode,
    DataTypeNode,
    FunctionListNode,
    FunctionNode,
    FunctionReturnNode,
    NameNode,
)
from fake_bpy_module.utils import find_children

from .transformer_base import TransformerBase


class SelfRewriter(TransformerBase):

    @classmethod
    def name(cls: type[Self]) -> str:
        return "self_rewriter"

    def _replace(self, from_node: nodes.Node, to_node: nodes.Node) -> None:
        parent = from_node.parent
        index = parent.index(from_node)
        parent.remove(from_node)
        parent.insert(index, to_node)

    def _rewrite_dtype_list(self, class_name: str,
                            dtype_list_node: DataTypeListNode) -> None:
        dtype_nodes = find_children(dtype_list_node, DataTypeNode)
        for dtype_node in dtype_nodes:
            dtype = dtype_node.to_string()
            if dtype == class_name:
                new_dtype_node = DataTypeNode()
                new_dtype_node.append(nodes.Text("typing.Self"))
                self._replace(dtype_node, new_dtype_node)

    def _rewrite_same_class_to_self(self, document: nodes.document) -> None:
        class_nodes = find_children(document, ClassNode)
        for class_node in class_nodes:
            class_name = class_node.element(NameNode).astext()

            func_list_node = class_node.element(FunctionListNode)
            func_nodes = find_children(func_list_node, FunctionNode)
            for func_node in func_nodes:
                arg_list_node = func_node.element(ArgumentListNode)
                arg_nodes = find_children(arg_list_node, ArgumentNode)
                for arg_node in arg_nodes:
                    dtype_list_node = arg_node.element(DataTypeListNode)
                    self._rewrite_dtype_list(class_name, dtype_list_node)

                ret_node = func_node.element(FunctionReturnNode)
                dtype_list_node = ret_node.element(DataTypeListNode)
                self._rewrite_dtype_list(class_name, dtype_list_node)

            attr_list_node = class_node.element(AttributeListNode)
            attr_nodes = find_children(attr_list_node, AttributeNode)
            for attr_node in attr_nodes:
                dtype_list_node = attr_node.element(DataTypeListNode)
                self._rewrite_dtype_list(class_name, dtype_list_node)

    def _apply(self, document: nodes.document) -> None:
        self._rewrite_same_class_to_self(document)

    def apply(self, **kwargs: dict) -> None:  # noqa: ARG002
        for document in self.documents:
            self._apply(document)
