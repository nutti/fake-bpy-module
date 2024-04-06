from typing import List
from docutils import nodes

from .transformer_base import TransformerBase
from ..analyzer.nodes import (
    ModuleNode,
    NameNode,
    ClassNode,
    FunctionNode,
    DataNode,
)
from ..analyzer.roles import (
    ClassRef,
)
from ..utils import get_first_child, find_children
from .utils import get_base_name, get_module_name, build_module_structure


class CannonicalDataTypeRewriter(TransformerBase):

    def __init__(self, documents: List[nodes.document], **kwargs):
        super().__init__(documents, **kwargs)

        self._package_structure = None
        if "package_structure" in kwargs:
            self._package_structure = kwargs["package_structure"]

    def _ensure_correct_data_type(self, data_type: str) -> str:
        mod_name = get_module_name(data_type, self._package_structure)
        base_name = get_base_name(data_type)

        ensured = f"{mod_name}.{base_name}"
        if ensured != data_type:
            raise RuntimeError(
                f"Invalid data type: ({data_type} vs {ensured})")

        return ensured

    def _get_generation_data_type(self, data_type: str,
                                  target_module: str) -> str:
        mod_names_full_1 = get_module_name(data_type, self._package_structure)
        mod_names_full_2 = target_module

        if mod_names_full_1 is None or mod_names_full_2 is None:
            # pylint: disable=W0511
            # TODO: should return better data_type
            return data_type

        mod_names_1 = mod_names_full_1.split(".")
        mod_names_2 = mod_names_full_2.split(".")

        for i, (m1, m2) in enumerate(zip(mod_names_1, mod_names_2)):
            if m1 != m2:
                match_level = i
                break
        else:
            if len(mod_names_1) >= len(mod_names_2):
                match_level = len(mod_names_2)
            else:
                match_level = len(mod_names_1)

        # [Case 1] No match => Use data_type
        #   data_type: bpy.types.Mesh
        #   target_module: bgl
        #       => bpy.types.Mesh
        if match_level == 0:
            final_data_type = self._ensure_correct_data_type(data_type)
        else:
            rest_level_1 = len(mod_names_1) - match_level
            rest_level_2 = len(mod_names_2) - match_level

            # [Case 2] Match exactly => Use data_type without module
            #   data_type: bgl.Buffer
            #   target_module: bgl
            #       => Buffer
            if rest_level_1 == 0 and rest_level_2 == 0:
                final_data_type = get_base_name(data_type)
            # [Case 3] Match partially (Same level) => Use data_type
            #   data_type: bpy.types.Mesh
            #   target_module: bpy.ops
            #       => bpy.types.Mesh
            elif rest_level_1 >= 1 and rest_level_2 >= 1:
                final_data_type = self._ensure_correct_data_type(data_type)
            # [Case 4] Match partially (Upper level) => Use data_type
            #   data_type: mathutils.Vector
            #   target_module: mathutils.noise
            #       => mathutils.Vector
            elif rest_level_1 == 0 and rest_level_2 >= 1:
                final_data_type = self._ensure_correct_data_type(data_type)
            # [Case 5] Match partially (Lower level) => Use data_type
            #   data_type: mathutils.noise.cell
            #   target_module: mathutils
            #       => mathutils.noise.cell
            elif rest_level_1 >= 1 and rest_level_2 == 0:
                final_data_type = self._ensure_correct_data_type(data_type)
            else:
                raise RuntimeError(
                    f"Should not reach this condition. ({rest_level_1} vs "
                    f"{rest_level_2})")

        return final_data_type

    def _rewrite(self, document: nodes.document):
        def rewrite(class_ref: ClassRef, module_name: str) -> ClassRef:
            class_name = class_ref.to_string()
            new_class_name = self._get_generation_data_type(
                class_name, module_name)
            new_class_ref = ClassRef(text=new_class_name)
            return new_class_ref

        def replace(from_node: nodes.Node, to_node: nodes.Node):
            parent = from_node.parent
            index = from_node.parent.index(from_node)
            parent.remove(from_node)
            parent.insert(index, to_node)

        module_node = get_first_child(document, ModuleNode)
        if module_node is None:
            return
        module_name = module_node.element(NameNode).astext()

        class_nodes = find_children(document, ClassNode)
        for class_node in class_nodes:
            class_refs = class_node.traverse(ClassRef)
            for class_ref in class_refs:
                new_class_ref = rewrite(class_ref, module_name)
                replace(class_ref, new_class_ref)

        func_nodes = find_children(document, FunctionNode)
        for func_node in func_nodes:
            class_refs = func_node.traverse(ClassRef)
            for class_ref in class_refs:
                new_class_ref = rewrite(class_ref, module_name)
                replace(class_ref, new_class_ref)

        data_nodes = find_children(document, DataNode)
        for data_node in data_nodes:
            class_refs = data_node.traverse(ClassRef)
            for class_ref in class_refs:
                new_class_ref = rewrite(class_ref, module_name)
                replace(class_ref, new_class_ref)

    @classmethod
    def name(cls) -> str:
        return "cannonical_data_type_rewriter"

    def apply(self, **kwargs):
        if self._package_structure is None:
            self._package_structure = build_module_structure(self.documents)

        for document in self.documents:
            self._rewrite(document)
