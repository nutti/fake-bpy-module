#!/usr/bin/env bash
# require: bash version >= 4
# usage example: bash download_blender.sh 2.79 out
set -eEu

SUPPORTED_VERSIONS=(
    "2.78" "2.79" "2.80" "2.81" "2.82" "2.83"
    "2.90" "2.91" "2.92" "2.93"
    "all"
)

declare -A BLENDER_DOWNLOAD_URL_MACOSX=(
    ["v2.78"]="https://download.blender.org/release/Blender2.78/blender-2.78c-OSX_10.6-x86_64.zip"
    ["v2.79"]="https://download.blender.org/release/Blender2.79/blender-2.79a-macOS-10.6.zip"
    ["v2.80"]=""
    ["v2.81"]=""
    ["v2.82"]=""
    ["v2.83"]="https://download.blender.org/release/Blender2.83/blender-2.83.9-macOS.dmg"
    ["v2.90"]=""
    ["v2.91"]=""
    ["v2.92"]=""
    ["v2.93"]=""
)

declare -A BLENDER_DOWNLOAD_URL_WIN64=(
    ["v2.78"]="https://download.blender.org/release/Blender2.78/blender-2.78c-windows64.zip"
    ["v2.79"]="https://download.blender.org/release/Blender2.79/blender-2.79b-windows64.zip"
    ["v2.80"]="https://download.blender.org/release/Blender2.80/blender-2.80-windows64.zip"
    ["v2.81"]="https://download.blender.org/release/Blender2.81/blender-2.81a-windows64.zip"
    ["v2.82"]="https://download.blender.org/release/Blender2.82/blender-2.82a-windows64.zip"
    ["v2.83"]="https://download.blender.org/release/Blender2.83/blender-2.83.9-windows64.zip"
    ["v2.90"]="https://download.blender.org/release/Blender2.90/blender-2.90.0-windows64.zip"
    ["v2.91"]="https://download.blender.org/release/Blender2.91/blender-2.91.0-windows64.zip"
    ["v2.92"]="https://download.blender.org/release/Blender2.92/blender-2.92.0-windows64.zip"
    ["v2.93"]="https://download.blender.org/release/Blender2.93/blender-2.93.0-windows64.zip"
)

declare -A BLENDER_DOWNLOAD_URL_LINUX=(
    ["v2.78"]="https://download.blender.org/release/Blender2.78/blender-2.78c-linux-glibc219-x86_64.tar.bz2"
    ["v2.79"]="https://download.blender.org/release/Blender2.79/blender-2.79b-linux-glibc219-x86_64.tar.bz2"
    ["v2.80"]="https://download.blender.org/release/Blender2.80/blender-2.80-linux-glibc217-x86_64.tar.bz2"
    ["v2.81"]="https://download.blender.org/release/Blender2.81/blender-2.81a-linux-glibc217-x86_64.tar.bz2"
    ["v2.82"]="https://download.blender.org/release/Blender2.82/blender-2.82a-linux64.tar.xz"
    ["v2.83"]="https://download.blender.org/release/Blender2.83/blender-2.83.9-linux64.tar.xz"
    ["v2.90"]="https://download.blender.org/release/Blender2.90/blender-2.90.0-linux64.tar.xz"
    ["v2.91"]="https://download.blender.org/release/Blender2.91/blender-2.91.0-linux64.tar.xz"
    ["v2.92"]="https://download.blender.org/release/Blender2.92/blender-2.92.0-linux64.tar.xz"
    ["v2.93"]="https://download.blender.org/release/Blender2.93/blender-2.93.1-linux-x64.tar.xz"
)

declare -A NEED_MOVE_MACOSX=(
    ["v2.78"]="blender-2.78c-OSX_10.6-x86_64"
    ["v2.79"]="blender-2.79b-macOS-10.6"
)

declare -A NEED_MOVE_WIN64=(
)

declare -A NEED_MOVE_LINUX=(
    ["v2.78"]="blender-2.78c-linux-glibc219-x86_64"
    ["v2.79"]="blender-2.79b-linux-glibc219-x86_64"
    ["v2.80"]="blender-2.80-linux-glibc217-x86_64"
    ["v2.81"]="blender-2.81a-linux-glibc217-x86_64"
    ["v2.82"]="blender-2.82a-linux64"
    ["v2.83"]="blender-2.83.9-linux64"
    ["v2.90"]="blender-2.90.0-linux64"
    ["v2.91"]="blender-2.91.0-linux64"
    ["v2.92"]="blender-2.92.0-linux64"
    ["v2.93"]="blender-2.93.1-linux-x64"
)

declare -A BLENDER_CHECKSUM_URL=(
    ["v2.78"]="https://download.blender.org/release/Blender2.78/release278c.md5"
    ["v2.79"]="https://download.blender.org/release/Blender2.79/release279b.md5"
    ["v2.80"]="https://download.blender.org/release/Blender2.80/release280.md5"
    ["v2.81"]="https://download.blender.org/release/Blender2.81/release281a.md5"
    ["v2.82"]="https://download.blender.org/release/Blender2.82/release282a.md5"
    ["v2.83"]="https://download.blender.org/release/Blender2.83/blender-2.83.9.md5"
    ["v2.90"]="https://download.blender.org/release/Blender2.90/blender-2.90.0.md5"
    ["v2.91"]="https://download.blender.org/release/Blender2.91/blender-2.91.0.md5"
    ["v2.92"]="https://download.blender.org/release/Blender2.92/blender-2.92.0.md5"
    ["v2.93"]="https://download.blender.org/release/Blender2.93/blender-2.93.1.md5"
)

