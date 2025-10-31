from pathlib import Path

import yaml

YAML_PATH = Path(__file__).parent.parent / "versions.yml"
YAML_DATA = yaml.safe_load(YAML_PATH.read_text(encoding="utf-8"))

SUPPORTED_TARGET: list[str] = [
    "blender",
    "upbge"
]

SUPPORTED_STYLE_FORMAT: list[str] = [
    "none",
    "yapf",
    "ruff"
]

SUPPORTED_BLENDER_VERSIONS: list[str] = YAML_DATA["SUPPORTED_BLENDER_VERSIONS"]
SUPPORTED_UPBGE_VERSIONS: list[str] = YAML_DATA["SUPPORTED_UPBGE_VERSIONS"]

SUPPORTED_MOD_BLENDER_VERSIONS = SUPPORTED_BLENDER_VERSIONS
SUPPORTED_MOD_UPBGE_VERSIONS = SUPPORTED_UPBGE_VERSIONS
