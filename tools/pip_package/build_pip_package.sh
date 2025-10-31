#!/usr/bin/env bash
# require: bash version >= 4
# usage example: bash build_pip_package.sh blender 4.3 "./blender-src" "./blender-v4.3-bin" 4.3
set -eEu

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
VERSIONS_YAML="$REPO_ROOT/src/versions.yml"

# Source the YAML loader
source "$REPO_ROOT/tools/utils/yaml_loader.sh"

load_sequence_from_yaml "SUPPORTED_BLENDER_VERSIONS"
readonly SUPPORTED_BLENDER_VERSIONS

load_sequence_from_yaml "SUPPORTED_UPBGE_VERSIONS"
readonly SUPPORTED_UPBGE_VERSIONS


declare -A BLENDER_TAG_NAME
load_mapping_from_yaml "BLENDER_TAG_NAME"

declare -A UPBGE_TAG_NAME
load_mapping_from_yaml "UPBGE_TAG_NAME"

declare -A PACKAGE_NAME=(
    ["blender"]="bpy"
    ["upbge"]="bge"
)

TMP_DIR_NAME="tmp"
RAW_MODULES_DIR="raw_modules"
RELEASE_DIR="release"
# shellcheck disable=SC2046,SC2155,SC2164
{
SCRIPT_DIR=$(cd $(dirname "$0"); pwd)
}
CURRENT_DIR=$(pwd)
PYTHON_BIN=${PYTHON_BIN:-python}

