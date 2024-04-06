from typing import List
from docutils import nodes

from .transformer_base import TransformerBase
from ..analyzer.nodes import (
    ModuleNode,
    NameNode,
    ClassNode,
    FunctionNode,
    DataNode,
    DependencyListNode,
    DependencyNode,
)
from ..analyzer.roles import (
    ClassRef,
)
from ..utils import get_first_child, find_children, append_child
from .utils import ModuleStructure, get_module_name, get_base_name, build_module_structure


class Dependency:
    def __init__(self):
        self._mod_name: str = None
        self._type_lists: List[str] = []

    @property
    def mod_name(self) -> str:
        if self._mod_name is None:
            raise RuntimeError("Must specify module name")
        return self._mod_name

    @mod_name.setter
    def mod_name(self, value: str):
        self._mod_name = value

    @property
    def type_lists(self) -> List[str]:
        if not self._type_lists:
            raise RuntimeError(
                "At least 1 element must be added to type lists")
        return self._type_lists

    def add_type(self, type_: str):
        self._type_lists.append(type_)


class DependencyBuilder(TransformerBase):

    def __init__(self, documents: List[nodes.document], **kwargs):
        super().__init__(documents, **kwargs)
        self._package_structure: ModuleStructure = None
        if "package_structure" in kwargs:
            self._package_structure = kwargs["package_structure"]

    def _get_import_module_path(self, module_structure: ModuleStructure,
                                data_type_1: str, data_type_2: str):
        mod_names_full_1 = get_module_name(data_type_1, module_structure)
        mod_names_full_2 = get_module_name(data_type_2, module_structure)
        if mod_names_full_1 is None or mod_names_full_2 is None:
            return None

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

        # [Case 1] No match => Need to import top level module
        #   data_type_1: bpy.types.Mesh
        #   data_type_2: bgl.glCallLists()
        #       => bpy.types
        if match_level == 0:
            module_path = ".".join(mod_names_1)
        else:
            rest_level_1 = len(mod_names_1) - match_level
            rest_level_2 = len(mod_names_2) - match_level

            # [Case 2] Match exactly => No need to import any modules
            #   data_type_1: bgl.Buffer
            #   data_type_2: bgl.glCallLists()
            #       => None
            if rest_level_1 == 0 and rest_level_2 == 0:
                module_path = None
            # [Case 3] Match partially (Same level)
            #               => Need to import top level
            #   data_type_1: bpy.types.Mesh
            #   data_type_2: bpy.ops.automerge()
            #       => bpy.types
            elif rest_level_1 >= 1 and rest_level_2 >= 1:
                module_path = ".".join(mod_names_1)
            # [Case 4] Match partially (Upper level)
            #               => Need to import top level
            #   data_type_1: mathutils.Vector
            #   data_type_2: mathutils.noise.cell
            #       => mathutils
            elif rest_level_1 == 0 and rest_level_2 >= 1:
                module_path = ".".join(mod_names_1)
            # [Case 5] Match partially (Lower level)
            #               => Need to import top level
            #   data_type_1: mathutils.noise.cell
            #   data_type_2: mathutils.Vector
            #       => mathutils.noise
            elif rest_level_1 >= 1 and rest_level_2 == 0:
                module_path = ".".join(mod_names_1)
            else:
                raise RuntimeError("Should not reach this condition.")

        return module_path

    def _add_dependency(self, dependencies: List[Dependency],
                        module_structure: ModuleStructure,
                        data_type_1: str, data_type_2: str):

        mod = self._get_import_module_path(module_structure, data_type_1, data_type_2)
        base = get_base_name(data_type_1)
        if mod is None:
            return

        target_dep = None
        for dep in dependencies:
            if dep.mod_name == mod:
                target_dep = dep
                break
        if target_dep is None:
            target_dep = Dependency()
            target_dep.mod_name = mod
            target_dep.add_type(base)
            dependencies.append(target_dep)
        else:
            if base not in target_dep.type_lists:
                target_dep.add_type(base)

    def _build_dependencies(
            self, document: nodes.document, package_structure: ModuleStructure):

        dependencies: List[Dependency] = []
        module_node = get_first_child(document, ModuleNode)
        if module_node is None:
            return
        module_name = module_node.element(NameNode).astext()

        class_nodes = find_children(document, ClassNode)
        for class_node in class_nodes:
            class_name = class_node.element(NameNode).astext()
            class_refs = class_node.traverse(ClassRef)
            for class_ref in class_refs:
                self._add_dependency(
                    dependencies, package_structure, class_ref.to_string(),
                    f"{module_name}.{class_name}")

        func_nodes = find_children(document, FunctionNode)
        for func_node in func_nodes:
            func_name = func_node.element(NameNode).astext()
            class_refs = func_node.traverse(ClassRef)
            for class_ref in class_refs:
                self._add_dependency(
                    dependencies, package_structure, class_ref.to_string(),
                    f"{module_name}.{func_name}")

        data_nodes = find_children(document, DataNode)
        for data_node in data_nodes:
            data_name = data_node.element(NameNode).astext()
            class_refs = data_node.traverse(ClassRef)
            for class_ref in class_refs:
                self._add_dependency(
                    dependencies, package_structure, class_ref.to_string(),
                    f"{module_name}.{data_name}")

        dep_list_node = DependencyListNode()
        for dep in dependencies:
            assert dep.mod_name[0] != "."
            dep_node = DependencyNode(text=dep.mod_name)
            dep_list_node.append_child(dep_node)
        append_child(document, dep_list_node)

    @classmethod
    def name(cls) -> str:
        return "dependency_builder"

    def apply(self, **kwargs):
        if self._package_structure is None:
            structure = build_module_structure(self.documents)
        else:
            structure = self._package_structure

        for document in self.documents:
            self._build_dependencies(document, structure)
