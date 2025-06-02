from docutils import nodes

from fake_bpy_module.analyzer.nodes import (
    DescriptionNode,
    EnumItemListNode,
    EnumItemNode,
    EnumNode,
    ModuleNode,
    NameNode,
    SourceFilenameNode,
)
from fake_bpy_module.utils import (
    get_first_child,
)

from .transformer_base import TransformerBase


def to_camel(name: str) -> str:
    return "".join(w.title() for w in name.split("-"))


class RnaEnumConverter(TransformerBase):
    @classmethod
    def name(cls) -> str:
        return "rna_enum_converter"

    def _apply(self, document: nodes.document) -> None:
        if "ids" not in document.attributes:
            return

        rna_enum_name = False
        for id_ in document.attributes["ids"]:
            if id_.startswith("rna-enum-"):
                rna_enum_name = id_[len("rna-enum-"):]
                break
        else:
            return

        source_file_node = get_first_child(document, SourceFilenameNode)
        children_orig = document.children[:]
        for child in children_orig:
            document.remove(child)
        document.append(source_file_node)

        module_node = ModuleNode.create_template()
        module_node.element(NameNode).add_text("bpy.stub_internal.rna_enums")
        document.append(module_node)

        enum_node = EnumNode.create_template()
        enum_node.element(NameNode).add_text(to_camel(rna_enum_name))
        enum_item_list_node = enum_node.element(EnumItemListNode)
        for child in children_orig:
            field_nodes = child.findall(nodes.field)
            for field_node in field_nodes:
                fname_node = get_first_child(field_node, nodes.field_name)
                fbody_node = get_first_child(field_node, nodes.field_body)

                enum_item_node = EnumItemNode.create_template()
                enum_item_node.element(NameNode).add_text(fname_node.astext())
                enum_item_node.element(DescriptionNode).add_text(fbody_node.astext())
                enum_item_list_node.append(enum_item_node)
        document.append(enum_node)

    def apply(self, **kwargs: dict) -> None:  # noqa: ARG002
        for document in self.documents:
            self._apply(document)
