from docutils import nodes
from docutils.core import publish_doctree

from fake_bpy_module.analyzer.nodes import ModuleNode, NameNode
from fake_bpy_module.utils import append_child, get_first_child

from .transformer_base import TransformerBase


class SameModuleMerger(TransformerBase):

    def _merge(self, documents: list[nodes.document]) -> list[nodes.document]:
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
        results: list[nodes.document] = []
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

    def apply(self, **kwargs: dict) -> None:  # noqa: ARG002
        new_documents = self._merge(self.documents)

        self.documents.clear()
        self.documents.extend(new_documents)
