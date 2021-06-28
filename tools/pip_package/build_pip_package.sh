#!/usr/bin/env bash
# require: bash version >= 4
# usage example: bash batch_gen_modules.sh 2.79 out
set -eEu

SUPPORTED_VERSIONS=(
    "2.78" "2.79" "2.80" "2.81" "2.82" "2.83"
    "2.90" "2.91" "2.92" "2.93"
)

declare -A BLENDER_TAG_NAME=(
    ["v2.78"]="v2.78c"
    ["v2.79"]="v2.79b"
    ["v2.80"]="v2.80"
    ["v2.81"]="v2.81a"
    ["v2.82"]="v2.82a"
    ["v2.83"]="v2.83.9"
    ["v2.90"]="v2.90.0"
    ["v2.91"]="v2.91.0"
    ["v2.92"]="v2.92.0"
    ["v2.93"]="v2.93.0"
)

TMP_DIR_NAME="tmp"
RAW_MODULES_DIR="raw_modules"
RELEASE_DIR="release"
SCRIPT_DIR=$(cd $(dirname $0); pwd)
CURRENT_DIR=`pwd`
PYTHON_BIN=${PYTHON_BIN:-python}

# check arguments
if [ $# -ne 4 ]; then
    echo "Usage: bash build_pip_package.sh <develop|release> <blender-version> <source-dir> <blender-dir>"
    exit 1
fi

target=${1}
version=${2}
source_dir=${3}
blender_dir=${4}

# check if PYTHON_BIN binary is availble
if ! command -v ${PYTHON_BIN} > /dev/null; then
    echo "Error: Cannot find ${PYTHON_BIN} binary."
    exit 1
fi
python_bin=$(command -v ${PYTHON_BIN})

# check if python version meets our requirements
IFS=" " read -r -a python_version <<< "$(${python_bin} -c 'import sys; print(sys.version_info[:])' | tr -d '(),')"
if [ ${python_version[0]} -lt 3 ] || [[ "${python_version[0]}" -eq 3 && "${python_version[1]}" -lt 7 ]]; then
    echo "Error: Unsupported python version \"${python_version[0]}.${python_version[1]}\". Requiring python 3.7 or higher."
    exit 1
fi

if [ ${RELEASE_VERSION:-not_exist} = "not_exist" ]; then
    echo "Environment variable 'RELEASE_VERSION' does not exist, so use date as release version"
    release_version=`date '+%Y%m%d'`
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

# check if the target is develop or release
if [ ! ${target} = "release" ] && [ ! ${target} = "develop" ]; then
    echo "target must be release or develop"
    exit 1
fi


# check if the specified version is supported
supported=0
for v in "${SUPPORTED_VERSIONS[@]}"; do
    if [ ${v} = ${version} ]; then
        supported=1
    fi
done
if [ ${supported} -eq 0 ]; then
    echo "${version} is not supported."
    echo "Supported version is ${SUPPORTED_VERSIONS[@]}."
    exit 1
fi


# check if release dir and tmp dir are not exist
tmp_dir=${SCRIPT_DIR}/${TMP_DIR_NAME}-${version}
raw_modules_dir=${CURRENT_DIR}/${RAW_MODULES_DIR}
release_dir=${CURRENT_DIR}/${RELEASE_DIR}
if [ -e ${tmp_dir} ]; then
    echo "${tmp_dir} is already exists."
    exit 1
fi


if [ ${target} = "release" ]; then
    # setup pre-generated-modules/release/temp directories
    mkdir -p ${raw_modules_dir}
    mkdir -p ${release_dir}
    mkdir -p ${tmp_dir} && cd ${tmp_dir}

    # generate fake bpy module
    fake_module_dir="out"
    ver=v${version}
    bash ${SCRIPT_DIR}/../../src/gen_module.sh ${CURRENT_DIR}/${source_dir} ${CURRENT_DIR}/${blender_dir} ${BLENDER_TAG_NAME[${ver}]} ${fake_module_dir} ${version}
    zip_dir="fake_bpy_modules_${version}-${release_version}"
    cp -r ${fake_module_dir} ${zip_dir}
    zip_file_name="fake_bpy_modules_${version}-${release_version}.zip"
    zip -r ${zip_file_name} ${zip_dir}
    mv ${zip_file_name} ${raw_modules_dir}
    mv ${fake_module_dir}/* .
    rm -r ${zip_dir}
    rm -r ${fake_module_dir}

    # build pip package
    cp ${SCRIPT_DIR}/setup.py .
    cp ${SCRIPT_DIR}/../../README.md .
    pandoc -f markdown -t rst -o README.rst README.md
    rm README.md
    rm -rf fake_bpy_module*.egg-info/ dist/ build/
    ls -R .
    ${python_bin} setup.py sdist
    ${python_bin} setup.py bdist_wheel

    # move the generated package to releaes directory
    mv dist ${release_dir}/${version}

    # clean up
    cd ${CURRENT_DIR}
    rm -rf ${tmp_dir}

elif [ ${target} = "develop" ]; then
    # setup pre-generated-modules/release/temp directories
    mkdir -p ${raw_modules_dir}
    mkdir -p ${release_dir} && cd ${release_dir}
    cp ${SCRIPT_DIR}/setup.py .

    # generate fake bpy module
    fake_module_dir="out"
    ver=v${version}
    bash ${SCRIPT_DIR}/../../src/gen_module.sh ${CURRENT_DIR}/${source_dir} ${CURRENT_DIR}/${blender_dir} ${BLENDER_TAG_NAME[${ver}]} ${fake_module_dir}
    zip_dir="fake_bpy_modules_${version}-${release_version}"
    cp -r ${fake_module_dir} ${zip_dir}
    zip_file_name="fake_bpy_modules_${version}-${release_version}.zip"
    zip -r ${zip_file_name} ${fake_module_dir}
    mv ${zip_file_name} ${raw_modules_dir}
    mv ${fake_module_dir}/* .
    rm -r ${zip_dir}
    rm -r ${fake_module_dir}

    # build and install package
    ls -R .
    ${python_bin} setup.py develop

    # clean up
    cd ${CURRENT_DIR}
    rm -rf ${tmp_dir}
fi

exit 0
