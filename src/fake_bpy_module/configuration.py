
class Configuration:
    target: str = ""
    target_version: str = ""


# TODO: Use singleton pattern.
_config: Configuration = Configuration()    # pylint: disable=C0103,W0602


def set_target(target: str):
    global _config  # pylint: disable=C0103,W0602

    _config.target = target


def set_target_version(version: str):
    global _config  # pylint: disable=C0103,W0602

    _config.target_version = version


def get_target() -> str:
    return _config.target


def get_target_version() -> str:
    return _config.target_version
