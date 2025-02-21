from threading import Lock
from typing import Self

from .utils import check_os


class Configuration:
    input_dir = "."
    output_dir: str = "./out"
    os: str = check_os()
    style_format: str = "ruff"
    target: str = "blender"
    target_version: str = None
    mod_version: str = None
    output_format: str = "pyi"

    # pylint: disable=W0201
    __inst = None
    __lock = Lock()

    def __init__(self) -> None:
        raise NotImplementedError("Not allowed to call constructor")

    @classmethod
    def __internal_new(cls) -> Self:
        return super().__new__(cls)

    @classmethod
    def get_instance(cls) -> Self:
        if not cls.__inst:
            with cls.__lock:
                if not cls.__inst:
                    cls.__inst = cls.__internal_new()

        return cls.__inst


def set_input_dir(input_dir: str) -> None:
    inst = Configuration.get_instance()
    inst.input_dir = input_dir


def set_output_dir(output_dir: str) -> None:
    inst = Configuration.get_instance()
    inst.output_dir = output_dir


def set_os(os: str) -> None:
    inst = Configuration.get_instance()
    inst.os = os


def set_style_format(style_format: str) -> None:
    inst = Configuration.get_instance()
    inst.style_format = style_format


def set_target(target: str) -> None:
    inst = Configuration.get_instance()
    inst.target = target


def set_target_version(target_version: str) -> None:
    inst = Configuration.get_instance()
    inst.target_version = target_version


def set_mod_version(mod_version: str) -> None:
    inst = Configuration.get_instance()
    inst.mod_version = mod_version


def set_output_format(output_format: str) -> None:
    inst = Configuration.get_instance()
    inst.output_format = output_format


def get_input_dir() -> str:
    inst = Configuration.get_instance()
    return inst.input_dir


def get_output_dir() -> str:
    inst = Configuration.get_instance()
    return inst.output_dir


def get_os() -> str:
    inst = Configuration.get_instance()
    return inst.os


def get_style_format() -> str:
    inst = Configuration.get_instance()
    return inst.style_format


def get_target() -> str:
    inst = Configuration.get_instance()
    return inst.target


def get_target_version() -> str:
    inst = Configuration.get_instance()
    return inst.target_version


def get_mod_version() -> str:
    inst = Configuration.get_instance()
    return inst.mod_version


def get_output_format() -> str:
    inst = Configuration.get_instance()
    return inst.output_format
