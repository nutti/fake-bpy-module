#!/usr/bin/env bash
set -eEu

declare -A PACKAGE_NAME=(
    ["blender"]="bpy"
    ["upbge"]="bge"
)

# Check if a Blender version argument is provided
if [ $# -ne 2 ]; then
    echo "No Blender version provided. Usage: $0 <target> <blender_version>"
    exit 1
fi

target=$1
BLENDER_VERSION=$2
ZIP_FILE="fake_${PACKAGE_NAME[$target]}_modules_${BLENDER_VERSION}-*.zip"
EXTRACT_DIR="extracted_modules"

# Find and unzip the correct file
ZIP_PATH=$(find . -name "${ZIP_FILE}" -print -quit)
if [ -z "${ZIP_PATH}" ]; then
    echo "No matching zip file found for Blender version ${BLENDER_VERSION}"
    exit 1
fi

mkdir -p "${EXTRACT_DIR}"
unzip -q "${ZIP_PATH}" -d "{$EXTRACT_DIR}"

# Run Ruff flake8-pyi checks
ruff check "${EXTRACT_DIR}" --select=PYI --ignore=PYI011,PYI014,PYI018,PYI021,PYI054

# Clean up
rm -rf "${EXTRACT_DIR}"