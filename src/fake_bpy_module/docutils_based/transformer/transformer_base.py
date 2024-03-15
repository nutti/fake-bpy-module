from typing import List
from docutils import nodes


class TransformerBase:

    # pylint: disable=W0613
    def __init__(self, documents: List[nodes.document], **kwargs):
        self.documents: List[nodes.document] = documents

    def apply(self, **kwargs):
        raise NotImplementedError("Subclass must implement this method")
