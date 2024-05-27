import re
import typing
from docutils import nodes

from .transformer_base import TransformerBase
from ..analyzer.nodes import (
    ClassNode,
    DataNode,
    DataTypeListNode,
    DataTypeNode,
    ModuleNode,
    FunctionNode,
    NameNode,
    ArgumentNode,
    ArgumentListNode,
    DefaultValueNode,
    AttributeListNode,
    AttributeNode,
    BaseClassListNode,
    BaseClassNode,
    make_data_type_node,
)

from ..utils import (
    find_children,
    get_first_child,
    append_child,
    output_log,
    LOG_LEVEL_DEBUG,
    LOG_LEVEL_WARN,
)


class BpyModuleTweaker(TransformerBase):
    def _make_bpy_prop_functions_arguments_kwonlyargs(self, document: nodes.document):
        module_name = get_first_child(document, ModuleNode).element(NameNode).astext()
        if module_name != "bpy.props":
            return

        func_nodes = find_children(document, FunctionNode)
        for func_node in func_nodes:
            arg_list_node = func_node.element(ArgumentListNode)
            arg_nodes = find_children(arg_list_node, ArgumentNode)
            for arg_node in arg_nodes:
                arg_node.attributes["argument_type"] = "kwonlyarg"

    def _add_bpy_app_handlers_functions_data_types(self, document: nodes.document):
        module_name = get_first_child(document, ModuleNode).element(NameNode).astext()
        if module_name != "bpy.app.handlers":
            return

        data_nodes = document.findall(DataNode)
        for data_node in data_nodes:
            name_node = data_node.element(NameNode)
            if name_node.astext() == "persistent":
                continue
            data_type_list_node = data_node.element(DataTypeListNode)
            data_type_list_node.insert(
                0, make_data_type_node("list of callable[`bpy.types.Scene`]")
            )

    def _add_bpy_ops_override_parameters(self, document: nodes.document):
        module_name = get_first_child(document, ModuleNode).element(NameNode).astext()
        if not module_name.startswith("bpy.ops"):
            return

        function_nodes = find_children(document, FunctionNode)
        for func_node in function_nodes:
            if func_node.attributes["function_type"] != "function":
                continue

            arg_list_node = get_first_child(func_node, ArgumentListNode)
            for arg_node in find_children(arg_list_node, ArgumentNode):
                arg_node.attributes["argument_type"] = "kwonlyarg"

            arg_node = ArgumentNode.create_template(argument_type="arg")
            arg_node.element(NameNode).add_text("override_context")
            arg_node.element(DefaultValueNode).add_text("None")
            arg_node.element(DataTypeListNode).append_child(
                make_data_type_node("`bpy.types.Context`")
            )
            dtype_node = DataTypeNode()
            append_child(dtype_node, nodes.Text("dict[str, typing.Any]"))
            dtype_node.attributes["mod-option"] = "skip-refine"
            arg_node.element(DataTypeListNode).append_child(dtype_node)
            arg_list_node.insert(0, arg_node)

            arg_node = ArgumentNode.create_template(argument_type="arg")
            arg_node.element(NameNode).add_text("execution_context")
            arg_node.element(DefaultValueNode).add_text("None")
            arg_node.element(DataTypeListNode).append_child(
                make_data_type_node("str, int")
            )
            arg_list_node.insert(1, arg_node)

            arg_node = ArgumentNode.create_template(argument_type="arg")
            arg_node.element(NameNode).add_text("undo")
            arg_node.element(DefaultValueNode).add_text("None")
            arg_node.element(DataTypeListNode).append_child(make_data_type_node("bool"))
            arg_list_node.insert(2, arg_node)

    def _rebase_bpy_types_class_base_class(self, document: nodes.document):
        module_name = get_first_child(document, ModuleNode).element(NameNode).astext()
        if not module_name.startswith("bpy.types"):
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
                        r"([a-zA-Z0-9]+)`, \(readonly\)$",
                        dtype_str,
                    ):
                        parent_to_child[m.group(1)] = m.group(2)

        for parent, child in parent_to_child.items():
            if parent == child:
                output_log(LOG_LEVEL_WARN, f"Parent and child is same ({parent})")
                continue
            output_log(
                LOG_LEVEL_DEBUG,
                f"Inheritance changed (Parent: {parent}, Child: {child})",
            )

            class_node = class_name_to_class_node[parent]
            bc_list_node = class_node.element(BaseClassListNode)

            bc_node = BaseClassNode.create_template()
            dtype_list_node = bc_node.element(DataTypeListNode)
            dtype_list_node.append_child(
                make_data_type_node(f"`bpy_prop_collection` of `{child}`, (readonly)")
            )
            bc_list_node.append_child(bc_node)

    def _apply(self, document: nodes.document):
        module_node = get_first_child(document, ModuleNode)
        if not module_node:
            return

        name_node = module_node.element(NameNode)
        if not name_node.astext().startswith("bpy"):
            return

        self._make_bpy_prop_functions_arguments_kwonlyargs(document)
        self._add_bpy_app_handlers_functions_data_types(document)
        self._add_bpy_ops_override_parameters(document)
        self._rebase_bpy_types_class_base_class(document)

    @classmethod
    def name(cls) -> str:
        return "bpy_module_tweaker"

    def apply(self, **kwargs):
        for document in self.documents:
            self._apply(document)
