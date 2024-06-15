from docutils import nodes

from .transformer_base import TransformerBase
from ..analyzer.nodes import (
    ClassNode,
    FunctionListNode,
    FunctionNode,
    ArgumentListNode,
    ArgumentNode,
    NameNode,
    AttributeListNode,
    AttributeNode,
)
from ..utils import find_children


class DuplicatedFunctionArgumentsRemover(TransformerBase):
    def _remove_duplicated_arguments(self, func_node: FunctionNode):
        arg_list_node = func_node.element(ArgumentListNode)
        arg_nodes = find_children(arg_list_node, ArgumentNode)
        exist_arg_names = set()
        for arg_node in arg_nodes:
            arg_name = arg_node.element(NameNode).astext()
            if arg_name in exist_arg_names:
                arg_list_node.remove(arg_node)
            else:
                exist_arg_names.add(arg_name)

    def _remove_duplicated_attributes(self, class_node: ClassNode):
        attr_list_node = class_node.element(AttributeListNode)
        attr_nodes = find_children(attr_list_node, AttributeNode)
        exist_attr_names = set()
        for attr_node in attr_nodes:
            attr_name = attr_node.element(NameNode).astext()
            if attr_name in exist_attr_names:
                attr_list_node.remove(attr_node)
            else:
                exist_attr_names.add(attr_name)

    def _apply(self, document: nodes.document):
        class_nodes = find_children(document, ClassNode)
        for class_node in class_nodes:
            func_list_node = class_node.element(FunctionListNode)
            func_nodes = find_children(func_list_node, FunctionNode)
            for func_node in func_nodes:
                self._remove_duplicated_arguments(func_node)
            self._remove_duplicated_attributes(class_node)

        func_nodes = find_children(document, FunctionNode)
        for func_node in func_nodes:
            self._remove_duplicated_arguments(func_node)

    @classmethod
    def name(cls) -> str:
        return "duplicated_function_arguments_remover"

    def apply(self, **kwargs):
        for document in self.documents:
            self._apply(document)
