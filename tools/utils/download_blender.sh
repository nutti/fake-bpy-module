#!/usr/bin/env bash
# require: bash version >= 4
# usage example: bash download_blender.sh 2.79 out
set -eEu

SUPPORTED_VERSIONS=(
    "2.78" "2.79" "2.80" "2.81" "2.82" "2.83"
    "all"
)

declare -A BLENDER_DOWNLOAD_URL_MACOSX=(
    ["v278"]="https://download.blender.org/release/Blender2.78/blender-2.78c-OSX_10.6-x86_64.zip"
    ["v279"]="https://download.blender.org/release/Blender2.79/blender-2.79a-macOS-10.6.zip"
    ["v280"]=""
    ["v281"]=""
    ["v282"]=""
    ["v283"]=""
)

declare -A BLENDER_DOWNLOAD_URL_WIN64=(
    ["v278"]="https://download.blender.org/release/Blender2.78/blender-2.78c-windows64.zip"
    ["v279"]="https://download.blender.org/release/Blender2.79/blender-2.79b-windows64.zip"
    ["v280"]="https://download.blender.org/release/Blender2.80/blender-2.80-windows64.zip"
    ["v281"]="https://download.blender.org/release/Blender2.81/blender-2.81a-windows64.zip"
    ["v282"]="https://download.blender.org/release/Blender2.82/blender-2.82a-windows64.zip"
    ["v283"]="https://download.blender.org/release/Blender2.83/blender-2.83.0-windows64.zip"
)

declare -A BLENDER_DOWNLOAD_URL_LINUX=(
    ["v278"]="https://download.blender.org/release/Blender2.78/blender-2.78c-linux-glibc219-x86_64.tar.bz2"
    ["v279"]="https://download.blender.org/release/Blender2.79/blender-2.79b-linux-glibc219-x86_64.tar.bz2"
    ["v280"]="https://download.blender.org/release/Blender2.80/blender-2.80-linux-glibc217-x86_64.tar.bz2"
    ["v281"]="https://download.blender.org/release/Blender2.81/blender-2.81a-linux-glibc217-x86_64.tar.bz2"
    ["v282"]="https://download.blender.org/release/Blender2.82/blender-2.82a-linux64.tar.xz"
    ["v283"]="https://download.blender.org/release/Blender2.83/blender-2.83.0-linux64.tar.xz"
)

declare -A NEED_MOVE_MACOSX=(
    ["v278"]="blender-2.78c-OSX_10.6-x86_64"
    ["v279"]="blender-2.79b-macOS-10.6"
)

declare -A NEED_MOVE_WIN64=(
)

declare -A NEED_MOVE_LINUX=(
    ["v278"]="blender-2.78c-linux-glibc219-x86_64"
    ["v279"]="blender-2.79b-linux-glibc219-x86_64"
    ["v280"]="blender-2.80-linux-glibc217-x86_64"
    ["v281"]="blender-2.81a-linux-glibc217-x86_64"
    ["v282"]="blender-2.82a-linux64"
    ["v283"]="blender-2.83.0-linux64"
)

