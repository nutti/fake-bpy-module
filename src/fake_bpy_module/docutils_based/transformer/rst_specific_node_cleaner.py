from typing import List
from docutils import nodes

from .transformer_base import TransformerBase
from ..analyzer.nodes import (
    DescriptionNode,
    ModuleNode,
    AttributeListNode,
    FunctionListNode,
    NameNode,
    DataTypeListNode,
    DataTypeNode,
    DataNode,
    AttributeNode,
    DefaultValueNode,
    ArgumentListNode,
    ArgumentNode,
    FunctionReturnNode,
    FunctionNode,
    BaseClassListNode,
    BaseClassNode,
    ClassNode,
    CodeDocumentNode,
    CodeNode,
)
from ..analyzer.roles import (
    ClassRef,
    ModuleRef,
    ConstRef,
    FunctionRef,
    RefRef,
    DataRef,
)
from ..common import append_child
from ..compat import SubNodeVisitor, walk_sub_node


# pylint: disable=C0103,R0904
class RstSpecificDocNodeTranslator(SubNodeVisitor):
    def __init__(self, document: nodes.Node, code_doc_node: CodeDocumentNode):
        super().__init__(document)
        self.code_doc_node: CodeDocumentNode = code_doc_node
        self.status_stack: List[str] = []

    def visit_Text(self, node: nodes.Text):
        append_child(self.code_doc_node, node)

    def depart_Text(self, _: nodes.Text):
        pass

    def visit_section(self, node: nodes.section):
        append_child(self.code_doc_node, nodes.Text(node.astext()))

    def depart_section(self, _: nodes.section):
        pass

    def visit_paragraph(self, _: nodes.paragraph):
        pass

    def depart_paragraph(self, _: nodes.paragraph):
        pass

    def visit_title_reference(self, _: nodes.title_reference):
        pass

    def depart_title_reference(self, _: nodes.title_reference):
        pass

    def visit_strong(self, _: nodes.strong):
        append_child(self.code_doc_node, nodes.Text("**"))

    def depart_strong(self, _: nodes.strong):
        append_child(self.code_doc_node, nodes.Text("**"))

    def visit_emphasis(self, _: nodes.emphasis):
        append_child(self.code_doc_node, nodes.Text("*"))

    def depart_emphasis(self, _: nodes.emphasis):
        append_child(self.code_doc_node, nodes.Text("*"))

    def visit_reference(self, _: nodes.reference):
        pass

    def depart_reference(self, _: nodes.reference):
        pass

    def visit_ClassRef(self, node: ClassRef):
        append_child(self.code_doc_node, nodes.Text(node.astext()))

    def depart_ClassRef(self, _: ClassRef):
        pass

    def visit_FunctionRef(self, node: FunctionRef):
        append_child(self.code_doc_node, nodes.Text(node.astext()))

    def depart_FunctionRef(self, _: FunctionRef):
        pass

    def visit_ModuleRef(self, node: ModuleRef):
        append_child(self.code_doc_node, nodes.Text(node.astext()))

    def depart_ModuleRef(self, _: ModuleRef):
        pass

    def visit_ConstRef(self, node: ConstRef):
        append_child(self.code_doc_node, nodes.Text(node.astext()))

    def depart_ConstRef(self, _: ConstRef):
        pass

    def visit_RefRef(self, node: RefRef):
        append_child(self.code_doc_node, nodes.Text(node.astext()))

    def depart_RefRef(self, _: RefRef):
        pass

    def visit_DataRef(self, node: DataRef):
        append_child(self.code_doc_node, nodes.Text(node.astext()))

    def depart_DataRef(self, _: DataRef):
        pass

    def visit_list_item(self, _: nodes.list_item):
        current_status = self.status_stack[-1]
        if current_status == 'BULLET_LIST':
            append_child(self.code_doc_node, nodes.Text("*"))

    def depart_list_item(self, _: nodes.list_item):
        current_status = self.status_stack[-1]
        if current_status == 'BULLET_LIST':
            append_child(self.code_doc_node, nodes.Text("\n"))

    def visit_bullet_list(self, _: nodes.bullet_list):
        self.status_stack.append('BULLET_LIST')

    def depart_bullet_list(self, _: nodes.bullet_list):
        status = self.status_stack.pop()
        assert status == 'BULLET_LIST'

    def visit_literal(self, _: nodes.literal):
        self.status_stack.append('LITERAL')
        append_child(self.code_doc_node, nodes.Text("`"))

    def depart_literal(self, _: nodes.literal):
        status = self.status_stack.pop()
        assert status == 'LITERAL'
        append_child(self.code_doc_node, nodes.Text("`"))

    def visit_line_block(self, _: nodes.line_block):
        self.status_stack.append('LINE_BLOCK')

    def depart_line_block(self, _: nodes.line_block):
        status = self.status_stack.pop()
        assert status == 'LINE_BLOCK'

    def visit_line(self, _: nodes.line):
        pass

    def depart_line(self, _: nodes.line):
        pass

    def visit_target(self, _: nodes.target):
        pass

    def depart_target(self, _: nodes.target):
        pass

    def visit_literal_block(self, _: nodes.literal_block):
        self.status_stack.append('LITERAL_BLOCK')
        append_child(self.code_doc_node, nodes.Text("```\n"))

    def depart_literal_block(self, _: nodes.literal_block):
        status = self.status_stack.pop()
        assert status == 'LITERAL_BLOCK'
        append_child(self.code_doc_node, nodes.Text("```\n"))

    def visit_inline(self, _: nodes.inline):
        pass

    def depart_inline(self, _: nodes.inline):
        pass

    def visit_block_quote(self, _: nodes.block_quote):
        self.status_stack.append('BLOCK_QUOTE')

    def depart_block_quote(self, _: nodes.block_quote):
        status = self.status_stack.pop()
        assert status == 'BLOCK_QUOTE'

    def visit_definition_list(self, _: nodes.definition_list):
        self.status_stack.append('DEFINITION_LIST')

    def depart_definition_list(self, _: nodes.definition_list):
        status = self.status_stack.pop()
        assert status == 'DEFINITION_LIST'

    def visit_definition_list_item(self, _: nodes.definition_list_item):
        pass

    def depart_definition_list_item(self, _: nodes.definition_list_item):
        pass

    def visit_enumerated_list(self, _: nodes.enumerated_list):
        self.status_stack.append('ENUMERATED_LIST')

    def depart_enumerated_list(self, _: nodes.enumerated_list):
        status = self.status_stack.pop()
        assert status == 'ENUMERATED_LIST'

    def visit_field_list(self, _: nodes.field_list):
        self.status_stack.append('FIELD_LIST')

    def depart_field_list(self, _: nodes.field_list):
        status = self.status_stack.pop()
        assert status == 'FIELD_LIST'

    def visit_field(self, _: nodes.field):
        self.status_stack.append('FIELD')

    def depart_field(self, _: nodes.field):
        status = self.status_stack.pop()
        assert status == 'FIELD'

    def visit_field_name(self, _: nodes.field_name):
        pass

    def depart_field_name(self, _: nodes.field_name):
        pass

    def visit_field_body(self, _: nodes.field_body):
        pass

    def depart_field_body(self, _: nodes.field_body):
        pass

    def visit_title(self, _: nodes.title):
        append_child(self.code_doc_node, nodes.Text("==================\n"))

    def depart_title(self, _: nodes.title):
        append_child(self.code_doc_node, nodes.Text("==================\n"))

    def visit_note(self, _: nodes.note):
        self.status_stack.append('NOTE')
        append_child(self.code_doc_node, nodes.Text("NOTE:\n"))

    def depart_note(self, _: nodes.note):
        status = self.status_stack.pop()
        assert status == 'NOTE'

    def visit_warning(self, _: nodes.warning):
        self.status_stack.append('WARNING')
        append_child(self.code_doc_node, nodes.Text("WARNING:\n"))

    def depart_warning(self, _: nodes.warning):
        status = self.status_stack.pop()
        assert status == 'WARNING'

    def visit_CodeNode(self, _: CodeNode):
        append_child(self.code_doc_node, nodes.Text("CODE:"))

    def depart_CodeNode(self, _: CodeNode):
        pass

    def visit_term(self, _: nodes.term):
        pass

    def depart_term(self, _: nodes.term):
        pass

    def visit_definition(self, _: nodes.definition):
        pass

    def depart_definition(self, _: nodes.definition):
        pass


