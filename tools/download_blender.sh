#!/bin/bash
# require: bash version >= 4
# usage example: bash download_blender.sh 2.79 out

SUPPORTED_VERSIONS=(
    "2.78" "2.78a" "2.78b" "2.78c"
    "2.79" "2.79a" "2.79b" "2.79c"
    "2.80"
    "all"
)

declare -A BLENDER_DOWNLOAD_URL=(
    ["v278"]="https://download.blender.org/release/Blender2.78/blender-2.78-OSX_10.6-x86_64.zip"
    ["v278a"]="https://download.blender.org/release/Blender2.78/blender-2.78a-OSX_10.6-x86_64.zip"
    ["v278b"]="https://download.blender.org/release/Blender2.78/blender-2.78b-OSX_10.6-x86_64-fixed.zip"
    ["v278c"]="https://download.blender.org/release/Blender2.78/blender-2.78c-OSX_10.6-x86_64.zip"
    ["v279"]="https://download.blender.org/release/Blender2.79/blender-2.79-macOS-10.6.tar.gz"
    ["v279a"]="https://download.blender.org/release/Blender2.79/blender-2.79a-macOS-10.6.zip"
    ["v279b"]="https://download.blender.org/release/Blender2.79/blender-2.79b-macOS-10.6.zip"
    ["v280"]="https://builder.blender.org/download/blender-2.80-7c438e5366b2-OSX-10.9-x86_64.zip"
)

declare -A NEED_MOVE=(
    ["v278c"]="blender-2.78c-OSX_10.6-x86_64"
    ["v279"]="blender-2.79-macOS-10.6"
    ["v279a"]="blender-2.79a-macOS-10.6"
    ["v279b"]="blender-2.79b-macOS-10.6"
)

# check arguments
if [ $# -ne 2 ]; then
    echo "Usage: sh download_blender.sh <version> <output-dir>"
    exit 1
fi

version=${1}
current_dir=`pwd`
output_dir=${2}

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

function download_blender() {
    ver=${1}

    # download Blender binary
    cd ${current_dir}
    target=blender-${ver}-bin
    mkdir -p ${output_dir}/${target}
    cd ${output_dir}/${target}

    url=${BLENDER_DOWNLOAD_URL[${ver}]}
    filename=${target}
    if [ ${url##*.} = "zip" ]; then
        filename=${filename}.zip
        curl ${url} -o ${filename}
        unzip ${filename}
    elif [ ${url##*.} = "gz" ]; then
        filename=${filename}.gz
        curl ${url} -o ${filename}
        tar xvfz ${filename}
    fi

    if [[ "${NEED_MOVE[${ver}]+_}" == "_" ]]; then
        mv ${NEED_MOVE[$ver]}/* .
    fi
}

function wait_for_all() {
    local status=0
    for pid in $@; do
        wait ${pid} &&:
        (exit $?) && (exit ${status}) &&:; status=$?
    done
    [ ${status} -ne 0 ] && exit ${status}
}

if [ ${version} = "all" ]; then
    pids=()
    for KEY in ${!BLENDER_DOWNLOAD_URL[@]}; do
        download_blender ${KEY} &
        pids+=($!)
    done
    wait_for_all ${pids[@]}
else
    download_blender v${version%.*}${version##*.}
fi

cd ${current_dir}
