from docutils import nodes

from .transformer_base import TransformerBase


class FirstTitleRemover(TransformerBase):
    def _apply(self, document: nodes.document) -> None:
        title_node = document.findall(nodes.title)
        for node in title_node:
            if isinstance(node.parent, nodes.section | nodes.document):
                node.parent.remove(node)
            break

    @classmethod
    def name(cls) -> str:
        return "first_title_remover"

    def apply(self, **kwargs: dict) -> None:  # noqa: ARG002
        for document in self.documents:
            self._apply(document)
