from docutils import nodes

from fake_bpy_module.analyzer.nodes import (
    ArgumentListNode,
    ArgumentNode,
    AttributeListNode,
    AttributeNode,
    ClassNode,
    DataNode,
    DataTypeListNode,
    DataTypeNode,
    FunctionListNode,
    FunctionNode,
    FunctionReturnNode,
    NameNode,
)
from fake_bpy_module.utils import find_children

from .transformer_base import TransformerBase


class DuplicationRemover(TransformerBase):
    def _remove_duplicated_arguments(self, func_node: FunctionNode) -> None:
        arg_list_node = func_node.element(ArgumentListNode)
        arg_nodes = find_children(arg_list_node, ArgumentNode)
        exist_arg_names = set()
        for arg_node in arg_nodes:
            arg_name = arg_node.element(NameNode).astext()
            if arg_name in exist_arg_names:
                arg_list_node.remove(arg_node)
            else:
                exist_arg_names.add(arg_name)

    def _remove_duplicated_attributes(self, class_node: ClassNode) -> None:
        attr_list_node = class_node.element(AttributeListNode)
        attr_nodes = find_children(attr_list_node, AttributeNode)
        exist_attr_names = set()
        for attr_node in attr_nodes:
            attr_name = attr_node.element(NameNode).astext()
            if attr_name in exist_attr_names:
                attr_list_node.remove(attr_node)
            else:
                exist_attr_names.add(attr_name)

    def _is_same_datatype(self, dtype_node_1: DataTypeNode,
                          dtype_node_2: DataTypeNode) -> bool:
        return dtype_node_1.to_string() == dtype_node_2.to_string()

    def _is_same_attribute(self, attr_node_1: AttributeNode,
                           attr_node_2: AttributeNode) -> bool:
        name_node_1 = attr_node_1.element(NameNode)
        name_node_2 = attr_node_2.element(NameNode)
        if name_node_1.astext() != name_node_2.astext():
            return False

        dtype_nodes_1 = find_children(
            attr_node_1.element(DataTypeListNode), DataTypeNode)
        dtype_nodes_2 = find_children(
            attr_node_2.element(DataTypeListNode), DataTypeNode)
        if len(dtype_nodes_1) != len(dtype_nodes_2):
            return False
        for dtype_node_1, dtype_node_2 in zip(dtype_nodes_1, dtype_nodes_2,
                                              strict=True):
            if not self._is_same_datatype(dtype_node_1, dtype_node_2):
                return False

        return True

    def _is_same_argument(self, arg_node_1: ArgumentNode,
                          arg_node_2: ArgumentNode) -> bool:
        name_node_1 = arg_node_1.element(NameNode)
        name_node_2 = arg_node_2.element(NameNode)
        if name_node_1.astext() != name_node_2.astext():
            return False

        dtype_nodes_1 = find_children(
            arg_node_1.element(DataTypeListNode), DataTypeNode)
        dtype_nodes_2 = find_children(
            arg_node_2.element(DataTypeListNode), DataTypeNode)
        if len(dtype_nodes_1) != len(dtype_nodes_2):
            return False
        for dtype_node_1, dtype_node_2 in zip(dtype_nodes_1, dtype_nodes_2,
                                              strict=True):
            if not self._is_same_datatype(dtype_node_1, dtype_node_2):
                return False

        return True

    def _is_same_function_return(self, ret_node_1: FunctionReturnNode,
                                 ret_node_2: FunctionReturnNode) -> bool:
        dtype_nodes_1 = find_children(
            ret_node_1.element(DataTypeListNode), DataTypeNode)
        dtype_nodes_2 = find_children(
            ret_node_2.element(DataTypeListNode), DataTypeNode)
        if len(dtype_nodes_1) != len(dtype_nodes_2):
            return False
        for dtype_node_1, dtype_node_2 in zip(dtype_nodes_1, dtype_nodes_2,
                                              strict=True):
            if not self._is_same_datatype(dtype_node_1, dtype_node_2):
                return False

        return True

    def _is_same_function(self, func_node_1: FunctionNode,
                          func_node_2: FunctionNode) -> bool:
        name_node_1 = func_node_1.element(NameNode)
        name_node_2 = func_node_2.element(NameNode)
        if name_node_1.astext() != name_node_2.astext():
            return False

        arg_nodes_1 = find_children(
            func_node_1.element(ArgumentListNode), ArgumentNode)
        arg_nodes_2 = find_children(
            func_node_2.element(ArgumentListNode), ArgumentNode)
        if len(arg_nodes_1) != len(arg_nodes_2):
            return False
        for arg_node_1, arg_node_2 in zip(arg_nodes_1, arg_nodes_2,
                                          strict=True):
            if not self._is_same_argument(arg_node_1, arg_node_2):
                return False

        ret_node_1 = func_node_1.element(FunctionReturnNode)
        ret_node_2 = func_node_2.element(FunctionReturnNode)

        return self._is_same_function_return(ret_node_1, ret_node_2)

    def _is_same_class(self, class_node_1: ClassNode,
                       class_node_2: ClassNode) -> bool:
        name_node_1 = class_node_1.element(NameNode).astext()
        name_node_2 = class_node_2.element(NameNode).astext()
        if name_node_1 != name_node_2:
            return False

        attr_nodes_1 = find_children(
            class_node_1.element(AttributeListNode), AttributeNode)
        attr_nodes_2 = find_children(
            class_node_2.element(AttributeListNode), AttributeNode)
        if len(attr_nodes_1) != len(attr_nodes_2):
            return False
        for attr_node_1, attr_node_2 in zip(attr_nodes_1, attr_nodes_2,
                                            strict=True):
            if not self._is_same_attribute(attr_node_1, attr_node_2):
                return False

        func_nodes_1 = find_children(
            class_node_1.element(FunctionListNode), FunctionNode)
        func_nodes_2 = find_children(
            class_node_2.element(FunctionListNode), FunctionNode)
        if len(func_nodes_1) != len(func_nodes_2):
            return False
        for func_node_1, func_node_2 in zip(func_nodes_1, func_nodes_2,
                                            strict=True):
            if not self._is_same_function(func_node_1, func_node_2):
                return False

        return True

    def _remove_duplicated_classes(self, document: nodes.document) -> None:
        class_nodes = find_children(document, ClassNode)
        class_name_to_nodes: dict[str, list[ClassNode]] = {}
        class_nodes_to_remove: list[ClassNode] = []
        for class_node in class_nodes:
            class_name = class_node.element(NameNode).astext()
            if class_name not in class_name_to_nodes:
                class_name_to_nodes[class_name] = [class_node]
                continue
            for ref_class_node in class_name_to_nodes[class_name]:
                if self._is_same_class(class_node, ref_class_node):
                    class_nodes_to_remove.append(class_node)
                else:
                    class_name_to_nodes[class_name].append(class_node)

        for class_node in class_nodes_to_remove:
            document.remove(class_node)

    def _remove_duplicated_functions(self, document: nodes.document) -> None:
        func_nodes = find_children(document, FunctionNode)
        func_name_to_nodes: dict[str, list[FunctionNode]] = {}
        func_nodes_to_remove: list[FunctionNode] = []
        for func_node in func_nodes:
            func_name = func_node.element(NameNode).astext()
            if func_name not in func_name_to_nodes:
                func_name_to_nodes[func_name] = [func_node]
                continue
            for ref_func_node in func_name_to_nodes[func_name]:
                if self._is_same_function(func_node, ref_func_node):
                    func_nodes_to_remove.append(func_node)
                else:
                    func_name_to_nodes[func_name].append(func_node)

        for func_node in func_nodes_to_remove:
            document.remove(func_node)

    def _remove_duplicated_data(self, document: nodes.document) -> None:
        data_nodes = find_children(document, DataNode)
        data_name_to_nodes: dict[str, list[DataNode]] = {}
        data_nodes_to_remove: list[DataNode] = []
        for data_node in data_nodes:
            data_name = data_node.element(NameNode).astext()
            if data_name not in data_name_to_nodes:
                data_name_to_nodes[data_name] = [data_node]
                continue
            for ref_data_node in data_name_to_nodes[data_name]:
                if self._is_same_attribute(data_node, ref_data_node):
                    data_nodes_to_remove.append(data_node)
                else:
                    data_name_to_nodes[data_name].append(data_node)

        for data_node in data_nodes_to_remove:
            document.remove(data_node)

    def _apply(self, document: nodes.document) -> None:
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

        self._remove_duplicated_classes(document)
        self._remove_duplicated_functions(document)
        self._remove_duplicated_data(document)

    @classmethod
    def name(cls) -> str:
        return "duplication_remover"

    def apply(self, **kwargs: dict) -> None:  # noqa: ARG002
        for document in self.documents:
            self._apply(document)