class RstSpecificNodeTranslator(SubNodeVisitor):
    def visit_Text(self, _: nodes.Text):
        pass

    def visit_document(self, _: nodes.document):
        pass

    def visit_ModuleNode(self, _: ModuleNode):
        pass

    def visit_AttributeListNode(self, _: AttributeListNode):
        pass

    def visit_FunctionListNode(self, _: FunctionListNode):
        pass

    def visit_NameNode(self, _: NameNode):
        pass

    def visit_DataTypeListNode(self, _: DataTypeListNode):
        pass

    def visit_DataTypeNode(self, _: DataTypeNode):
        pass

    def visit_DescriptionNode(self, _: DescriptionNode):
        pass

    def visit_DataNode(self, _: DataNode):
        pass

    def visit_AttributeNode(self, _: AttributeNode):
        pass

    def visit_DefaultValueNode(self, _: DefaultValueNode):
        pass

    def visit_ArgumentListNode(self, _: ArgumentListNode):
        pass

    def visit_ArgumentNode(self, _: ArgumentNode):
        pass

    def visit_FunctionReturnNode(self, _: FunctionReturnNode):
        pass

    def visit_FunctionNode(self, _: FunctionNode):
        pass

    def visit_BaseClassListNode(self, _: BaseClassListNode):
        pass

    def visit_BaseClassNode(self, _: BaseClassNode):
        pass

    def visit_ClassNode(self, _: ClassNode):
        pass

    def parse_doc_node(self, node: nodes.Node):
        code_doc_node = CodeDocumentNode()

        visitor = RstSpecificDocNodeTranslator(node, code_doc_node)
        walk_sub_node(node, visitor, ignore_self=False, call_depart=True)

        return code_doc_node

    def visit_bullet_list(self, node: nodes.bullet_list):
        code_doc_node = self.parse_doc_node(node)
        self.replace(node, code_doc_node)

        raise nodes.SkipChildren

    def visit_definition_list(self, node: nodes.definition_list):
        code_doc_node = self.parse_doc_node(node)
        self.replace(node, code_doc_node)

        raise nodes.SkipChildren

    def visit_line_block(self, node: nodes.line_block):
        code_doc_node = self.parse_doc_node(node)
        self.replace(node, code_doc_node)

        raise nodes.SkipChildren

    def visit_literal_block(self, node: nodes.literal_block):
        code_doc_node = self.parse_doc_node(node)
        self.replace(node, code_doc_node)

        raise nodes.SkipChildren

    def visit_enumerated_list(self, node: nodes.enumerated_list):
        code_doc_node = self.parse_doc_node(node)
        self.replace(node, code_doc_node)

        raise nodes.SkipChildren

    def visit_field_list(self, node: nodes.field_list):
        code_doc_node = self.parse_doc_node(node)
        self.replace(node, code_doc_node)

        raise nodes.SkipChildren

    def visit_target(self, node: nodes.target):
        code_doc_node = self.parse_doc_node(node)
        self.replace(node, code_doc_node)

        raise nodes.SkipChildren

    def visit_block_quote(self, node: nodes.block_quote):
        code_doc_node = self.parse_doc_node(node)
        self.replace(node, code_doc_node)

        raise nodes.SkipChildren

    def visit_title(self, node: nodes.title):
        code_doc_node = self.parse_doc_node(node)
        self.replace(node, code_doc_node)

        raise nodes.SkipChildren

    def visit_paragraph(self, node: nodes.paragraph):
        code_doc_node = self.parse_doc_node(node)
        self.replace(node, code_doc_node)

        raise nodes.SkipChildren

    def visit_warning(self, node: nodes.warning):
        code_doc_node = self.parse_doc_node(node)
        self.replace(node, code_doc_node)

        raise nodes.SkipChildren

    def visit_note(self, node: nodes.note):
        code_doc_node = self.parse_doc_node(node)
        self.replace(node, code_doc_node)

        raise nodes.SkipChildren

    def visit_CodeNode(self, node: CodeNode):
        code_doc_node = self.parse_doc_node(node)
        self.replace(node, code_doc_node)

        raise nodes.SkipChildren

    def visit_section(self, node: nodes.section):
        parent = node.parent
        index = parent.index(node)
        for i, child in enumerate(node.children[:]):
            parent.insert(index + i + 1, child)
            node.remove(child)

        code_doc_node = self.parse_doc_node(node)
        self.replace(node, code_doc_node)

    def replace(self, from_node: nodes.Node, to_node: nodes.Node):
        parent = from_node.parent
        index = from_node.parent.index(from_node)
        parent.remove(from_node)
        parent.insert(index, to_node)


