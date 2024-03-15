import re
from docutils import nodes

from .transformer_base import TransformerBase
from ..analyzer.nodes import (
    ClassNode,
    BaseClassListNode,
    BaseClassNode,
    DataTypeListNode,
    DataTypeNode,
)
from ..common import find_children, split_string_by_comma


class BaseClassFixture(TransformerBase):
    _BASE_CLASS_REGEX = re.compile(r"^base (class|classes) --- (.*)")

    def _apply(self, document: nodes.document):
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

    def apply(self, **kwargs):
        for document in self.documents:
            self._apply(document)
