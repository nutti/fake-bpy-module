from docutils import nodes

from .transformer_base import TransformerBase
from ..analyzer.nodes import (
    DataTypeListNode,
    DataTypeNode,
    ModuleNode,
    FunctionNode,
    NameNode,
    ArgumentNode,
    ArgumentListNode,
    DefaultValueNode,
    make_data_type_node,
)

from ..utils import find_children, get_first_child, append_child


class BpyOpsOverrideParameterAdder(TransformerBase):
    def _apply(self, document: nodes.document):
        module_node = get_first_child(document, ModuleNode)
        if module_node:
            name_node = module_node.element(NameNode)
            if name_node.astext().startswith("bpy.ops"):
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
                        make_data_type_node("`bpy.types.Context`"))
                    dtype_node = DataTypeNode()
                    append_child(dtype_node, nodes.Text("typing.Dict[str, typing.Any]"))
                    dtype_node.attributes["mod-option"] = "skip-refine"
                    arg_node.element(DataTypeListNode).append_child(dtype_node)
                    arg_list_node.insert(0, arg_node)

                    arg_node = ArgumentNode.create_template(argument_type="arg")
                    arg_node.element(NameNode).add_text("execution_context")
                    arg_node.element(DefaultValueNode).add_text("None")
                    arg_node.element(DataTypeListNode).append_child(
                        make_data_type_node("str, int"))
                    arg_list_node.insert(1, arg_node)

                    arg_node = ArgumentNode.create_template(argument_type="arg")
                    arg_node.element(NameNode).add_text("undo")
                    arg_node.element(DefaultValueNode).add_text("None")
                    arg_node.element(DataTypeListNode).append_child(
                        make_data_type_node("bool"))
                    arg_list_node.insert(2, arg_node)

    @classmethod
    def name(cls) -> str:
        return "bpy_ops_override_parameters_adder"

    def apply(self, **kwargs):
        for document in self.documents:
            self._apply(document)
