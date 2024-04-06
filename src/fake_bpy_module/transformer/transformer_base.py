from typing import List, Dict
from docutils import nodes


class TransformerBase:

    # pylint: disable=W0613
    def __init__(self, documents: List[nodes.document], **kwargs):
        self.documents: List[nodes.document] = documents
        self.outputs: Dict = {}

    @classmethod
    def name(cls) -> str:
        raise NotImplementedError("Subclass must implement this method")

    def get_outputs(self) -> Dict:
        return self.outputs

    def apply(self, **kwargs):
        raise NotImplementedError("Subclass must implement this method")
