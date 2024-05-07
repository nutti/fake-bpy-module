from typing import List
from docutils import nodes
from docutils.core import publish_doctree

from .transformer_base import TransformerBase
from ..analyzer.nodes import (
    ModuleNode,
    NameNode,
)
from ..utils import get_first_child, append_child


class SameModuleMerger(TransformerBase):

    def _merge(self, documents: List[nodes.document]) -> List[nodes.document]:
        module_to_documents = {}
        for document in documents:
            module_node = get_first_child(document, ModuleNode)
            if module_node is None:
                continue

            module_name = module_node.astext()
            if module_name not in module_to_documents:
                module_to_documents[module_name] = []
            module_to_documents[module_name].append(document)

        # Combine document by the same module document.
        results: List[nodes.document] = []
        for module_name, docs in module_to_documents.items():
            new_doc: nodes.document = publish_doctree("")
            for doc in docs:
                for child in doc.children[:]:
                    if isinstance(child, ModuleNode):
                        assert module_name == child.element(NameNode).astext()
                        try:
                            next(new_doc.findall(ModuleNode))
                        except StopIteration:
                            append_child(new_doc, child)
                    else:
                        append_child(new_doc, child)
            results.append(new_doc)

        return results

    @classmethod
    def name(cls) -> str:
        return "same_module_merger"

    def apply(self, **kwargs):
        new_documents = self._merge(self.documents)

        self.documents.clear()
        self.documents.extend(new_documents)
