from docutils import nodes


class AttributeListNode(nodes.Element, nodes.Sequential):
    """
    <attribute-list>
        <attribute>
            <description/>
            <data-type-list>
                <data-type/>
                ...
            <name/>
        </attribute>
    </attribute-list>
    """

    tagname = "attribute-list"


class FunctionListNode(nodes.Element, nodes.Sequential):
    tagname = "function-list"


class NameNode(nodes.TextElement, nodes.Part):
    tagname = "name"


class DataTypeListNode(nodes.Element, nodes.Sequential):
    tagname = "data-type-list"


class DataTypeNode(nodes.TextElement, nodes.Part):
    tagname = "data-type"


class DescriptionNode(nodes.TextElement, nodes.Part):
    tagname = "description"


class DataNode(nodes.Element, nodes.Part):
    tagname = "data"


class AttributeNode(nodes.Element, nodes.Part):
    tagname = "attribute"


class DefaultValueNode(nodes.TextElement, nodes.Part):
    tagname = "default-value"


class ArgumentListNode(nodes.Element, nodes.Sequential):
    tagname = "argument-list"


class ArgumentNode(nodes.Element, nodes.Part):
    tagname = "argument"


class FunctionReturnNode(nodes.Element, nodes.Part):
    tagname = "return"


class FunctionNode(nodes.Element, nodes.Part):
    tagname = "function"


class BaseClassListNode(nodes.Element, nodes.Sequential):
    """
    <base-class-list>
        <base-class>
            <data-type/>
        </base-class>
        ...
    </base-class-list>
    """

    tagname = "base-class-list"


class BaseClassNode(nodes.Element, nodes.Part):
    tagname = "base-class"


class ClassNode(nodes.Element, nodes.Part):
    tagname = "class"


class ModuleNode(nodes.Element, nodes.Part):
    """
    <module>
        <name/>
        <description/>
    </module>
    """
    tagname = "module"


class CodeNode(nodes.TextElement, nodes.Part):
    tagname = "code"
