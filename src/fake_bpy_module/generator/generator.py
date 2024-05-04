import pathlib
from typing import List

from docutils import nodes

from ..analyzer.nodes import (
    TargetFileNode,
)
from ..utils import get_first_child
from ..config import PackageGenerationConfig

from .writers import (
    BaseWriter,
    PyCodeWriter,
    PyInterfaceWriter,
    JsonWriter,
)


def generate(documents: List[nodes.document], gen_config: PackageGenerationConfig):
    # Create module directories.
    for doc in documents:
        target_filename = get_first_child(doc, TargetFileNode).astext()
        dir_path = gen_config.output_dir + "/" + target_filename[:target_filename.rfind("/")]
        pathlib.Path(dir_path).mkdir(parents=True, exist_ok=True)

        # Create py.typed file.
        filename = f"{dir_path}/py.typed"
        with open(filename, "w", encoding="utf-8", newline="\n") as file:
            file.write("")

    # Generate modules.
    generator: BaseWriter = None
    if gen_config.output_format == "py":
        generator = PyCodeWriter()
    elif gen_config.output_format == "pyi":
        generator = PyInterfaceWriter()
    elif gen_config.output_format == "json":
        generator = JsonWriter()

    for doc in documents:
        target_filename = get_first_child(doc, TargetFileNode).astext()
        generator.write(f"{gen_config.output_dir}/{target_filename}", doc, gen_config.style_format)
