import re
from typing import List, Dict
from docutils import nodes
from docutils.core import publish_doctree

from .transformer_base import TransformerBase
from ..analyzer.nodes import (
    ModuleNode,
    NameNode,
    TargetFileNode,
    ChildModuleListNode,
    ChildModuleNode,
)
from ..utils import get_first_child, append_child
from .utils import ModuleStructure, build_module_structure


class GenerationInfoByModule:
    def __init__(self):
        self.target_filename: str = None
        self.documents: List[nodes.document] = []
        self.child_modules: List[str] = []


class GenerationInfo:
    def __init__(self):
        # Key: Module name
        self._info: Dict[str, GenerationInfoByModule] = {}

    def get(self, module_name: str) -> GenerationInfoByModule:
        if module_name not in self._info:
            raise RuntimeError("Could not find module in GenerationInfoByModule "
                               f"(module: {module_name})")
        return self._info[module_name]

    def create(self, module_name: str) -> GenerationInfoByModule:
        self._info[module_name] = GenerationInfoByModule()
        return self._info[module_name]

    def modules(self) -> str:
        return self._info.keys()


class TargetFileCombiner(TransformerBase):

    def __init__(self, documents: List[nodes.document], **kwargs):
        super().__init__(documents, **kwargs)
        self._package_structure: ModuleStructure = None
        if "package_structure" in kwargs:
            self._package_structure = kwargs["package_structure"]

    def _build_generation_info(
            self, documents: List[nodes.document],
            module_structure: ModuleStructure) -> GenerationInfoByModule:
        def find_target_file(
                name: str, structure: ModuleStructure, target: str,
                module_level: int) -> str:
            for m in structure.children():
                mod_name = name + m.name
                if mod_name == target:
                    return mod_name + "/__init__"

                if len(m.children()) > 0:
                    ret = find_target_file(
                        mod_name + "/", m, target, module_level+1)
                    if ret:
                        return ret
            return None

        def build_child_modules(
                gen_info: GenerationInfo, name: str,
                structure: ModuleStructure, module_level: int):
            for m in structure.children():
                mod_name = name + m.name
                if len(m.children()) == 0:
                    filename = \
                        re.sub(r"\.", "/", mod_name) + "/__init__"
                    info = gen_info.create(mod_name)
                    info.documents = []
                    info.child_modules = []
                    info.target_filename = filename
                else:
                    filename = re.sub(r"\.", "/", mod_name) + "/__init__"
                    info = gen_info.create(mod_name)
                    info.documents = []
                    info.child_modules = [child.name for child in m.children()]
                    info.target_filename = filename
                    build_child_modules(
                        gen_info, mod_name + ".", m, module_level+1)

        # build child modules
        gen_info = GenerationInfo()
        build_child_modules(gen_info, "", module_structure, 0)

        # build data
        for document in documents:
            module_node = get_first_child(document, ModuleNode)
            if module_node is None:
                continue
            module_name = module_node.element(NameNode).astext()
            target = find_target_file("", module_structure,
                                      re.sub(r"\.", "/", module_name), 0)
            if target is None:
                raise RuntimeError("Could not find target file to "
                                   f"generate (target: {module_name})")
            info = gen_info.get(module_name)
            info.documents.append(document)

        # Combine document by the same targets.
        results: List[nodes.document] = []
        for mod_name in gen_info.modules():
            info = gen_info.get(mod_name)
            new_doc: nodes.document = publish_doctree("")

            append_child(new_doc, TargetFileNode(text=info.target_filename))

            child_module_list_node = ChildModuleListNode()
            for child_module in info.child_modules:
                child_module_list_node.append_child(ChildModuleNode(text=child_module))
            append_child(new_doc, child_module_list_node)

            found_module_node = False
            for doc in info.documents:
                for child in doc.children[:]:
                    if isinstance(child, ModuleNode):
                        assert mod_name == child.element(NameNode).astext()
                        try:
                            next(new_doc.findall(ModuleNode))
                        except StopIteration:
                            append_child(new_doc, child)
                            found_module_node = True
                    else:
                        append_child(new_doc, child)
            if not found_module_node:
                module_node = ModuleNode()
                module_node.append_child(NameNode(text=mod_name))
                append_child(new_doc, module_node)

            results.append(new_doc)

        return results

    @classmethod
    def name(cls) -> str:
        return "target_file_combiner"

    def apply(self, **kwargs):
        if self._package_structure is None:
            structure = build_module_structure(self.documents)
        else:
            structure = self._package_structure
        new_documents = self._build_generation_info(self.documents, structure)

        self.documents.clear()
        self.documents.extend(new_documents)
