from typing import List
from docutils import nodes
from docutils.core import publish_doctree

from .transformer_base import TransformerBase
from .base_class_fixture import BaseClassFixture
from ..analyzer.nodes import (
    ModuleNode,
    DataNode,
    FunctionNode,
    ClassNode,
    NameNode,
    ArgumentListNode,
    ArgumentNode,
    FunctionReturnNode,
    FunctionListNode,
    AttributeListNode,
    AttributeNode,
    BaseClassListNode,
    BaseClassNode,
    ModTypeNode,
)
from ..utils import get_first_child, append_child, find_children


class ModApplier(TransformerBase):

    def get_mod_documents(self) -> List[nodes.document]:
        return self.mod_documents

    def _mod_append_function(self, func_nodes: List[FunctionNode],
                             mod_func_nodes: List[FunctionNode]):
        for mod_func_node in mod_func_nodes:
            mod_func_name_node = mod_func_node.element(NameNode)
            mod_arg_list_node = mod_func_node.element(ArgumentListNode)
            mod_arg_nodes = find_children(mod_arg_list_node, ArgumentNode)
            mod_return_node = mod_func_node.element(FunctionReturnNode)
            for func_node in func_nodes:
                func_name_node = func_node.element(NameNode)
                if func_name_node.astext() == mod_func_name_node.astext():
                    arg_list_node = func_node.element(ArgumentListNode)
                    for mod_arg_node in mod_arg_nodes:
                        arg_list_node.append_child(mod_arg_node)

                    return_node = func_node.element(FunctionReturnNode)
                    if not mod_return_node.empty() and return_node.empty():
                        index = func_node.index(return_node)
                        func_node.insert(index, mod_return_node.deepcopy())
                    break

    def _mod_append_class(self, class_nodes: List[ClassNode], mod_class_nodes: List[ClassNode]):
        for mod_class_node in mod_class_nodes:
            mod_class_name_node = mod_class_node.element(NameNode)
            for class_node in class_nodes:
                class_name_node = class_node.element(NameNode)
                if class_name_node.astext() != mod_class_name_node.astext():
                    continue

                func_list_node = class_node.element(FunctionListNode)
                mod_func_list_node = mod_class_node.element(FunctionListNode)
                func_nodes = find_children(func_list_node, FunctionNode)
                mod_func_nodes = find_children(mod_func_list_node, FunctionNode)

                # Append functions.
                for mod_func_node in mod_func_nodes:
                    mod_func_name_node = mod_func_node.element(NameNode)
                    mod_arg_list_node = mod_func_node.element(ArgumentListNode)
                    mod_arg_nodes = find_children(mod_arg_list_node, ArgumentNode)
                    mod_return_node = mod_func_node.element(FunctionReturnNode)
                    for func_node in func_nodes:
                        func_name_node = func_node.element(NameNode)
                        if func_name_node.astext() != mod_func_name_node.astext():
                            continue
                        arg_list_node = func_node.element(ArgumentListNode)
                        for mod_arg_node in mod_arg_nodes:
                            arg_list_node.append_child(mod_arg_node)
                        func_node.append_child(mod_return_node[0])
                        break
                    else:
                        func_list_node.append_child(mod_func_node)

                # Append attributes.
                attr_list_node = class_node.element(AttributeListNode)
                mod_attr_list_node = mod_class_node.element(AttributeListNode)
                mod_attr_nodes = find_children(mod_attr_list_node, AttributeNode)
                for mod_attr_node in mod_attr_nodes:
                    attr_list_node.append_child(mod_attr_node)

                # Append base classes.
                base_class_list_node = class_node.element(BaseClassListNode)
                mod_base_class_list_node = mod_class_node.element(BaseClassListNode)
                mod_base_class_nodes = find_children(mod_base_class_list_node, BaseClassNode)
                for mod_base_class_node in mod_base_class_nodes:
                    base_class_list_node.append_child(mod_base_class_node)

    def __init__(self, documents: List[nodes.document], **kwargs):
        super().__init__(documents, **kwargs)
        self.mod_files = kwargs["mod_files"]
        self.mod_documents = []

    @classmethod
    def name(cls) -> str:
        return "mod_applier"

    def apply(self, **kwargs):
        self.mod_documents = []

        if self.mod_files is None:
            return

        for file in self.mod_files:
            with open(file, "r", encoding="utf-8") as f:
                contents = f.read()

            settings_overrides = {
                "exit_status_level": 2,
                "halt_level": 2,
                "line_length_limit": 20000,
            }
            mod_document: nodes.document = publish_doctree(
                contents, settings_overrides=settings_overrides)
            fixture = BaseClassFixture([mod_document])
            fixture.apply()
            self.mod_documents.append(mod_document.deepcopy())

            mod_type_node = get_first_child(mod_document, ModTypeNode)
            if mod_type_node.astext() == "new":
                for document in self.documents:
                    module_node = get_first_child(document, ModuleNode)
                    if module_node is None:
                        continue
                    module_name_node = module_node.element(NameNode)
                    mod_module_node = get_first_child(mod_document, ModuleNode)
                    mod_module_name_node = mod_module_node.element(NameNode)
                    if module_name_node.astext() == mod_module_name_node.astext():
                        mod_data_nodes = find_children(mod_document, DataNode)
                        for mod_data_node in mod_data_nodes:
                            append_child(document, mod_data_node.deepcopy())
                        mod_func_nodes = find_children(mod_document, FunctionNode)
                        for mod_func_node in mod_func_nodes:
                            append_child(document, mod_func_node.deepcopy())
                        mod_class_nodes = find_children(mod_document, ClassNode)
                        for mod_class_node in mod_class_nodes:
                            append_child(document, mod_class_node.deepcopy())
                        break
                else:   # If the module is not found, add whole document.
                    mod_type_nodes = mod_document.findall(ModTypeNode)
                    for mod_type_node in mod_type_nodes:
                        mod_document.remove(mod_type_node)
                    self.documents.append(mod_document)
            elif mod_type_node.astext() == "append":
                for document in self.documents:
                    module_node = get_first_child(document, ModuleNode)
                    if module_node is None:
                        continue
                    # For functions, support only appending arguments and return.
                    func_nodes = find_children(document, FunctionNode)
                    mod_func_nodes = find_children(mod_document, FunctionNode)
                    self._mod_append_function(func_nodes, mod_func_nodes)

                    # For classes, support appending functions, attributes, and base-classes.
                    # For methods, support appending arguments and return.
                    class_nodes = find_children(document, ClassNode)
                    mod_class_nodes = find_children(mod_document, ClassNode)
                    self._mod_append_class(class_nodes, mod_class_nodes)
            else:
                raise NotImplementedError(f"ModTypeNode does not support {mod_type_node.astext()}")
