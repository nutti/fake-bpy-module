import re
from docutils import transforms
from docutils import nodes

from .analyzer.nodes import (
    ClassNode,
    AttributeNode,
    AttributeListNode,
    DataNode,
    BaseClassListNode,
    BaseClassNode,
    DataTypeListNode,
    DataTypeNode,
)
from . import common


class FakeBpyModuleTransformer(transforms.Transform):
    def apply(self, **kwargs):
        pass


class BaseClassFinder(FakeBpyModuleTransformer):
    _BASE_CLASS_REGEX = re.compile(r"^base (class|classes) --- (.*)")

    def apply(self, **kwargs):
        document: nodes.document = self.document

        paragraphs = list(document.findall(nodes.paragraph))
        for para in paragraphs:
            m = self._BASE_CLASS_REGEX.match(para.astext())
            if m:
                base_classes = common.split_string_by_comma(m.group(2))
                base_class_list_node = BaseClassListNode()
                for bc in base_classes:
                    base_class_node = BaseClassNode()
                    data_type_list_node = DataTypeListNode(
                        "", DataTypeNode(text=bc))
                    base_class_node.insert(0, data_type_list_node)
                    base_class_list_node.insert(0, base_class_node)
                class_nodes = list(document.findall(ClassNode))
                for class_node in class_nodes:
                    class_node.insert(0, base_class_list_node)
                para.parent.remove(para)
                break

# TODO: set optional flag from parameter description
# TODO: https://github.com/nutti/fake-bpy-module/issues/139
# TODO: test_bge_support_no_module

# class ModuleLevelAttributeNodeFinder(SubNodeVisitor):
#     def __init__(self, node: nodes.Node,
#             attribute_nodes: list[AttributeNode]):
#         assert isinstance(node, BaseClassNode)

#         super().__init__(node)
#         self.attribute_nodes: list[AttributeNode] = attribute_nodes

#     def visit_AttributeNode(self, node: AttributeNode):
#         if isinstance(node.parent, AttributeListNode

#         self.imm._data_type = data_type._data_type

#         raise nodes.SkipChildren


class AttributeToDataTransformer(FakeBpyModuleTransformer):
    def apply(self, **kwargs):
        document: nodes.document = self.document

        def is_module_level_attribute_node(node: nodes.Node):
            if not isinstance(node, AttributeNode):
                return False
            if isinstance(node.parent, AttributeListNode):
                return False
            return True

        attribute_nodes = document.findall(is_module_level_attribute_node)

        nodes_to_remove = []
        nodes_to_add = []
        for attr_node in attribute_nodes:
            data_node = DataNode()
            for c in attr_node.children:
                data_node.insert(len(data_node.children), c)

            nodes_to_remove.append(attr_node)
            nodes_to_add.append([data_node, attr_node.parent])

        for node in nodes_to_remove:
            node.parent.remove(node)
        for (node, parent) in nodes_to_add:
            parent.insert(len(document.children), node)
