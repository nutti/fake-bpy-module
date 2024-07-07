from pathlib import Path

from docutils import nodes

from fake_bpy_module import config
from fake_bpy_module.analyzer.nodes import TargetFileNode
from fake_bpy_module.utils import get_first_child

from .writers import (
    BaseWriter,
    JsonWriter,
    PyCodeWriter,
    PyInterfaceWriter,
)


def generate(documents: list[nodes.document]) -> None:
    # Create module directories.
    for doc in documents:
        target_filename = get_first_child(doc, TargetFileNode).astext()
        dir_path = (f"{config.get_output_dir()}/"
                    f"{target_filename[:target_filename.rfind('/')]}")
        Path(dir_path).mkdir(parents=True, exist_ok=True)

        # Create py.typed file at the root of modules.
        if target_filename.count("/") == 1:
            filename = f"{dir_path}/py.typed"
            with Path(filename).open(
                    "w", encoding="utf-8", newline="\n") as file:
                file.write("")

    # Generate modules.
    generator: BaseWriter
    if config.get_output_format() == "py":
        generator = PyCodeWriter()
    elif config.get_output_format() == "pyi":
        generator = PyInterfaceWriter()
    elif config.get_output_format() == "json":
        generator = JsonWriter()

    for doc in documents:
        target_filename = get_first_child(doc, TargetFileNode).astext()
        generator.write(f"{config.get_output_dir()}/{target_filename}",
                        doc, config.get_style_format())
