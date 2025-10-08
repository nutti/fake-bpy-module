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

if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Print variable values.")
    parser.add_argument("var_name", help="Name of the variable to print")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    var = globals()[args.var_name]

    if args.json:
        print(json.dumps(var))
    else:
        # Make it easy for .sh to read.
        print(" ".join(var))