function download_blender() {
    ver=${1}
    blender_download_url=${2}
    move_from=${3}

    # download Blender binary
    cd ${current_dir}
    target=blender-${ver}-bin
    mkdir -p ${output_dir}/${target}
    cd ${output_dir}/${target}

    url=${blender_download_url}
    filename=${target}
    if [ ${url##*.} = "zip" ]; then
        filename=${filename}.zip
        curl ${url} -o ${filename}
        unzip ${filename}
        rm ${filename}
    elif [ ${url##*.} = "bz2" ]; then
        filename=${filename}.bz2
        curl ${url} -o ${filename}
        tar -jxvf ${filename}
        rm ${filename}
    elif [ ${url##*.} = "xz" ]; then
        filename=${filename}.xz
        curl ${url} -o ${filename}
        tar Jxvf ${filename}
        rm ${filename}
    fi

    if [ ! ${move_from} = "" ]; then
        mv ${move_from}/* .
    fi
}

function wait_for_all() {
    local status=0
    for pid in $@; do
        wait ${pid} &&:
        (exit $?) && (exit ${status}) &&:; status=$?
    done
    if [ ${status} -ne 0 ]; then
        exit ${status}
    fi
}

function check_os() {
    if [ "$(uname)" == "Darwin" ]; then
        echo "Mac"
    elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
        echo "Linux"
    elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]; then
        echo "Cygwin64"
    else
        echo "Unknown"
    fi
}

# check arguments
if [ $# -ne 2 ]; then
    echo "Usage: sh download_blender.sh <version> <output-dir>"
    exit 1
fi

version=${1}
current_dir=`pwd`
output_dir=${2}

# check operating system
os=`check_os`
echo "Operating System is ${os}"

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

if [ ${version} = "all" ]; then
    pids=()
    if [ ${os} == "Mac" ]; then
        for KEY in ${!BLENDER_DOWNLOAD_URL_MACOSX[@]}; do
            url=${BLENDER_DOWNLOAD_URL_MACOSX[${KEY}]}
            move_from=""
            if [[ "${NEED_MOVE_MACOSX[${KEY}]+_}" == "_" ]]; then
                move_from=${NEED_MOVE_MACOSX[${KEY}]}
            fi
            download_blender ${KEY} ${url} ${move_from} &
            pids+=($!)
        done
    elif [ ${os} == "Cygwin64" ]; then
        for KEY in ${!BLENDER_DOWNLOAD_URL_WIN64[@]}; do
            url=${BLENDER_DOWNLOAD_URL_WIN64[${KEY}]}
            move_from=""
            if [[ "${NEED_MOVE_WIN64[${KEY}]+_}" == "_" ]]; then
                move_from=${NEED_MOVE_WIN64[${KEY}]}
            fi
            download_blender ${KEY} ${url} ${move_from} &
            pids+=($!)
        done
    elif [ ${os} == "Linux" ]; then
        for KEY in ${!BLENDER_DOWNLOAD_URL_LINUX[@]}; do
            url=${BLENDER_DOWNLOAD_URL_LINUX[${KEY}]}
            move_from=""
            if [[ "${NEED_MOVE_LINUX[${KEY}]+_}" == "_" ]]; then
                move_from=${NEED_MOVE_LINUX[${KEY}]}
            fi
            download_blender ${KEY} ${url} ${move_from} &
            pids+=($!)
        done
    else
        echo "Not supported operating system (OS=${os})"
        exit 1
    fi
    wait_for_all ${pids[@]}
else
    if [ ${os} == "Mac" ]; then
        ver=v${version%.*}${version##*.}
        url=${BLENDER_DOWNLOAD_URL_MACOSX[${ver}]}
        move_from=""
        if [[ "${NEED_MOVE_MACOSX[${ver}]+_}" == "_" ]]; then
            move_from=${NEED_MOVE_MACOSX[${ver}]}
        fi
        download_blender ${ver} ${url} ${move_from}
    elif [ ${os} == "Cygwin64" ]; then
        ver=v${version%.*}${version##*.}
        url=${BLENDER_DOWNLOAD_URL_WIN64[${ver}]}
        move_from=""
        if [[ "${NEED_MOVE_WIN64[${ver}]+_}" == "_" ]]; then
            move_from=${NEED_MOVE_WIN64[${ver}]}
        fi
        download_blender ${ver} ${url} ${move_from}
    elif [ ${os} == "Linux" ]; then
        ver=v${version%.*}${version##*.}
        url=${BLENDER_DOWNLOAD_URL_LINUX[${ver}]}
        move_from=""
        if [[ "${NEED_MOVE_LINUX[${ver}]+_}" == "_" ]]; then
            move_from=${NEED_MOVE_LINUX[${ver}]}
        fi
        download_blender ${ver} ${url} ${move_from}
    else
        echo "Not supported operating system (OS=${os})"
        exit 1
    fi
fi

cd ${current_dir}
