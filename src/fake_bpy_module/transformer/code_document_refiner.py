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

        # Part 1:
        #     <section ids="inherited-properties" names="inherited\ properties">
        #     <title>
        #         Inherited Properties
        #     <paragraph>
        #         ...
        nodes_to_remove: list[nodes.Node] = []
        nodes_to_search = find_children(new_doc_node, nodes.section)
        for node in nodes_to_search:
            need_remove = False
            for attr_id in node.attributes["ids"]:
                if attr_id in ("inherited-functions",
                               "inherited-properties",
                               "references"):
                    need_remove = True
                    break
            if need_remove:
                index = node.parent.children.index(node)
                next_node = node.parent.children[index+1]
                next_next_node = node.parent.children[index+2]
                nodes_to_remove.append(node)
                nodes_to_remove.append(next_node)
                nodes_to_remove.append(next_next_node)

        # Part 2:
        #     <paragraph>
        #         Inherited Properties
        #     <paragraph>
        #         ...
        # and
        #     <paragraph>
        #         subclasses ---
        nodes_to_search = find_children(new_doc_node, nodes.paragraph)
        for node in nodes_to_search:
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
