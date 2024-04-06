from typing import List
from docutils import nodes

from ..analyzer.nodes import (
    ModuleNode,
    NameNode,
)
from ..utils import get_first_child


class ModuleStructure:
    def __init__(self):
        self._name: str = None
        self._children: List['ModuleStructure'] = []

    @property
    def name(self) -> str:
        # this is a root of structure. name of root is None
        if self._name is None:
            raise RuntimeError("name must not call when self._name is None")
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    def add_child(self, child: 'ModuleStructure'):
        self._children.append(child)

    def children(self) -> List['ModuleStructure']:
        return self._children

    def to_dict(self) -> dict:
        def to_dict_internal(c: List[dict], psc: List['ModuleStructure']):
            for p in psc:
                nd = {"name": p.name, "children": []}
                to_dict_internal(nd["children"], p.children())
                c.append(nd)

        result = {"name": self._name, "children": []}
        to_dict_internal(result["children"], self._children)

        return result


def build_module_structure(documents: List[nodes.document]) -> 'ModuleStructure':
    def build(mod_name: str, structure_: ModuleStructure):
        sp = mod_name.split(".")
        for i in structure_.children():
            if i.name == sp[0]:
                item = i
                break
        else:
            item = ModuleStructure()
            item.name = sp[0]
            structure_.add_child(item)
        if len(sp) >= 2:
            s = ".".join(sp[1:])
            build(s, item)

    # Collect modules.
    modules = []
    for document in documents:
        module_node = get_first_child(document, ModuleNode)
        if module_node is None:
            continue
        module_name_node = module_node.element(NameNode)
        modules.append(module_name_node.astext())

    # Build module structure.
    structure = ModuleStructure()
    for m in modules:
        build(m, structure)
    return structure


def get_base_name(data_type: str) -> str:
    if data_type is None:
        return None

    sp = data_type.split(".")
    return sp[-1]


def get_module_name(data_type: str, module_structure: ModuleStructure) -> str:
    if data_type is None:
        return None

    module_names = data_type.split(".")[:-1]

    def search(
            mod_names, structure: ModuleStructure, dtype: str,
            is_first_level: bool = False):
        if len(mod_names) == 0:
            return dtype
        for s in structure.children():
            if s.name != mod_names[0]:
                continue
            if is_first_level:
                return search(mod_names[1:], s, s.name)
            return search(mod_names[1:], s, dtype + "." + s.name)
        return ""

    relative_type = search(module_names, module_structure, "", True)

    return relative_type if relative_type != "" else None
