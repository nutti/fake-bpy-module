from docutils import writers
from docutils import nodes

from ..common import (
    SectionInfo,
    ClassInfo,
    IntermidiateDataType,
    VariableInfo,
    FunctionInfo,
    ParameterDetailInfo,
    ReturnInfo,
)

from .analyzer.nodes import (
    ModuleNode,
    ClassNode,
    BaseClassNode,
    BaseClassListNode,
    AttributeNode,
    AttributeListNode,
    FunctionNode,
    FunctionListNode,
    ArgumentNode,
    ArgumentListNode,
    DefaultValueNode,
    FunctionReturnNode,
    DataNode,
    NameNode,
    DescriptionNode,
    DataTypeNode,
    DataTypeListNode,

    CodeNode,
    CodeDocumentNode,
)


class FakeBpyModuleImmWriter(writers.Writer):
    def __init__(self, document: nodes.document, imm: SectionInfo):
        super().__init__()

        self.translator_class = RstToFakeBpyModuleImmTranslator
        self.document = document
        self.imm = imm

    def translate(self):
        visitor = self.translator_class(self.document, self.imm)
        self.document.walk(visitor)


class SubNodeVisitor:
    # TODO: consider to use SparseNodeVisitor

    def __init__(self, node: nodes.Node):
        self.node = node

    def dispatch_visit(self, node: nodes.Node):
        node_name = node.__class__.__name__
        method = getattr(self, f"visit_{node_name}", self.unknown_visit)
        return method(node)

    def dispatch_depart(self, node: nodes.Node):
        node_name = node.__class__.__name__
        method = getattr(self, f"depart_{node_name}", self.unknown_depart)
        return method(node)

    def unknown_visit(self, node: nodes.Node):
        raise ValueError(
            f"{self.__class__} visiting unknown node type: "
            f"{node.__class__.__name__}\n\n{node.pformat()}")

    def unknown_depart(self, node: nodes.Node):
        raise ValueError(
            f"{self.__class__} departing unknown node type: "
            f"{node.__class__.__name__}\n\n{node.pformat()}")


def walk_sub_node(node: nodes.Node, visitor: SubNodeVisitor,
                  ignore_self: bool = True, call_depart: bool = False):
    should_stop = False

    try:
        if not ignore_self:
            visitor.dispatch_visit(node)
    except nodes.SkipChildren:
        return should_stop

    for child in node.children[:]:
        walk_sub_node(child, visitor, ignore_self=False, call_depart=call_depart)

    if call_depart and not ignore_self:
        visitor.dispatch_depart(node)

    return should_stop


class BaseClassNodeVisitor(SubNodeVisitor):
    def __init__(self, node: nodes.Node, imm: IntermidiateDataType):
        assert isinstance(node, BaseClassNode)

        super().__init__(node)
        self.imm: IntermidiateDataType = imm

    # pylint: disable=C0103
    def visit_BaseClassNode(self, node: BaseClassNode):
        pass

    # pylint: disable=C0103
    def visit_DataTypeListNode(self, node: DataTypeListNode):
        if not node.empty():
            data_type = IntermidiateDataType("")
            visitor = DataTypeListNodeVisitor(node, data_type)
            walk_sub_node(node, visitor)

            self.imm._data_type = data_type._data_type      # pylint: disable=W0212
            self.imm._skip_refine = data_type._skip_refine  # pylint: disable=W0212

        raise nodes.SkipChildren


# pylint: disable=C0103
class DataTypeListNodeVisitor(SubNodeVisitor):

    def __init__(self, node: nodes.Node, imm: IntermidiateDataType):
        assert isinstance(node, DataTypeListNode)

        super().__init__(node)
        self.imm: IntermidiateDataType = imm

    def visit_DataTypeListNode(self, node: DataTypeListNode):
        pass

    def visit_DataTypeNode(self, node: DataTypeNode):
        mod_options = []
        if "mod-option" in node.attributes:
            mod_options = [sp.strip() for sp in node.attributes["mod-option"].split(",")]
        if "skip-refine" in mod_options:
            self.imm._skip_refine = True    # pylint: disable=W0212
        self.imm._data_type = node.astext()     # pylint: disable=W0212

        raise nodes.SkipChildren


