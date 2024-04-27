from typing import Union
from docutils import nodes

from .transformer_base import TransformerBase
from ..analyzer.nodes import (
    ModuleNode,
    ClassNode,
    FunctionNode,
    DataNode,
    NameNode,
    SourceFilenameNode,
    DescriptionNode,
    AttributeListNode,
    AttributeNode,
    DataTypeListNode,
    DataTypeNode,
    FunctionListNode,
    BaseClassListNode,
    BaseClassNode,
    ArgumentListNode,
    ArgumentNode,
    FunctionReturnNode,
    DefaultValueNode,
    CodeDocumentNode,
)
from ..analyzer.roles import (
    ClassRef,
    RefRef,
)


class FormatValidator(TransformerBase):

    def _check_num_children(self, node: nodes.Node, expect: int):
        assert len(node.children) == expect, f"{node.pformat()}"

    def _check_node(self, node: nodes.Node, expect_type: type):
        assert isinstance(node, expect_type), f"{node.pformat()}"

        type_to_check_func = {
            ModuleNode: self._check_module_node,
            FunctionListNode: self._check_function_list_node,
            FunctionNode: self._check_function_node,
            FunctionReturnNode: self._check_function_return_node,
            ArgumentListNode: self._check_argument_list_node,
            ArgumentNode: self._check_argument_node,
            AttributeListNode: self._check_attribute_list_node,
            AttributeNode: self._check_data_node,
            BaseClassListNode: self._check_base_class_list_node,
            BaseClassNode: self._check_base_class_node,
            NameNode: self._check_name_node,
            DescriptionNode: self._check_description_node,
            DataTypeListNode: self._check_data_type_list_node,
            DataTypeNode: self._check_data_type_node,
            DefaultValueNode: self._check_default_value_node,
            ClassRef: self._check_class_ref_node,
            RefRef: self._check_ref_ref_node,
            nodes.Text: self._check_text_node,
        }
        type_to_check_func[expect_type](node)

    def _check_text_node(self, text_node: nodes.Text):
        pass

    def _check_class_ref_node(self, class_ref_node: ClassRef):
        for child in class_ref_node.children:
            self._check_node(child, nodes.Text)

    def _check_ref_ref_node(self, ref_ref_node: RefRef):
        for child in ref_ref_node.children:
            self._check_node(child, nodes.Text)

    def _check_name_node(self, name_node: NameNode):
        for child in name_node.children:
            self._check_node(child, nodes.Text)

    def _check_description_node(self, description_node: DescriptionNode):
        for child in description_node.children:
            self._check_node(child, nodes.Text)

    def _check_data_type_node(self, data_type_node: DataTypeNode):
        for child in data_type_node.children:
            assert isinstance(child, (nodes.Text, ClassRef, RefRef,
                                      nodes.literal, nodes.emphasis,
                                      nodes.title_reference)), f"{child.pformat()}"

            if isinstance(child, (nodes.Text, nodes.literal, nodes.emphasis,
                                  nodes.title_reference)):
                for c in child.children:
                    self._check_node(c, nodes.Text)
            elif isinstance(child, ClassRef):
                self._check_node(child, ClassRef)
            elif isinstance(child, RefRef):
                self._check_node(child, RefRef)

    def _check_data_type_list_node(self, data_type_list_node: DataTypeListNode):
        for child in data_type_list_node.children:
            self._check_node(child, DataTypeNode)

    def _check_module_node(self, module_node: ModuleNode):
        self._check_num_children(module_node, 2)

        children = module_node.children
        self._check_node(children[0], NameNode)
        self._check_node(children[1], DescriptionNode)

    def _check_attribute_list_node(self,
                                   attribute_list_node: AttributeListNode):
        for attr_node in attribute_list_node.children:
            self._check_node(attr_node, AttributeNode)

    def _check_function_list_node(self, function_list_node: FunctionListNode):
        for func_node in function_list_node.children:
            self._check_node(func_node, FunctionNode)

    def _check_base_class_list_node(self,
                                    base_class_list_node: BaseClassListNode):
        for base_class_node in base_class_list_node.children:
            self._check_node(base_class_node, BaseClassNode)

    def _check_base_class_node(self, base_class_node: BaseClassNode):
        self._check_num_children(base_class_node, 1)

        self._check_node(base_class_node.children[0], DataTypeListNode)

    def _check_class_node(self, class_node: ClassNode):
        self._check_num_children(class_node, 5)

        children = class_node.children
        self._check_node(children[0], NameNode)
        self._check_node(children[1], DescriptionNode)
        self._check_node(children[2], BaseClassListNode)
        self._check_node(children[3], AttributeListNode)
        self._check_node(children[4], FunctionListNode)

    def _check_argument_node(self, argument_node: ArgumentNode):
        self._check_num_children(argument_node, 4)

        children = argument_node.children
        self._check_node(children[0], NameNode)
        self._check_node(children[1], DescriptionNode)
        self._check_node(children[2], DefaultValueNode)
        self._check_node(children[3], DataTypeListNode)

    def _check_default_value_node(self, default_value_node: DefaultValueNode):
        for child in default_value_node.children:
            self._check_node(child, nodes.Text)

    def _check_argument_list_node(self, argument_list_node: ArgumentListNode):
        for child in argument_list_node.children:
            self._check_node(child, ArgumentNode)

    def _check_function_return_node(self, return_node: FunctionReturnNode):
        self._check_num_children(return_node, 2)

        children = return_node.children
        self._check_node(children[0], DescriptionNode)
        self._check_node(children[1], DataTypeListNode)

    def _check_function_node(self, function_node: FunctionNode):
        self._check_num_children(function_node, 4)

        children = function_node.children
        self._check_node(children[0], NameNode)
        self._check_node(children[1], DescriptionNode)
        self._check_node(children[2], ArgumentListNode)
        self._check_node(children[3], FunctionReturnNode)

    def _check_data_node(self, data_node: Union[DataNode, AttributeNode]):
        self._check_num_children(data_node, 3)

        children = data_node.children
        self._check_node(children[0], NameNode)
        self._check_node(children[1], DescriptionNode)
        self._check_node(children[2], DataTypeListNode)

    def _check_paragraph_node(self, paragraph_node: nodes.paragraph):
        self._check_num_children(paragraph_node, 0)

    def _check_code_document_node(self, code_document_node: CodeDocumentNode):
        for child in code_document_node.children:
            assert not isinstance(child, (
                ModuleNode,
                FunctionListNode,
                FunctionNode,
                FunctionReturnNode,
                ArgumentListNode,
                ArgumentNode,
                AttributeListNode,
                AttributeNode,
                BaseClassListNode,
                BaseClassNode,
                NameNode,
                DescriptionNode,
                DataTypeListNode,
                DataTypeNode,
                DefaultValueNode
            )), f"{code_document_node.pformat()}"

    def _check_filename_node(self, source_filename_node: SourceFilenameNode):
        for child in source_filename_node.children:
            self._check_node(child, nodes.Text)

    def _check_document(self, document: nodes.document):
        for child in document.children:
            if isinstance(child, ModuleNode):
                self._check_module_node(child)
            elif isinstance(child, ClassNode):
                self._check_class_node(child)
            elif isinstance(child, FunctionNode):
                self._check_function_node(child)
            elif isinstance(child, DataNode):
                self._check_data_node(child)
            elif isinstance(child, CodeDocumentNode):
                self._check_code_document_node(child)
            elif isinstance(child, SourceFilenameNode):
                self._check_filename_node(child)
            else:
                raise ValueError(f"{type(child)} must not be a child of "
                                 f"{type(document)}.\n{document.pformat()}")

    def _apply(self, document: nodes.document):
        self._check_document(document)

    @classmethod
    def name(cls) -> str:
        return "format_validator"

    def apply(self, **kwargs):
        for document in self.documents:
            self._apply(document)
