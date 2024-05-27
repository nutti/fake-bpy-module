from typing import List
from docutils import nodes

from ..analyzer.nodes import (
    CodeNode,
    CodeDocumentNode,
)
from ..analyzer.roles import (
    ModuleRef,
    ClassRef,
    FunctionRef,
    MethodRef,
    ConstRef,
    DataRef,
    RefRef,
)
from .code_writer import (
    CodeWriter,
    CodeWriterIndent,
)


class Status:
    def __init__(self, status=None, parameters=None):
        self.kind = status
        self.parameters = parameters


# pylint: disable=C0103,R0904
class CodeDocumentNodeTranslator(nodes.SparseNodeVisitor):
    INDENT = "    "

    def __init__(self, document: nodes.document, doc_writer: CodeWriter):
        super().__init__(document)

        self.doc_writer: CodeWriter = doc_writer
        CodeWriterIndent.reset_indent()

        self.status_stack: List[Status] = []

    def get_list_level(self) -> int:
        c = 0
        for status in self.status_stack:
            if status.kind in ('BULLET_LIST', 'ENUMERATED_LIST'):
                c += 1
        return c

    def visit_CodeDocumentNode(self, _: CodeDocumentNode):
        self.doc_writer.addln('"""')

    def depart_CodeDocumentNode(self, _: CodeDocumentNode):
        self.doc_writer.addln('"""')

    def visit_title(self, _: nodes.title):
        raise nodes.SkipChildren

    def depart_title(self, _: nodes.title):
        pass

    def visit_section(self, _: nodes.section):
        self.doc_writer.new_line()

    def depart_section(self, _: nodes.section):
        self.doc_writer.addln("--------------------")
        self.doc_writer.new_line()

    def visit_Text(self, node: nodes.Text):
        lines = str(node).split("\n")
        for line in lines[:-1]:
            self.doc_writer.addln(line)
        self.doc_writer.add(lines[-1])

    def depart_Text(self, _: nodes.Text):
        pass

    def visit_emphasis(self, _: nodes.emphasis):
        self.doc_writer.add("*")

    def depart_emphasis(self, _: nodes.emphasis):
        self.doc_writer.add("*")

    def visit_paragraph(self, _: nodes.paragraph):
        pass

    def depart_paragraph(self, _: nodes.paragraph):
        new_line_num = 0
        if len(self.status_stack) >= 1:
            status = self.status_stack[-1]
            if status.kind in (
                'BULLET_LIST',
                'ENUMERATED_LIST',
                'NOTE',
                'WARNING',
                'BLOCK_QUOTE',
            ):
                new_line_num = 1
        else:
            new_line_num = 2

        if new_line_num >= 1:
            self.doc_writer.new_line(new_line_num)

    def visit_CodeNode(self, _: CodeNode):
        self.doc_writer.add("```")

    def depart_CodeNode(self, _: CodeNode):
        self.doc_writer.addln("```")
        self.doc_writer.new_line()

    def visit_bullet_list(self, _: nodes.bullet_list):
        level = self.get_list_level()
        self.status_stack.append(Status('BULLET_LIST', {"level": level}))

    def depart_bullet_list(self, _: nodes.bullet_list):
        status = self.status_stack.pop()
        assert status.kind == 'BULLET_LIST'

        if status.parameters["level"] == 0:
            self.doc_writer.new_line()

    def visit_enumerated_list(self, _: nodes.enumerated_list):
        level = self.get_list_level()
        self.status_stack.append(
            Status('ENUMERATED_LIST', {"number": 0, "level": level})
        )

    def depart_enumerated_list(self, _: nodes.enumerated_list):
        status = self.status_stack.pop()
        assert status.kind == 'ENUMERATED_LIST'

        if status.parameters["level"] == 0:
            self.doc_writer.new_line()

    def visit_field_list(self, _: nodes.field_list):
        self.status_stack.append(Status('FIELD_LIST'))

    def depart_field_list(self, _: nodes.field_list):
        status = self.status_stack.pop()
        assert status.kind == 'FIELD_LIST'

        self.doc_writer.new_line()

    def visit_field(self, _: nodes.field):
        self.status_stack.append(Status('FIELD'))

    def depart_field(self, _: nodes.field):
        status = self.status_stack.pop()
        assert status.kind == 'FIELD'

        self.doc_writer.new_line()

    def visit_field_name(self, _: nodes.field_name):
        status = self.status_stack[-1]
        assert status.kind == 'FIELD'

    def depart_field_name(self, _: nodes.field_name):
        status = self.status_stack[-1]
        assert status.kind == 'FIELD'

        self.doc_writer.add(": ")

    def visit_field_body(self, _: nodes.field_body):
        status = self.status_stack[-1]
        assert status.kind == 'FIELD'

    def depart_field_body(self, _: nodes.field_body):
        status = self.status_stack[-1]
        assert status.kind == 'FIELD'

    def visit_definition_list(self, _: nodes.definition_list):
        self.status_stack.append(Status('DEFINITION_LIST'))

    def depart_definition_list(self, _: nodes.definition_list):
        status = self.status_stack.pop()
        assert status.kind == 'DEFINITION_LIST'

    def visit_list_item(self, _: nodes.list_item):
        status = self.status_stack[-1]
        if status.kind == 'BULLET_LIST':
            if status.parameters["level"] >= 1:
                CodeWriterIndent.add_indent(1, True)
            self.doc_writer.add("* ")
        elif status.kind == 'ENUMERATED_LIST':
            num = status.parameters["number"] + 1
            status.parameters["number"] = num
            if status.parameters["level"] >= 1:
                CodeWriterIndent.add_indent(1, True)
            self.doc_writer.add(f"{num}. ")
        assert status.kind in ('BULLET_LIST', 'ENUMERATED_LIST'), status.kind

    def depart_list_item(self, _: nodes.list_item):
        status = self.status_stack[-1]
        assert status.kind in ('BULLET_LIST', 'ENUMERATED_LIST'), status.kind
        if status.parameters["level"] >= 1:
            CodeWriterIndent.remove_indent()

    def visit_definition_list_item(self, _: nodes.definition_list_item):
        status = self.status_stack[-1]
        assert status.kind == 'DEFINITION_LIST'

    def depart_definition_list_item(self, _: nodes.definition_list_item):
        status = self.status_stack[-1]
        assert status.kind == 'DEFINITION_LIST'

        self.doc_writer.new_line()

    def visit_term(self, _: nodes.term):
        status = self.status_stack[-1]
        assert status.kind == 'DEFINITION_LIST'

    def depart_term(self, _: nodes.term):
        status = self.status_stack[-1]
        assert status.kind == 'DEFINITION_LIST'

        self.doc_writer.new_line()

    def visit_definition(self, _: nodes.definition):
        status = self.status_stack[-1]
        assert status.kind == 'DEFINITION_LIST'

        CodeWriterIndent.add_indent(1, True)

    def depart_definition(self, _: nodes.definition):
        status = self.status_stack[-1]
        assert status.kind == 'DEFINITION_LIST'

        self.doc_writer.new_line()
        CodeWriterIndent.remove_indent()

    def visit_literal(self, _: nodes.literal):
        self.status_stack.append(Status('LITERAL'))

    def depart_literal(self, _: nodes.literal):
        status = self.status_stack.pop()
        assert status.kind == 'LITERAL'
        self.doc_writer.new_line(2)

    def visit_literal_block(self, _: nodes.literal_block):
        self.status_stack.append(Status('LITERAL_BLOCK'))
        self.doc_writer.addln("```")

    def depart_literal_block(self, _: nodes.literal_block):
        status = self.status_stack.pop()
        assert status.kind == 'LITERAL_BLOCK'
        self.doc_writer.new_line()
        self.doc_writer.addln("```")
        self.doc_writer.new_line()

    def visit_ModuleRef(self, node: ModuleRef):
        self.doc_writer.add(node.to_string())
        raise nodes.SkipChildren

    def depart_ModuleRef(self, _: ModuleRef):
        pass

    def visit_RefRef(self, node: RefRef):
        self.doc_writer.add(node.to_string())
        raise nodes.SkipChildren

    def depart_RefRef(self, _: RefRef):
        pass

    def visit_ClassRef(self, node: ClassRef):
        self.doc_writer.add(node.to_string())
        raise nodes.SkipChildren

    def depart_ClassRef(self, _: ClassRef):
        pass

    def visit_FunctionRef(self, node: FunctionRef):
        self.doc_writer.add(node.to_string())
        raise nodes.SkipChildren

    def depart_FunctionRef(self, _: FunctionRef):
        pass

    def visit_MethodRef(self, node: MethodRef):
        self.doc_writer.add(node.to_string())
        raise nodes.SkipChildren

    def depart_MethodRef(self, _: MethodRef):
        pass

    def visit_DataRef(self, node: DataRef):
        self.doc_writer.add(node.to_string())
        raise nodes.SkipChildren

    def depart_DataRef(self, _: DataRef):
        pass

    def visit_ConstRef(self, node: ConstRef):
        self.doc_writer.add(node.to_string())
        raise nodes.SkipChildren

    def depart_ConstRef(self, _: ConstRef):
        pass

    def visit_note(self, _: nodes.note):
        self.status_stack.append(Status('NOTE'))
        self.doc_writer.addln("[NOTE]")

    def depart_note(self, _: nodes.note):
        status = self.status_stack.pop()
        assert status.kind == 'NOTE'

        self.doc_writer.new_line(1)

    def visit_warning(self, _: nodes.warning):
        self.status_stack.append(Status('WARNING'))
        self.doc_writer.addln("[WARNING]")

    def depart_warning(self, _: nodes.warning):
        status = self.status_stack.pop()
        assert status.kind == 'WARNING'

        self.doc_writer.new_line(1)

    def visit_block_quote(self, _: nodes.block_quote):
        self.status_stack.append(Status('BLOCK_QUOTE'))
        self.doc_writer.addln("[QUOTE]")

    def depart_block_quote(self, _: nodes.block_quote):
        status = self.status_stack.pop()
        assert status.kind == 'BLOCK_QUOTE'
        self.doc_writer.new_line(1)

    def visit_line_block(self, _: nodes.line_block):
        self.status_stack.append(Status('LINE_BLOCK'))

    def depart_line_block(self, _: nodes.line_block):
        status = self.status_stack.pop()
        assert status.kind == 'LINE_BLOCK'

        self.doc_writer.new_line()

    def visit_line(self, _: nodes.line):
        status = self.status_stack[-1]
        assert status.kind == 'LINE_BLOCK'

    def depart_line(self, _: nodes.line):
        status = self.status_stack[-1]
        assert status.kind == 'LINE_BLOCK'

        self.doc_writer.new_line()

    def visit_reference(self, _: nodes.reference):
        pass

    def depart_reference(self, _: nodes.reference):
        pass

    def visit_target(self, _: nodes.target):
        pass

    def depart_target(self, _: nodes.target):
        pass

    def visit_inline(self, _: nodes.inline):
        pass

    def depart_inline(self, _: nodes.inline):
        pass
