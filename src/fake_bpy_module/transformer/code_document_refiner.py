from docutils import nodes

from fake_bpy_module.analyzer.nodes import CodeDocumentNode
from fake_bpy_module.utils import append_child, find_children

from .transformer_base import TransformerBase


class CodeDocumentRefiner(TransformerBase):
    def _apply(self, document: nodes.document) -> None:
        # Merge CodeDocumentNode.
        doc_nodes = find_children(document, CodeDocumentNode)
        new_doc_node = CodeDocumentNode()
        for node in doc_nodes:
            for child in node.children:
                new_doc_node.append(child)
            document.remove(node)

        # Remove trivial nodes.
        para_nodes = find_children(new_doc_node, nodes.paragraph)
        nodes_to_remove: list[nodes.Node] = []
        for node in para_nodes:
            print("@@@@@@@@")
            print(node.pformat())
            if node.astext() in ("Inherited Functions", "Inherited Properties",
                                 "References"):
                index = node.parent.children.index(node)
                next_node = node.parent.children[index+1]
                nodes_to_remove.append(node)
                nodes_to_remove.append(next_node)
            elif node.astext().startswith("subclasses ---"):
                nodes_to_remove.append(node)
        for node in nodes_to_remove:
            new_doc_node.remove(node)

        # Remove CodeDocumentNode if empty.
        if len(new_doc_node.children) != 0:
            append_child(document, new_doc_node)

    @classmethod
    def name(cls) -> str:
        return "code_document_refiner"

    def apply(self, **kwargs: dict) -> None:  # noqa: ARG002
        for document in self.documents:
            self._apply(document)
