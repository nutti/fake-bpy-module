from threading import Lock


class Configuration:
    target: str = ""
    target_version: str = ""

    # pylint: disable=W0201
    __inst = None
    __lock = Lock()

    def __init__(self):
        raise NotImplementedError("Not allowed to call constructor")

    @classmethod
    def __internal_new(cls):
        inst = super().__new__(cls)

        return inst

    @classmethod
    def get_instance(cls):
        if not cls.__inst:
            with cls.__lock:
                if not cls.__inst:
                    cls.__inst = cls.__internal_new()

        return cls.__inst


def set_target(target: str):
    inst = Configuration.get_instance()

    inst.target = target


def set_target_version(version: str):
    inst = Configuration.get_instance()

    inst.target_version = version


def get_target() -> str:
    inst = Configuration.get_instance()

    return inst.target


def get_target_version() -> str:
    inst = Configuration.get_instance()

    return inst.target_version


class PackageGenerationConfig:
    def __init__(self):
        self.output_dir: str = "./out"
        self.os: str = "Linux"
        self.style_format: str = "ruff"
        self.target: str = "blender"
        self.target_version: str = None
        self.mod_version: str = None
        self.output_format: str = "pyi"
