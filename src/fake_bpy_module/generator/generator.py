import pathlib
from typing import List

from docutils import nodes

from ..analyzer.nodes import (
    TargetFileNode,
)
from ..utils import get_first_child
from .. import config

from .writers import (
    BaseWriter,
    PyCodeWriter,
    PyInterfaceWriter,
    JsonWriter,
)


def generate(documents: List[nodes.document]):
    # Create module directories.
    for doc in documents:
        target_filename = get_first_child(doc, TargetFileNode).astext()
        dir_path = (
            config.get_output_dir()
            + "/"
            + target_filename[: target_filename.rfind("/")]
        )
        pathlib.Path(dir_path).mkdir(parents=True, exist_ok=True)

        # Create py.typed file at the root of modules.
        if target_filename.count("/") == 1:
            filename = f"{dir_path}/py.typed"
            with open(filename, "w", encoding="utf-8", newline="\n") as file:
                file.write("")

    # Generate modules.
    generator: BaseWriter = None
    if config.get_output_format() == "py":
        generator = PyCodeWriter()
    elif config.get_output_format() == "pyi":
        generator = PyInterfaceWriter()
    elif config.get_output_format() == "json":
        generator = JsonWriter()

    for doc in documents:
        target_filename = get_first_child(doc, TargetFileNode).astext()
        generator.write(
            f"{config.get_output_dir()}/{target_filename}",
            doc,
            config.get_style_format(),
        )