class RstSpecificNodeCleaner(TransformerBase):

    def _replace(self, from_node: nodes.Node, to_node: nodes.Node):
        parent = from_node.parent
        index = from_node.parent.index(from_node)
        parent.remove(from_node)
        parent.insert(index, to_node)

    def _apply(self, document: nodes.document):
        # Move to the upper node under the section node.
        for section_node in document.traverse(nodes.section):
            parent = section_node.parent
            index = parent.index(section_node)
            for i, child in enumerate(section_node.children[:]):
                parent.insert(index + i + 1, child)
                section_node.remove(child)

        # Make CodeDocumentNode from RST specific nodes.
        for node in document.children[:]:
            if isinstance(node, (
                    nodes.title,
                    nodes.paragraph,
                    nodes.bullet_list,
                    nodes.enumerated_list,
                    nodes.definition_list,
                    nodes.block_quote,
                    nodes.line_block,
                    nodes.literal_block,
                    nodes.section,
                    nodes.field_list,
                    nodes.note,
                    nodes.warning,
                    nodes.target,
                    CodeNode)):
                code_doc_node = CodeDocumentNode()
                self._replace(node, code_doc_node)
                append_child(code_doc_node, node)

    @classmethod
    def name(cls) -> str:
        return "rst_specific_node_cleaner"

    def apply(self, **kwargs):
        for document in self.documents:
            self._apply(document)
