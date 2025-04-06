import copy
from pathlib import Path
from typing import Any

from docutils import nodes
from docutils.core import publish_doctree

from fake_bpy_module.analyzer.nodes import (
    ArgumentListNode,
    ArgumentNode,
    AttributeListNode,
    AttributeNode,
    BaseClassListNode,
    BaseClassNode,
    ClassNode,
    DataNode,
    DataTypeListNode,
    DataTypeNode,
    DefaultValueNode,
    DescriptionNode,
    FunctionListNode,
    FunctionNode,
    FunctionReturnNode,
    ModTypeNode,
    ModuleNode,
    NameNode,
    NodeBase,
)
from fake_bpy_module.utils import (
    LOG_LEVEL_DEBUG,
    append_child,
    find_children,
    get_first_child,
    output_log,
)

from .base_class_fixture import BaseClassFixture
from .transformer_base import TransformerBase


def get_merged_node_attributes(
        node_1: NodeBase, node_2: NodeBase) -> dict[str, Any]:
    attrs_1 = node_1.attributes
    attrs_2 = node_2.attributes

    attrs_merged = copy.deepcopy(attrs_1)
    for key, value in attrs_2.items():
        if key not in attrs_merged:
            attrs_merged[key] = value
    return attrs_merged


class ModApplier(TransformerBase):

    def get_mod_documents(self) -> list[nodes.document]:
        return self.mod_documents

    def _mod_update_data(self, data_nodes: list[DataNode],
                         mod_data_nodes: list[DataNode]) -> None:
        for mod_data_node in mod_data_nodes:
            mod_data_name_node = mod_data_node.element(NameNode)
            for data_node in data_nodes:
                data_name_node = data_node.element(NameNode)
                if data_name_node.astext() == mod_data_name_node.astext():
                    dtype_list_node = data_node.element(DataTypeListNode)
                    dtype_list_node.clear()

                    mod_dtype_list_node = mod_data_node.element(
                        DataTypeListNode)
                    dtype_nodes = find_children(
                        mod_dtype_list_node, DataTypeNode)
                    for node in dtype_nodes:
                        dtype_list_node.append(node)
                    break

    def _mod_update_function_arguments(
            self, arg_list_node: ArgumentListNode,
            mod_arg_list_node: ArgumentListNode) -> None:
        if mod_arg_list_node.empty():
            return

        arg_nodes = find_children(arg_list_node, ArgumentNode)
        mod_arg_nodes = find_children(mod_arg_list_node, ArgumentNode)

        for mod_arg_node in mod_arg_nodes:
            mod_arg_name_node = mod_arg_node.element(NameNode)
            mod_arg_name = mod_arg_name_node.astext()

            for arg_node in arg_nodes:
                arg_name = arg_node.element(NameNode).astext()

                if arg_name == mod_arg_name:
                    mod_options = []
                    node_attrs = mod_arg_node.attributes
                    if "mod-option" in node_attrs:
                        mod_options = node_attrs["mod-option"].split(",")
                    if "update-argument-type" in mod_options:
                        arg_node.attributes["argument_type"] = \
                            node_attrs["argument_type"]

                    mod_desc_node = mod_arg_node.element(DescriptionNode)
                    if not mod_desc_node.empty():
                        arg_node.replace_node(mod_desc_node)
                    mod_default_value_node = mod_arg_node.element(
                        DefaultValueNode)
                    if not mod_default_value_node.empty():
                        arg_node.replace_node(mod_default_value_node)
                    mod_dtype_list_node = mod_arg_node.element(DataTypeListNode)
                    if not mod_dtype_list_node.empty():
                        arg_node.replace_node(mod_dtype_list_node)
                    break
            else:
                arg_list_node.append_child(mod_arg_node)

    def _mod_update_function_return(
            self, return_node: FunctionReturnNode,
            mod_return_node: FunctionReturnNode) -> None:
        if mod_return_node.empty():
            return

        mod_desc_node = mod_return_node.element(DescriptionNode)
        if not mod_desc_node.empty():
            return_node.replace_node(mod_desc_node)
        mod_dtype_list_node = mod_return_node.element(
            DataTypeListNode)
        if not mod_dtype_list_node.empty():
            return_node.replace_node(mod_dtype_list_node)

    # pylint: disable=R0914,R1702
    def _mod_update_function(self, func_nodes: list[FunctionNode],
                             mod_func_nodes: list[FunctionNode]) -> None:
        for mod_func_node in mod_func_nodes:
            mod_func_name_node = mod_func_node.element(NameNode)
            mod_arg_list_node = mod_func_node.element(ArgumentListNode)
            mod_return_node = mod_func_node.element(FunctionReturnNode)
            for func_node in func_nodes:
                func_name_node = func_node.element(NameNode)
                if func_name_node.astext() != mod_func_name_node.astext():
                    continue

                attrs = get_merged_node_attributes(func_node, mod_func_node)
                func_node.attributes = attrs

                # Update description.
                mod_desc_node = mod_func_node.element(DescriptionNode)
                if not mod_desc_node.empty():
                    func_node.replace_node(mod_desc_node)

                # Update arguments.
                arg_list_node = func_node.element(ArgumentListNode)
                self._mod_update_function_arguments(
                    arg_list_node, mod_arg_list_node)

                # Update return.
                return_node = func_node.element(FunctionReturnNode)
                self._mod_update_function_return(return_node, mod_return_node)
                break

    # pylint: disable=R0914,R1702
    def _mod_update_class(self, class_nodes: list[ClassNode],
                          mod_class_nodes: list[ClassNode]) -> None:
        for mod_class_node in mod_class_nodes:
            mod_class_name_node = mod_class_node.element(NameNode)
            mod_class_name = mod_class_name_node.astext()

            for class_node in class_nodes:
                class_name_node = class_node.element(NameNode)
                class_name = class_name_node.astext()
                if class_name != mod_class_name:
                    continue

                attrs = get_merged_node_attributes(class_node, mod_class_node)
                class_node.attributes = attrs

                # Update description.
                mod_desc_node = mod_class_node.element(DescriptionNode)
                if not mod_desc_node.empty():
                    class_node.replace_node(mod_desc_node)

                # Update functions.
                func_list_node = class_node.element(FunctionListNode)
                mod_func_list_node = mod_class_node.element(FunctionListNode)
                func_nodes = find_children(func_list_node, FunctionNode)
                mod_func_nodes = find_children(mod_func_list_node, FunctionNode)
                self._mod_update_function(func_nodes, mod_func_nodes)

                # Update attributes.
                attr_list_node = class_node.element(AttributeListNode)
                attr_nodes = find_children(attr_list_node, AttributeNode)
                mod_attr_list_node = mod_class_node.element(AttributeListNode)
                mod_attr_nodes = find_children(
                    mod_attr_list_node, AttributeNode)
                for mod_attr_node in mod_attr_nodes:
                    mod_attr_name = mod_attr_node.element(NameNode).astext()
                    for attr_node in attr_nodes:
                        attr_name = attr_node.element(NameNode).astext()
                        if attr_name == mod_attr_name:
                            attr_list_node.replace(attr_node, mod_attr_node)
                            break

                # Update base classes.
                bc_list_node = class_node.element(BaseClassListNode)
                mod_bc_list_node = mod_class_node.element(BaseClassListNode)
                if not mod_bc_list_node.empty():
                    bc_list_node.clear()
                    mod_bc_nodes = find_children(
                        mod_bc_list_node, BaseClassNode)
                    for mod_bc_node in mod_bc_nodes:
                        bc_list_node.append_child(mod_bc_node)

    def _mod_append_function(
            self, func_nodes: list[FunctionNode],
            mod_func_nodes: list[FunctionNode],
            add_if_not_exist: bool = False,
            func_list_node: FunctionListNode | None = None) -> None:
        for mod_func_node in mod_func_nodes:
            mod_func_name_node = mod_func_node.element(NameNode)
            mod_arg_list_node = mod_func_node.element(ArgumentListNode)
            mod_arg_nodes = find_children(mod_arg_list_node, ArgumentNode)
            mod_return_node = mod_func_node.element(FunctionReturnNode)
            for func_node in func_nodes:
                func_name_node = func_node.element(NameNode)
                if func_name_node.astext() == mod_func_name_node.astext():
                    attrs = get_merged_node_attributes(func_node, mod_func_node)
                    func_node.attributes = attrs

                    arg_list_node = func_node.element(ArgumentListNode)
                    for mod_arg_node in mod_arg_nodes:
                        arg_list_node.append_child(mod_arg_node)

                    return_node = func_node.element(FunctionReturnNode)
                    if not mod_return_node.empty() and return_node.empty():
                        func_node.replace_node(mod_return_node)
                    break
            else:
                if add_if_not_exist:
                    func_list_node.append_child(mod_func_node)

    # pylint: disable=R0914
    def _mod_append_class(self, class_nodes: list[ClassNode],
                          mod_class_nodes: list[ClassNode]) -> None:
        for mod_class_node in mod_class_nodes:
            mod_class_name_node = mod_class_node.element(NameNode)
            mod_class_name = mod_class_name_node.astext()

            for class_node in class_nodes:
                class_name_node = class_node.element(NameNode)
                class_name = class_name_node.astext()
                if class_name != mod_class_name:
                    continue

                attrs = get_merged_node_attributes(class_node, mod_class_node)
                class_node.attributes = attrs

                func_list_node = class_node.element(FunctionListNode)
                mod_func_list_node = mod_class_node.element(FunctionListNode)
                func_nodes = find_children(func_list_node, FunctionNode)
                mod_func_nodes = find_children(mod_func_list_node, FunctionNode)

                # Append functions.
                self._mod_append_function(func_nodes, mod_func_nodes,
                                          True, func_list_node)

                # Append attributes.
                attr_list_node = class_node.element(AttributeListNode)
                mod_attr_list_node = mod_class_node.element(AttributeListNode)
                mod_attr_nodes = find_children(
                    mod_attr_list_node, AttributeNode)
                for mod_attr_node in mod_attr_nodes:
                    attr_list_node.append_child(mod_attr_node)

                # Append base classes.
                bc_list_node = class_node.element(BaseClassListNode)
                mod_bc_list_node = mod_class_node.element(BaseClassListNode)
                mod_bc_nodes = find_children(mod_bc_list_node, BaseClassNode)
                for mod_bc_node in mod_bc_nodes:
                    bc_list_node.append_child(mod_bc_node)

    def _mod_new(self, mod_document: nodes.document,
                 module_name_to_document: dict[str, nodes.document]) -> None:
        mod_module_node = get_first_child(mod_document, ModuleNode)
        mod_module_name_node = mod_module_node.element(NameNode)

        mod_module_name = mod_module_name_node.astext()
        if mod_module_name in module_name_to_document:
            document = module_name_to_document[mod_module_name]

            data_nodes = find_children(document, DataNode)
            data_names = {d.element(NameNode).astext() for d in data_nodes}
            mod_data_nodes = find_children(mod_document, DataNode)
            for mod_data_node in mod_data_nodes:
                mod_data_name = mod_data_node.element(NameNode).astext()
                if mod_data_name in data_names:
                    output_log(LOG_LEVEL_DEBUG,
                               f"Duplication Skip: {mod_data_name}")
                    continue
                append_child(document, mod_data_node.deepcopy())

            func_nodes = find_children(document, FunctionNode)
            mod_func_nodes = find_children(mod_document, FunctionNode)
            func_names = {f.element(NameNode).astext() for f in func_nodes}
            for mod_func_node in mod_func_nodes:
                mod_func_name = mod_func_node.element(NameNode).astext()
                if mod_func_name in func_names:
                    output_log(LOG_LEVEL_DEBUG,
                               f"Duplication Skip: {mod_func_name}")
                    continue
                append_child(document, mod_func_node.deepcopy())

            class_nodes = find_children(document, ClassNode)
            mod_class_nodes = find_children(mod_document, ClassNode)
            class_names = {c.element(NameNode).astext() for c in class_nodes}
            for mod_class_node in mod_class_nodes:
                mod_class_name = mod_class_node.element(NameNode).astext()
                if mod_class_name in class_names:
                    output_log(LOG_LEVEL_DEBUG,
                               f"Duplication Skip: {mod_class_name}")
                    continue
                append_child(document, mod_class_node.deepcopy())
        else:   # If the module is not found, add whole document.
            mod_type_nodes = mod_document.findall(ModTypeNode)
            for mod_type_node in mod_type_nodes:
                mod_document.remove(mod_type_node)
            self.documents.append(mod_document)
            assert mod_module_name not in mod_module_name_node
            module_name_to_document[mod_module_name] = mod_document

    def _mod_append(self, mod_document: nodes.document,
                    module_name_to_document: dict[str, nodes.document]) -> None:
        mod_module_node = get_first_child(mod_document, ModuleNode)
        mod_module_name_node = mod_module_node.element(NameNode)

        mod_module_name = mod_module_name_node.astext()
        if mod_module_name in module_name_to_document:
            document = module_name_to_document[mod_module_name]

            # For functions, support only appending arguments
            # and return.
            func_nodes = find_children(document, FunctionNode)
            mod_func_nodes = find_children(mod_document, FunctionNode)
            self._mod_append_function(func_nodes, mod_func_nodes)

            # For classes, support appending functions, attributes,
            # and base-classes.
            # For methods, support appending arguments and return.
            class_nodes = find_children(document, ClassNode)
            mod_class_nodes = find_children(mod_document, ClassNode)
            self._mod_append_class(class_nodes, mod_class_nodes)
        else:
            raise ValueError(f"Modules to be appended are not found "
                             f"{mod_module_name}")

    def _mod_update(self, mod_document: nodes.document,
                    module_name_to_document: dict[str, nodes.document]) -> None:
        mod_module_node = get_first_child(mod_document, ModuleNode)
        mod_module_name_node = mod_module_node.element(NameNode)

        mod_module_name = mod_module_name_node.astext()
        if mod_module_name in module_name_to_document:
            document = module_name_to_document[mod_module_name]

            # For data, suppor only updating type.
            data_nodes = find_children(document, DataNode)
            mod_data_nodes = find_children(mod_document, DataNode)
            self._mod_update_data(data_nodes, mod_data_nodes)

            # For functions, support only updating arguments and return.
            func_nodes = find_children(document, FunctionNode)
            mod_func_nodes = find_children(mod_document, FunctionNode)
            self._mod_update_function(func_nodes, mod_func_nodes)

            # For classes, support updating functions, attributes,
            # and base-classes.
            # For methods, support updating arguments and return.
            class_nodes = find_children(document, ClassNode)
            mod_class_nodes = find_children(mod_document, ClassNode)
            self._mod_update_class(class_nodes, mod_class_nodes)
        else:
            raise ValueError(f"Modules to be updated are not found "
                             f"{mod_module_name}")

    def __init__(self, documents: list[nodes.document], **kwargs: dict) -> None:
        super().__init__(documents, **kwargs)
        self.mod_files = kwargs["mod_files"]
        self.mod_documents = []

    @classmethod
    def name(cls) -> str:
        return "mod_applier"

    def apply(self, **kwargs: dict) -> None:  # noqa: ARG002
        self.mod_documents = []

        if self.mod_files is None:
            return

        # Store documents for performance improvement.
        module_name_to_document = {}
        for document in self.documents:
            module_node = get_first_child(document, ModuleNode)
            if module_node is None:
                continue
            module_name_node = module_node.element(NameNode)
            module_name_to_document[module_name_node.astext()] = document

        for file in self.mod_files:
            with Path(file).open("r", encoding="utf-8") as f:
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
                self._mod_new(mod_document, module_name_to_document)
            elif mod_type_node.astext() == "append":
                self._mod_append(mod_document, module_name_to_document)
            elif mod_type_node.astext() == "update":
                self._mod_update(mod_document, module_name_to_document)
            else:
                raise NotImplementedError(f"ModTypeNode does not support "
                                          f"{mod_type_node.astext()}")
