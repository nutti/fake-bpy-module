from docutils import nodes


class TransformerBase:

    # pylint: disable=W0613
    def __init__(self, documents: list[nodes.document], **kwargs) -> None:
        self.documents: list[nodes.document] = documents
        self.outputs: dict = {}

    @classmethod
    def name(cls: type['TransformerBase']) -> str:
        raise NotImplementedError("Subclass must implement this method")

    def get_outputs(self) -> dict:
        return self.outputs

    def apply(self, **kwargs):
        raise NotImplementedError("Subclass must implement this method")
