import re

from docutils import nodes

from fake_bpy_module.analyzer.nodes import (
    BaseClassListNode,
    BaseClassNode,
    ClassNode,
    DataTypeListNode,
    DataTypeNode,
    NameNode,
)
from fake_bpy_module.utils import find_children, split_string_by_comma

from .transformer_base import TransformerBase


class BaseClassFixture(TransformerBase):
    _BASE_CLASS_REGEX = re.compile(r"^base (class|classes) --- (.*)")

    # Remove same base class with parent class.
    def _remove_self_parent_class(self, document: nodes.document) -> None:
        class_nodes = find_children(document, ClassNode)
        for class_node in class_nodes:
            class_name = class_node.element(NameNode).astext()

            base_class_list_node = class_node.element(BaseClassListNode)
            base_class_nodes = find_children(base_class_list_node,
                                             BaseClassNode)
            for base_class_node in base_class_nodes:
                dtype_list_node = base_class_node.element(DataTypeListNode)
                dtype_nodes = find_children(dtype_list_node, DataTypeNode)
                for dtype_node in dtype_nodes:
                    if class_name == dtype_node.to_string():
                        dtype_list_node.remove(dtype_node)
                if dtype_list_node.empty():
                    base_class_list_node.remove(base_class_node)

    def _apply(self, document: nodes.document) -> None:
        paragraphs = document.findall(nodes.paragraph)
        for para in paragraphs:
            m = self._BASE_CLASS_REGEX.match(para.astext())
            if m:
                base_classes = split_string_by_comma(m.group(2))
                # Fix: "E0240: Inconsistent method resolution order" error on
                #      pylint_cycles.sh
                base_classes.reverse()
                class_nodes = find_children(document, ClassNode)
                for class_node in class_nodes:
                    base_class_list_node = class_node.element(BaseClassListNode)
                    for bc in base_classes:
                        base_class_node = BaseClassNode.create_template()
                        base_class_node.element(DataTypeListNode).append_child(
                            DataTypeNode(text=bc))
                        base_class_list_node.append_child(base_class_node)

                para.parent.remove(para)
                break

    @classmethod
    def name(cls) -> str:
        return "base_class_fixture"

    def apply(self, **kwargs: dict) -> None:  # noqa: ARG002
        for document in self.documents:
            self._apply(document)
            self._remove_self_parent_class(document)
