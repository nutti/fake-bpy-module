# This file shouldn't have any dependencies
# as it will be executed independently by .sh scripts.


SUPPORTED_TARGET: list[str] = [
    "blender",
    "upbge"
]

SUPPORTED_STYLE_FORMAT: list[str] = [
    "none",
    "yapf",
    "ruff"
]

SUPPORTED_BLENDER_VERSIONS: list[str] = [
    "2.78", "2.79",
    "2.80", "2.81", "2.82", "2.83",
    "2.90", "2.91", "2.92", "2.93",
    "3.0", "3.1", "3.2", "3.3", "3.4", "3.5", "3.6",
    "4.0", "4.1", "4.2", "4.3",
    "latest"
]

SUPPORTED_UPBGE_VERSIONS: list[str] = [
    "0.2.5",
    "0.30", "0.36",
    "latest"
]

SUPPORTED_MOD_BLENDER_VERSIONS = SUPPORTED_BLENDER_VERSIONS
SUPPORTED_MOD_UPBGE_VERSIONS = SUPPORTED_UPBGE_VERSIONS

SUPPORTED_BLENDER_VERSIONS_CI = SUPPORTED_BLENDER_VERSIONS.copy()
SUPPORTED_BLENDER_VERSIONS_CI.remove("latest")
SUPPORTED_UPBGE_VERSIONS_CI = SUPPORTED_UPBGE_VERSIONS.copy()
SUPPORTED_UPBGE_VERSIONS_CI.remove("latest")

SUPPORTED_BLENDER_VERSIONS_DOWNLOAD = SUPPORTED_BLENDER_VERSIONS.copy()
SUPPORTED_BLENDER_VERSIONS_DOWNLOAD.remove("latest")
SUPPORTED_BLENDER_VERSIONS_DOWNLOAD.append("all")
SUPPORTED_UPBGE_VERSIONS_DOWNLOAD = SUPPORTED_UPBGE_VERSIONS.copy()
SUPPORTED_UPBGE_VERSIONS_DOWNLOAD.remove("latest")
SUPPORTED_UPBGE_VERSIONS_DOWNLOAD.append("all")

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