# check arguments
if [ $# -ne 4 ] && [ $# -ne 5 ]; then
    echo "Usage: bash build_pip_package.sh <target> <target-version> <source-dir> <blender-dir> [<mod-version>]"
    exit 1
fi

target=${1}
target_version=${2}
source_dir=${3}
blender_dir=${4}
mod_version=${5:-not-specified}

# check if PYTHON_BIN binary is availble
if ! command -v "${PYTHON_BIN}" > /dev/null; then
    echo "Error: Cannot find ${PYTHON_BIN} binary."
    exit 1
fi
python_bin=$(command -v "${PYTHON_BIN}")

# check if python version meets our requirements
IFS=" " read -r -a python_version <<< "$(${python_bin} -c 'import sys; print(sys.version_info[:])' | tr -d '(),')"
if [ "${python_version[0]}" -lt 3 ] || [[ "${python_version[0]}" -eq 3 && "${python_version[1]}" -lt 11 ]]; then
    echo "Error: Unsupported python version \"${python_version[0]}.${python_version[1]}\". Requiring python 3.11 or higher."
    exit 1
fi

if [ "${RELEASE_VERSION:-not_exist}" = "not_exist" ]; then
    echo "Environment variable 'RELEASE_VERSION' does not exist, so use date as release version"
    release_version=$(date '+%Y%m%d')
else
    echo "Environment variable 'RELEASE_VERSION' exists, so use it as release version"
    release_version="${RELEASE_VERSION}"
fi

# Verify that the version is compatible with PEP 440: https://www.python.org/dev/peps/pep-0440/
# This is assumed in further steps below, so check abort early in case it does not match
if ! ${python_bin} -c "from setuptools._vendor.packaging.version import Version; Version(\"${release_version}\")"; then
    echo "Error: Found invalid release version: \"${release_version}\""
    exit 1
fi

# check if the specified version is supported
supported=0
if [ "${target}" = "blender" ]; then
    for v in "${SUPPORTED_BLENDER_VERSIONS[@]}"; do
        if [ "${v}" = "${target_version}" ]; then
            supported=1
        fi
    done
    if [ ${supported} -eq 0 ]; then
        echo "${target_version} is not supported."
        echo "Supported version is ${SUPPORTED_BLENDER_VERSIONS[*]}."
        exit 1
    fi
elif [ "${target}" = "upbge" ]; then
    for v in "${SUPPORTED_UPBGE_VERSIONS[@]}"; do
        if [ "${v}" = "${target_version}" ]; then
            supported=1
        fi
    done
    if [ ${supported} -eq 0 ]; then
        echo "${target_version} is not supported."
        echo "Supported version is ${SUPPORTED_UPBGE_VERSIONS[*]}."
        exit 1
    fi
else
    echo "${target} is not supported."
    exit 1
fi

# check if release dir and tmp dir are not exist
tmp_dir="${SCRIPT_DIR}/${TMP_DIR_NAME}-${target_version}"
raw_modules_dir="${CURRENT_DIR}/${RAW_MODULES_DIR}"
release_dir="${CURRENT_DIR}/${RELEASE_DIR}"
if [ -e "${tmp_dir}" ]; then
    echo "${tmp_dir} is already exists."
    exit 1
fi

# setup pre-generated-modules/release/temp directories
mkdir -p "${raw_modules_dir}"
mkdir -p "${release_dir}"
mkdir -p "${tmp_dir}" && cd "${tmp_dir}"

# generate fake module
fake_module_dir="out"
if [ "${target}" = "blender" ]; then
    if [ "${mod_version}" = "not-specified" ]; then
        bash "${SCRIPT_DIR}/../../src/gen_module.sh" "${CURRENT_DIR}/${source_dir}" "${CURRENT_DIR}/${blender_dir}" "${target}" "${BLENDER_TAG_NAME[${target_version}]}" "${target_version}" "${fake_module_dir}"
    else
        bash "${SCRIPT_DIR}/../../src/gen_module.sh" "${CURRENT_DIR}/${source_dir}" "${CURRENT_DIR}/${blender_dir}" "${target}" "${BLENDER_TAG_NAME[${target_version}]}" "${target_version}" "${fake_module_dir}" "${mod_version}"
    fi
elif [ "${target}" = "upbge" ]; then
    if [ "${mod_version}" = "not-specified" ]; then
        bash "${SCRIPT_DIR}/../../src/gen_module.sh" "${CURRENT_DIR}/${source_dir}" "${CURRENT_DIR}/${blender_dir}" "${target}" "${UPBGE_TAG_NAME[${target_version}]}" "${target_version}" "${fake_module_dir}"
    else
        bash "${SCRIPT_DIR}/../../src/gen_module.sh" "${CURRENT_DIR}/${source_dir}" "${CURRENT_DIR}/${blender_dir}" "${target}" "${UPBGE_TAG_NAME[${target_version}]}" "${target_version}" "${fake_module_dir}" "${mod_version}"
    fi
else
    echo "${target} is not supported."
    exit 1
fi

# Install package build tool.
${python_bin} -m pip install build

# Build standalone (.zip) package.
zip_dir="fake_${PACKAGE_NAME[$target]}_modules_${target_version}-${release_version}"
cp -r ${fake_module_dir} "${zip_dir}"
zip_file_name="fake_${PACKAGE_NAME[$target]}_modules_${target_version}-${release_version}.zip"
zip -r "${zip_file_name}" "${zip_dir}"
mv "${zip_file_name}" "${raw_modules_dir}"
rm -r "${zip_dir}"

# Build pip (.whl) package.
mv ${fake_module_dir}/* .
rm -r ${fake_module_dir}
cp "${SCRIPT_DIR}/../../README.md" .
cp "${SCRIPT_DIR}/../../pyproject.toml" .
cp "${SCRIPT_DIR}/../../setup.py" .

# To test against fake-bge-module in fake-bpy-module repository, we need to 
# mimic package name to fake-bge-module.
if [ "${target}" = "upbge" ]; then
    sed -i -e "s/^name = \"fake-bpy-module/name = \"fake-bge-module/g" pyproject.toml
fi

sed -i -e "s/^name = \"fake-${PACKAGE_NAME[$target]}-module\"$/name = \"fake-${PACKAGE_NAME[$target]}-module-${target_version}\"/g" pyproject.toml
rm -rf fake_"${PACKAGE_NAME[$target]}"_module*.egg-info/ dist/ build/
ls -R .
${python_bin} -m build
mv dist "${release_dir}/${target_version}"

# Create non-versioned package for latest release
if [ "${target_version}" = "latest" ]; then
    cp "${SCRIPT_DIR}/../../pyproject.toml" .
    rm -rf fake_"${PACKAGE_NAME[$target]}"_module*.egg-info/ dist/ build/
    ls -R .
    ${python_bin} -m build
    mv dist "${release_dir}/non-version"
fi

# clean up
cd "${CURRENT_DIR}"
rm -rf "${tmp_dir}"
