from pathlib import Path

import yaml

# Path to versions.yml.
REPO_PATH = Path(__file__).parent.parent
VERSIONS_YAML = REPO_PATH / "src" / "versions.yml"
DATA = yaml.safe_load(VERSIONS_YAML.read_text(encoding="utf-8"))


def main() -> None:
    fail = False

    # Check SUPPORTED_BLENDER_VERSIONS.
    base_blender: list[str] = DATA["SUPPORTED_BLENDER_VERSIONS_BASE"]
    expected_blender = [*base_blender, "latest"]
    actual_blender: list[str] = DATA["SUPPORTED_BLENDER_VERSIONS"]
    if actual_blender != expected_blender:
        print(
            f"SUPPORTED_BLENDER_VERSIONS should be {expected_blender}, "
            f"but got {actual_blender}"
        )
        fail = True

    # Check SUPPORTED_UPBGE_VERSIONS.
    base_upbge: list[str] = DATA["SUPPORTED_UPBGE_VERSIONS_BASE"]
    expected_upbge = [*base_upbge, "latest"]
    actual_upbge: list[str] = DATA["SUPPORTED_UPBGE_VERSIONS"]
    if actual_upbge != expected_upbge:
        print(
            f"SUPPORTED_UPBGE_VERSIONS should be {expected_upbge}, "
            f"but got {actual_upbge}"
        )
        fail = True

    # Check BLENDER_TAG_NAME keys (includes latest).
    blender_tag_name: dict[str, str] = DATA["BLENDER_TAG_NAME"]
    missing = [
        version for version in actual_blender if version not in blender_tag_name
    ]
    if missing:
        print(f"Missing in BLENDER_TAG_NAME: {missing}")
        fail = True

    # Check UPBGE_TAG_NAME keys.
    upbge_tag_name: dict[str, str] = DATA["UPBGE_TAG_NAME"]
    missing_upbge = [
        version for version in actual_upbge if version not in upbge_tag_name
    ]
    if missing_upbge:
        print(f"Missing in UPBGE_TAG_NAME: {missing_upbge}")
        fail = True

    # Check Blender download mappings.
    other_blender_mappings = [
        "BLENDER_CHECKSUM_URL",
        "BLENDER_NEED_MOVE_LINUX",
        "BLENDER_DOWNLOAD_URL_LINUX",
        "BLENDER_DOWNLOAD_URL_WIN64",
    ]
    for mapping in other_blender_mappings:
        tag_dict: dict[str, str] = DATA[mapping]
        missing = [
            version for version in base_blender if version not in tag_dict
        ]
        if missing:
            print(f"Missing in {mapping}: {missing}")
            fail = True

    # Check UPBGE download mappings.
    other_upbge_mappings = [
        "UPBGE_CHECKSUM_URL",
        "UPBGE_NEED_MOVE_LINUX",
        "UPBGE_DOWNLOAD_URL_LINUX",
    ]
    for mapping in other_upbge_mappings:
        tag_dict: dict[str, str] = DATA[mapping]
        missing = [version for version in base_upbge if version not in tag_dict]
        if missing:
            print(f"Missing in {mapping}: {missing}")
            fail = True

    if not fail:
        print("All validations passed! ✅")

    assert not fail, "Some validations failed. See the messages above."


if __name__ == "__main__":
    main()
