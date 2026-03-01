from docutils.readers import standalone
from docutils.transforms import references, frontmatter

from fake_bpy_module.transformer.transformer_base import TransformerBase


class BpyRstDocsReader(standalone.Reader):
    def get_transforms(self) -> list[TransformerBase]:
        transforms = super().get_transforms()
        transforms.remove(references.DanglingReferences)
        transforms.remove(frontmatter.DocTitle)

        return transforms