# pylint: disable=C0103
class AttributeNodeVisitor(SubNodeVisitor):
    def __init__(self, node: nodes.Node, imm: VariableInfo):
        assert isinstance(node, (DataNode, AttributeNode))

        super().__init__(node)
        self.imm: VariableInfo = imm

    def visit_AttributeNode(self, node: AttributeNode):
        pass

    def visit_DataNode(self, node: DataNode):
        pass

    def visit_NameNode(self, node: NameNode):
        self.imm.set_name(node.astext())
        raise nodes.SkipChildren

    def visit_DescriptionNode(self, node: DescriptionNode):
        self.imm.set_description(node.astext())
        raise nodes.SkipChildren

    def visit_DataTypeListNode(self, node: DataTypeListNode):
        if not node.empty():
            data_type = IntermidiateDataType("")
            visitor = DataTypeListNodeVisitor(node, data_type)
            walk_sub_node(node, visitor)

            self.imm.set_data_type(data_type)

        raise nodes.SkipChildren


class ArgumentNodeVisitor(SubNodeVisitor):
    def __init__(self, node: nodes.Node, imm: ParameterDetailInfo):
        assert isinstance(node, ArgumentNode)

        super().__init__(node)
        self.imm: ParameterDetailInfo = imm

    def visit_ArgumentNode(self, node: ArgumentNode):
        pass

    def visit_NameNode(self, node: NameNode):
        self.imm.set_name(node.astext())
        raise nodes.SkipChildren

    def visit_DescriptionNode(self, node: DescriptionNode):
        self.imm.set_description(node.astext())
        raise nodes.SkipChildren

    def visit_DefaultValueNode(self, node: DefaultValueNode):
        if not node.empty():
            self.imm.default_value = node.astext()
        raise nodes.SkipChildren

    def visit_DataTypeListNode(self, node: DataTypeListNode):
        if not node.empty():
            data_type = IntermidiateDataType("")
            visitor = DataTypeListNodeVisitor(node, data_type)
            walk_sub_node(node, visitor)

            self.imm._data_type = data_type     # pylint: disable=W0212

        raise nodes.SkipChildren


class FunctionReturnNodeVisitor(SubNodeVisitor):
    def __init__(self, node: nodes.Node, imm: ReturnInfo):
        assert isinstance(node, FunctionReturnNode)

        super().__init__(node)
        self.imm: ReturnInfo = imm

    def visit_FunctionReturnNode(self, node: FunctionNode):
        pass

    def visit_DescriptionNode(self, node: DescriptionNode):
        self.imm.set_description(node.astext())

        raise nodes.SkipChildren

    def visit_DataTypeListNode(self, node: DataTypeListNode):
        if not node.empty():
            data_type = IntermidiateDataType("")
            visitor = DataTypeListNodeVisitor(node, data_type)
            walk_sub_node(node, visitor)

            self.imm.set_data_type(data_type)

        raise nodes.SkipChildren


class FunctionNodeVisitor(SubNodeVisitor):
    def __init__(self, node: nodes.Node, imm: FunctionInfo):
        assert isinstance(node, FunctionNode)

        super().__init__(node)
        self.imm: FunctionInfo = imm

    def visit_FunctionNode(self, node: FunctionNode):
        pass

    def visit_NameNode(self, node: NameNode):
        self.imm.set_name(node.astext())
        raise nodes.SkipChildren

    def visit_DescriptionNode(self, node: DescriptionNode):
        self.imm.set_description(node.astext())
        raise nodes.SkipChildren

    def visit_ArgumentListNode(self, node: ArgumentListNode):
        start_kwarg = False
        for child in node.children:
            if isinstance(child, ArgumentNode):
                is_kwonlyarg = child.attributes["argument_type"] == "kwonlyarg"
                if not start_kwarg and is_kwonlyarg:
                    wildcard: ParameterDetailInfo = ParameterDetailInfo()
                    wildcard.set_name("*")
                    self.imm.add_parameter_detail(wildcard)
                    start_kwarg = True

                param_detail_info: ParameterDetailInfo = ParameterDetailInfo()
                visitor = ArgumentNodeVisitor(child, param_detail_info)
                walk_sub_node(child, visitor)

                if child.attributes["argument_type"] == "vararg":
                    param_detail_info.set_name(f"*{param_detail_info.name()}")
                if child.attributes["argument_type"] == "kwarg":
                    param_detail_info.set_name(
                        f"**{param_detail_info.name()}")

                self.imm.add_parameter_detail(param_detail_info)

        raise nodes.SkipChildren

    def visit_FunctionReturnNode(self, node: FunctionReturnNode):
        if not node.empty():
            return_info = ReturnInfo()
            visitor = FunctionReturnNodeVisitor(node, return_info)
            walk_sub_node(node, visitor)

            self.imm.set_return(return_info)

        raise nodes.SkipChildren


