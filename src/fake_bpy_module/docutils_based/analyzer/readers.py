from docutils.readers import standalone
from docutils.transforms import references


class BpyRstDocsReader(standalone.Reader):
    def get_transforms(self):
        transforms = super().get_transforms()
        transforms.remove(references.DanglingReferences)

        return transforms
