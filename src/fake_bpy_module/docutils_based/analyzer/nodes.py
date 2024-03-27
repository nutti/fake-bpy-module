from typing import TypeVar, Type
from docutils import nodes

from .roles import ClassRef
from ..common import append_child

T = TypeVar("T", bound=nodes.Node)


class NodeBase(nodes.Element):
    def append_child(self, item: nodes.Node):
        self.insert(len(self.children), item)


class UniqueElementNode(NodeBase):
    # pylint: disable=W1113
    def __init__(self, rawsource: str = "", *children: nodes.Node,
                 **attributes):
        super().__init__(rawsource, *children, **attributes)

        self.elements = {}

    def append_child(self, item: nodes.Node):
        self.insert(len(self.children), item)
        self.elements[type(item)] = item

    def element(self, element_type: Type[T]) -> T:
        return self.elements[element_type]

    def deepcopy(self):
        new_obj = super().deepcopy()
        new_obj.elements.clear()
        for child in new_obj.children:
            new_obj.elements[type(child)] = child
        return new_obj


class ListNode(NodeBase, nodes.Sequential):
    def empty(self) -> bool:
        return len(self.children) == 0


class TextNode(nodes.TextElement):
    def add_text(self, text: str):
        self.insert(len(self.children), nodes.Text(text))


class AttributeListNode(ListNode):
    tagname = "attribute-list"
    child_text_separator = ""


class FunctionListNode(ListNode):
    tagname = "function-list"
    child_text_separator = ""


class NameNode(TextNode, nodes.Part):
    tagname = "name"
    child_text_separator = ""


class DataTypeListNode(ListNode):
    tagname = "data-type-list"
    child_text_separator = ""


class DataTypeNode(TextNode, nodes.Part):
    tagname = "data-type"
    child_text_separator = ""

    def astext(self):
        return "".join(c.astext() for c in self.children)

    def to_string(self):
        s = ""
        for c in self.children:
            if isinstance(c, nodes.Text):
                s += c.astext()
            elif isinstance(c, ClassRef):
                s += c.to_string()
            else:
                raise NotImplementedError(f"{type(c)} is not supported")
        return s


class DescriptionNode(TextNode, nodes.Part):
    tagname = "description"
    child_text_separator = ""

    def empty(self) -> bool:
        return len(self.children) == 0


class DataNode(UniqueElementNode, nodes.Part):
    tagname = "data"
    child_text_separator = ""

    # pylint: disable=W1113
    @classmethod
    def create_template(cls, rawsource: str = "", *children: nodes.Node,
                        **attributes) -> "DataNode":
        node = DataNode(rawsource, *children, **attributes)

        node.append_child(NameNode())
        node.append_child(DescriptionNode())
        node.append_child(DataTypeListNode())

        return node


class AttributeNode(DataNode):
    tagname = "attribute"
    child_text_separator = ""

    # pylint: disable=W1113
    @classmethod
    def create_template(cls, rawsource: str = "", *children: nodes.Node,
                        **attributes) -> "AttributeNode":
        node = AttributeNode(rawsource, *children, **attributes)

        node.append_child(NameNode())
        node.append_child(DescriptionNode())
        node.append_child(DataTypeListNode())

        return node


class DefaultValueNode(TextNode, nodes.Part):
    tagname = "default-value"
    child_text_separator = ""

    def empty(self) -> bool:
        return len(self.children) == 0


class ArgumentListNode(ListNode):
    tagname = "argument-list"
    child_text_separator = ""


class ArgumentNode(UniqueElementNode, nodes.Part):
    tagname = "argument"
    child_text_separator = ""

    # pylint: disable=W1113
    @classmethod
    def create_template(cls, rawsource: str = "", *children: nodes.Node,
                        **attributes) -> "ArgumentNode":
        node = ArgumentNode(rawsource, *children, **attributes)

        node.append_child(NameNode())
        node.append_child(DescriptionNode())
        node.append_child(DefaultValueNode())
        node.append_child(DataTypeListNode())

        return node


class FunctionReturnNode(UniqueElementNode, nodes.Part):
    tagname = "return"
    child_text_separator = ""

    # pylint: disable=W1113
    @classmethod
    def create_template(cls, rawsource: str = "", *children: nodes.Node,
                        **attributes) -> "FunctionReturnNode":
        node = FunctionReturnNode(rawsource, *children, **attributes)

        node.append_child(DescriptionNode())
        node.append_child(DataTypeListNode())

        return node

    def empty(self) -> bool:
        for child in self.children:
            if not child.empty():
                return False
        return True


class FunctionNode(UniqueElementNode, nodes.Part):
    tagname = "function"
    child_text_separator = ""

    # pylint: disable=W1113
    @classmethod
    def create_template(cls, rawsource: str = "", *children: nodes.Node,
                        **attributes) -> "FunctionNode":
        node = FunctionNode(rawsource, *children, **attributes)

        node.append_child(NameNode())
        node.append_child(DescriptionNode())
        node.append_child(ArgumentListNode())
        node.append_child(FunctionReturnNode.create_template())

        return node


class BaseClassListNode(ListNode):
    tagname = "base-class-list"
    child_text_separator = ""


class BaseClassNode(UniqueElementNode, nodes.Part):
    tagname = "base-class"
    child_text_separator = ""

    # pylint: disable=W1113
    @classmethod
    def create_template(cls, rawsource: str = "", *children: nodes.Node,
                        **attributes) -> "BaseClassNode":
        node = BaseClassNode(rawsource, *children, **attributes)

        node.append_child(DataTypeListNode())

        return node


class ClassNode(UniqueElementNode, nodes.Part):
    tagname = "class"
    child_text_separator = ""

    # pylint: disable=W1113
    @classmethod
    def create_template(cls, rawsource: str = "", *children: nodes.Node,
                        **attributes) -> "ClassNode":
        node = ClassNode(rawsource, *children, **attributes)

        node.append_child(NameNode())
        node.append_child(DescriptionNode())
        node.append_child(BaseClassListNode())
        node.append_child(AttributeListNode())
        node.append_child(FunctionListNode())

        return node


class ModuleNode(UniqueElementNode, nodes.Part):
    tagname = "module"
    child_text_separator = ""

    # pylint: disable=W1113
    @classmethod
    def create_template(cls, rawsource: str = "", *children: nodes.Node,
                        **attributes) -> "ModuleNode":
        node = ModuleNode(rawsource, *children, **attributes)

        node.append_child(NameNode())
        node.append_child(DescriptionNode())

        return node


class CodeNode(TextNode, nodes.Part):
    tagname = "code"
    child_text_separator = ""


class ModTypeNode(TextNode, nodes.Part):
    tagname = "mod-type"
    child_text_separator = ""


class CodeDocumentNode(TextNode, nodes.Part):
    tagname = "code-document"
    child_text_separator = ""


def make_data_type_node(dtype_str: str) -> DataTypeNode:
    in_quote = False
    current_text = ""
    result = []
    for c in dtype_str:
        if c == "`":
            if in_quote:
                if current_text != "":
                    result.append(ClassRef(text=current_text))
                current_text = ""
                in_quote = False
            else:
                if current_text != "":
                    result.append(nodes.Text(current_text))
                current_text = ""
                in_quote = True
        else:
            current_text += c
    if current_text != "":
        result.append(nodes.Text(current_text))

    dtype_node = DataTypeNode()
    for r in result:
        append_child(dtype_node, r)

    return dtype_node
