from typing import Self

from docutils import nodes

from fake_bpy_module.analyzer.nodes import (
    ArgumentListNode,
    ArgumentNode,
    DataTypeListNode,
    DataTypeNode,
    DefaultValueNode,
    FunctionNode,
)
from fake_bpy_module.utils import find_children

from .transformer_base import TransformerBase


class DefaultValueFiller(TransformerBase):

    def _fill(self, document: nodes.document) -> None:
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
                    BUILTIN_DTYPE_DEFAULT_VALUE_MAP = {  # noqa: N806
                        "bool": "False",
                        "str": '""',
                        "bytes": "0",
                        "float": "0.0",
                        "int": "0",
                        "list": "[]",
                        "dict": "{}",
                        "set": "()",
                        "tuple": "()",
                    }
                    if dtype in BUILTIN_DTYPE_DEFAULT_VALUE_MAP:
                        default_value_node.add_text(BUILTIN_DTYPE_DEFAULT_VALUE_MAP[dtype])
                        continue

                    # Modifier data type.
                    DEFAULT_VALUE_MAP = {  # noqa: N806
                        "list": "[]",
                        "dict": "{}",
                        "set": "()",
                        "tuple": "()",
                        "Generic": "None",
                        "collections.abc.Iterator": "[]",
                        "collections.abc.Callable": "None",
                        "typing.Any": "None",
                        "collections.abc.Sequence": "[]",
                    }
                    found_type = False
                    for mod_dtype, default_value in DEFAULT_VALUE_MAP.items():
                        if dtype.startswith(mod_dtype):
                            default_value_node.add_text(default_value)
                            found_type = True
                            break
                    if found_type:
                        continue

                    default_value_node.add_text("None")

    @classmethod
    def name(cls: type[Self]) -> str:
        return "default_value_filler"

    def apply(self, **kwargs: dict) -> None:  # noqa: ARG002
        for document in self.documents:
            self._fill(document)