class RstToFakeBpyModuleImmTranslator(nodes.NodeVisitor):
    def __init__(self, document: nodes.document, imm: SectionInfo):
        super().__init__(document)
        self.imm: SectionInfo = imm
        self.module_name = None

    def visit_CodeDocumentNode(self, node: CodeDocumentNode):
        raise nodes.SkipChildren

    def visit_document(self, node: nodes.document):
        pass

    def visit_title(self, node: nodes.title):
        raise nodes.SkipChildren

    def visit_paragraph(self, node: nodes.paragraph):
        raise nodes.SkipChildren

    def visit_field_list(self, node: nodes.field_list):
        raise nodes.SkipChildren

    def visit_bullet_list(self, node: nodes.bullet_list):
        raise nodes.SkipChildren

    def visit_section(self, node: nodes.section):
        pass

    # TODO: below nodes can be handled by using rst visitor
    # https://github.com/sphinx-contrib/restbuilder/blob/c8b9c0d5764480d0433215504311f14895aa2215/sphinxcontrib/writers/rst.py#L52

    def visit_enumerated_list(self, node: nodes.enumerated_list):
        raise nodes.SkipChildren

    def visit_literal_block(self, node: nodes.literal_block):
        raise nodes.SkipChildren

    def visit_line_block(self, node: nodes.line_block):
        raise nodes.SkipChildren

    def visit_target(self, node: nodes.target):
        raise nodes.SkipChildren

    def visit_block_quote(self, node: nodes.target):
        raise nodes.SkipChildren

    def visit_CodeNode(self, node: CodeNode):
        raise nodes.SkipChildren

    def visit_warning(self, node: nodes.warning):
        raise nodes.SkipChildren

    def visit_note(self, node: nodes.note):
        raise nodes.SkipChildren

    def visit_definition_list(self, node: nodes.definition_list):
        raise nodes.SkipChildren

    def visit_rubric(self, node: nodes.rubric):
        raise nodes.SkipChildren

    ######

    def visit_ModuleNode(self, node: ModuleNode):
        for child in node.children:
            if isinstance(child, NameNode):
                self.module_name = child.astext()
        raise nodes.SkipChildren

    def visit_ClassNode(self, node: ClassNode):
        class_info: ClassInfo = ClassInfo()
        class_info.set_module(self.module_name)

        for child in node.children:
            if isinstance(child, BaseClassListNode):
                for base_class_node in child.children:
                    data_type = IntermidiateDataType("")
                    visitor = BaseClassNodeVisitor(base_class_node, data_type)
                    walk_sub_node(base_class_node, visitor)

                    class_info.add_base_class(data_type)
            elif isinstance(child, NameNode):
                class_info.set_name(child.astext())
            elif isinstance(child, DescriptionNode):
                class_info.append_description(child.astext())
            elif isinstance(child, AttributeListNode):
                for attr_node in child.children:
                    assert isinstance(attr_node, AttributeNode)

                    var_info = VariableInfo("attribute")
                    visitor = AttributeNodeVisitor(attr_node, var_info)
                    walk_sub_node(attr_node, visitor)

                    class_info.add_attribute(var_info)
            elif isinstance(child, FunctionListNode):
                for func_node in child.children:
                    assert isinstance(func_node, FunctionNode)

                    func_info = FunctionInfo("method")
                    visitor = FunctionNodeVisitor(func_node, func_info)
                    walk_sub_node(func_node, visitor)

                    class_info.add_method(func_info)

        # Set class name and module name to all attributes and methods.
        for attr in class_info.attributes():
            attr.set_module(class_info.module())
            attr.set_class(class_info.name())
        for method in class_info.methods():
            method.set_module(class_info.module())
            method.set_class(class_info.name())
            for param_detail in method.parameter_details():
                method.add_parameter(param_detail.name())

        self.imm.add_info(class_info)

        raise nodes.SkipChildren

    def visit_FunctionNode(self, node: FunctionNode):
        func_info = FunctionInfo("function")
        visitor = FunctionNodeVisitor(node, func_info)
        walk_sub_node(node, visitor)

        func_info.set_module(self.module_name)

        for param_detail in func_info.parameter_details():
            func_info.add_parameter(param_detail.name())

        self.imm.add_info(func_info)

        raise nodes.SkipChildren

    def visit_DataNode(self, node: DataNode):
        var_info = VariableInfo("constant")
        visitor = AttributeNodeVisitor(node, var_info)
        walk_sub_node(node, visitor)

        var_info.set_module(self.module_name)

        self.imm.add_info(var_info)

        raise nodes.SkipChildren
