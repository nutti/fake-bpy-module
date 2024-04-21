from docutils import nodes

from .transformer_base import TransformerBase
from ..analyzer.nodes import (
    FunctionNode,
    ArgumentListNode,
    ArgumentNode,
    DataTypeListNode,
    DataTypeNode,
    DefaultValueNode,
)
from ..utils import find_children


class DefaultValueFiller(TransformerBase):

    def _fill(self, document: nodes.document):
        func_nodes = document.findall(FunctionNode)
        for func_node in func_nodes:
            arg_list_node = func_node.element(ArgumentListNode)
            arg_nodes = find_children(arg_list_node, ArgumentNode)
            for arg_node in arg_nodes:
                default_value_node = arg_node.element(DefaultValueNode)
                if not default_value_node.empty():
                    continue

                dtype_list_nodes = arg_node.element(DataTypeListNode)
                dtype_nodes = find_children(dtype_list_nodes, DataTypeNode)
                for dtype_node in dtype_nodes:
                    if "option" not in dtype_node.attributes:
                        continue
                    if "optional" in dtype_node.attributes["option"]:
                        break
                else:
                    # "optional" is not found.
                    continue

                for dtype_node in dtype_nodes:
                    dtype = dtype_node.to_string()

                    # Built-in data type.
                    BUILTIN_DTYPE_DEFAULT_VALUE_MAP = {
                        "bool": "False",
                        "str": "\"\"",
                        "bytes": "0",
                        "float": "0.0",
                        "int": "0",
                        "typing.List": "[]",
                        "typing.Dict": "{}",
                        "typing.Set": "()",
                        "typing.Tuple": "()",
                    }
                    if dtype in BUILTIN_DTYPE_DEFAULT_VALUE_MAP:
                        default_value_node.add_text(BUILTIN_DTYPE_DEFAULT_VALUE_MAP[dtype])
                        continue

                    # Modifier data type.
                    MODIFIER_DTYPE_DEFAULT_VALUE_MAP = {
                        "typing.List": "[]",
                        "typing.Dict": "{}",
                        "typing.Set": "()",
                        "typing.Tuple": "()",
                        "Generic": "None",
                        "typing.Iterator": "[]",
                        "typing.Callable": "None",
                        "typing.Any": "None",
                        "typing.Sequence": "[]",
                    }
                    found_type = False
                    for mod_dtype, default_value in MODIFIER_DTYPE_DEFAULT_VALUE_MAP.items():
                        if dtype.startswith(mod_dtype):
                            default_value_node.add_text(default_value)
                            found_type = True
                            break
                    if found_type:
                        continue

                    default_value_node.add_text("None")

    @classmethod
    def name(cls) -> str:
        return "default_value_filler"

    def apply(self, **kwargs):
        for document in self.documents:
            self._fill(document)
