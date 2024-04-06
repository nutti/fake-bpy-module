import os
from docutils import writers
from docutils import nodes

from ..analyzer.nodes import (
    ModuleNode,
    NameNode,
    DescriptionNode,
)


class PyiWriter(writers.Writer):
    def __init__(self, document: nodes.document):
        super().__init__()

        self.translator_class = RstToPyiTranslator
        self.document = document

    def translate(self):
        visitor = self.translator_class(self.document)
        self.document.walkabout(visitor)


# pylint: disable=C0103
class RstToPyiTranslator(nodes.NodeVisitor):
    def __init__(self, document):
        super().__init__(document)
        self.current_level = 0
        self.file = None

        self.target_dir = "result"
        os.makedirs(self.target_dir, exist_ok=True)

    def visit_document(self, _: nodes.document):
        pass

    def visit_ModuleNode(self, node: ModuleNode):
        # pylint: disable=R1732
        self.file = open(f"{self.target_dir}/{node.astext()}.pyi",
                         "w", encoding="utf-8")

    def depart_ModuleNode(self, _: ModuleNode):
        self.file.close()

    def visit_DescriptionNode(self, _: DescriptionNode):
        pass

    def depart_DescriptionNode(self, _: DescriptionNode):
        pass

    def visit_NameNode(self, _: NameNode):
        pass

    def depart_NameNode(self, _: NameNode):
        pass

    def visit_Text(self, _: nodes.Text):
        pass

    def depart_Text(self, _: nodes.Text):
        pass
