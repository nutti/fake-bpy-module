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

    def _apply(self, document: nodes.document):
        module_node = get_first_child(document, ModuleNode)
        if not module_node:
            return

        name_node = module_node.element(NameNode)
        if not name_node.astext().startswith("bpy"):
            return

        self._make_bpy_prop_functions_arguments_kwonlyargs(document)

    @classmethod
    def name(cls) -> str:
        return "bpy_module_tweaker"

    def apply(self, **kwargs):
        for document in self.documents:
            self._apply(document)