function get_extractor() {
    local file_extension=${1}
    local extractor

    if [ "${file_extension}" = "zip" ]; then
        extractor="unzip"
    elif [[ "${file_extension}" = "bz2" || "${file_extension}" = "xz" ]]; then
        extractor="tar xf"
    fi
    echo "${extractor}"
}

function verify_download_integrity() {
    local version=${1}
    local target_filepath=${2}

    if [ ! -f "${target_filepath}" ]; then
        return 1
    fi

    echo "Found Blender ${version} download. Verifying the integrity."

    local target_filename download_dir checksum_url checksum_filename
    target_filename="$(basename "${target_filepath}")"
    download_dir="$(dirname "${target_filepath}")"
    checksum_url="${BLENDER_CHECKSUM_URL[${version}]}"
    checksum_filename="$(basename "${checksum_url}")"

    pushd "${download_dir}" 1> /dev/null

    curl --location --fail -s "${checksum_url}" -o "${checksum_filename}"

    if ! grep -q "${target_filename}" "${checksum_filename}"; then
        echo "Error: Unable to find \"${target_filename}\" in \"${checksum_filename}\""
        cat "${checksum_filename}"
        return 1
    fi

    local checksum
    checksum="$(grep "${target_filename}" "${checksum_filename}")"

    md5sum --check --status <<< "${checksum}"
    local returncode=$?

    if [ $returncode -ne 0 ]; then
        echo "Checksum verification of Blender ${version} failed:"
        echo "  Expected: ${checksum}"
        echo "  Received: $(md5sum "${target_filename}")"
    else
        echo "Checksum of Blender ${version} verified."
    fi

    # if function had no critical errors, remove checksum file again.
    rm "${checksum_filename}"

    popd 1> /dev/null
    return ${returncode}
}

# download Blender binary
function download_blender() {
    ver=${1}
    blender_download_url=${2}
    move_from=${3}

    local download_dir target
    download_dir="$(pwd)/downloads"
    target=blender-${ver}-bin

    local url file_extension filename filepath
    url=${blender_download_url}
    file_extension=${url##*.}
    filename="$(basename "${url}")"
    filepath="${download_dir}/${filename}"

    local extractor
    extractor=$(get_extractor "${file_extension}")
    if [ -z "${extractor}" ]; then
        echo "Error: Unknown file extension '${file_extension}'"
        exit 1
    fi

    # check if file already has been download and verify its signature
    if ! verify_download_integrity "${ver}" "${filepath}";  then
        # create download folder
        mkdir -p "${download_dir}"

        # fetch file
        echo "Downloading Blender ${ver}: ${blender_download_url}"
        curl --location --fail -s "${url}" -o "${filepath}"

        # verify integrity of the download
        if ! verify_download_integrity "${ver}" "${filepath}"; then
            echo "Error: Blender ${ver} download failed, please retry. If this happens again, please open a bug report."
            echo "  URL: ${url}"
            exit 1
        fi
    else
        echo "Found verified Blender ${ver} download: \"${filepath}\""
    fi

    local targetpath="${output_dir}/${target}"

    # cleanup existing files
    if [ -d "${targetpath}" ]; then
        echo "Removing old target folder \"${targetpath}\"."
        rm -r "${targetpath}"
    fi
    mkdir -p "${targetpath}"

    # change working directory
    pushd "${targetpath}" 1> /dev/null

    # extract file
    echo "Extracting Blender ${ver} using \"${extractor%% *}\"."
    ${extractor} "${filepath}"

    if [ ! ${move_from} = "" ]; then
        echo "Moving downloaded Blender ${ver} files from \"${move_from}\" to \"${targetpath}\"."
        mv ${move_from}/* .
    fi

    # go back to download folder
    popd 1> /dev/null
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
output_dir=${2}

if [ -z "${output_dir}" ]; then
    echo "Error: <output-dir> cannot be empty. Use \".\" if you wannt to use the current folder."
    exit 1
fi

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
        ver=v${version}
        url=${BLENDER_DOWNLOAD_URL_MACOSX[${ver}]}
        move_from=""
        if [[ "${NEED_MOVE_MACOSX[${ver}]+_}" == "_" ]]; then
            move_from=${NEED_MOVE_MACOSX[${ver}]}
        fi
        download_blender ${ver} ${url} ${move_from}
    elif [ ${os} == "Cygwin64" ]; then
        ver=v${version}
        url=${BLENDER_DOWNLOAD_URL_WIN64[${ver}]}
        move_from=""
        if [[ "${NEED_MOVE_WIN64[${ver}]+_}" == "_" ]]; then
            move_from=${NEED_MOVE_WIN64[${ver}]}
        fi
        download_blender ${ver} ${url} ${move_from}
    elif [ ${os} == "Linux" ]; then
        ver=v${version}
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
