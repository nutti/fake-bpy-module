#!/bin/bash
# require: bash version >= 4
# usage example: bash batch_gen_modules.sh 2.79 out

SUPPORTED_VERSIONS=(
    "2.78" "2.78a" "2.78b" "2.78c"
    "2.79" "2.79a" "2.79b"
    "2.80"
)

declare -A BLENDER_TAG_NAME=(
    ["v278"]="v2.78"
    ["v278a"]="v2.78a"
    ["v278b"]="v2.78b"
    ["v278c"]="v2.78c"
    ["v279"]="v2.79"
    ["v279a"]="v2.79a"
    ["v279b"]="v2.79b"
    ["v280"]="master"
)

TMP_DIR_NAME="tmp"
RELEASE_DIR="release"
SCRIPT_DIR=$(cd $(dirname $0); pwd)
CURRENT_DIR=`pwd`

# check arguments
if [ $# -ne 4 ]; then
    echo "Usage: sh build_pip_package.sh <develop|release> <blender-version> <source-dir> <blender-dir>"
    exit 1
fi

target=${1}
version=${2}
source_dir=${3}
blender_dir=${4}


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
release_dir=${CURRENT_DIR}/${RELEASE_DIR}
if [ -e ${tmp_dir} ]; then
    echo "${tmp_dir} is already exists."
    exit 1
fi


if [ ${target} = "release" ]; then
    # setup release/temp directories
    mkdir -p ${release_dir}
    mkdir -p ${tmp_dir} && cd ${tmp_dir}
    cp ${SCRIPT_DIR}/setup.py .
    cp ${SCRIPT_DIR}/../../README.md .

    # generate fake bpy module
    fake_module_dir="out"
    ver=v${version%.*}${version##*.}
    sh ${SCRIPT_DIR}/../../src/gen_module.sh ${CURRENT_DIR}/${source_dir} ${CURRENT_DIR}/${blender_dir} ${BLENDER_TAG_NAME[${ver}]} ${fake_module_dir}
    mv ${fake_module_dir}/* .
    rm -r ${fake_module_dir}

    # build pip package
    rm -rf fake_bpy_module*.egg-info/ dist/ build/
    python3 setup.py sdist
    python3 setup.py bdist_wheel

    # move the generated package to releaes directory
    mv dist ${release_dir}/${version}

    # clean up
    cd ${CURRENT_DIR}
    rm -rf ${tmp_dir}

elif [ ${target} = "develop" ]; then
    # setup release/temp directories
    mkdir -p ${release_dir} && cd ${release_dir}
    cp ${SCRIPT_DIR}/setup.py .

    # generate fake bpy module
    fake_module_dir="out"
    ver=v${version%.*}${version##*.}
    sh ${SCRIPT_DIR}/../../src/gen_module.sh ${CURRENT_DIR}/${source_dir} ${CURRENT_DIR}/${blender_dir} ${BLENDER_TAG_NAME[${ver}]} ${fake_module_dir}
    mv ${fake_module_dir}/* .
    rm -r ${fake_module_dir}

    # build and install package
    python3 setup.py develop

    # clean up
    cd ${CURRENT_DIR}
    rm -rf ${tmp_dir}
fi

exit 0
