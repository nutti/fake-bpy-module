#!/usr/bin/env bash
# require: bash version >= 4
# usage example: bash download_blender.sh 2.79 out
set -eEu

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
VERSIONS_YAML="$REPO_ROOT/src/versions.yml"

# Source the YAML loader
source "$REPO_ROOT/tools/utils/yaml_loader.sh"

load_sequence_from_yaml "SUPPORTED_BLENDER_VERSIONS_BASE"
SUPPORTED_VERSIONS=("${SUPPORTED_BLENDER_VERSIONS_BASE[@]}")
SUPPORTED_VERSIONS+=("all")
readonly SUPPORTED_VERSIONS

declare -A BLENDER_DOWNLOAD_URL_MACOSX
load_mapping_from_yaml "BLENDER_DOWNLOAD_URL_MACOSX"

declare -A BLENDER_DOWNLOAD_URL_WIN64
load_mapping_from_yaml "BLENDER_DOWNLOAD_URL_WIN64"

declare -A BLENDER_DOWNLOAD_URL_LINUX
load_mapping_from_yaml "BLENDER_DOWNLOAD_URL_LINUX"

declare -A BLENDER_NEED_MOVE_MACOSX
load_mapping_from_yaml "BLENDER_NEED_MOVE_MACOSX"

declare -A BLENDER_NEED_MOVE_WIN64
load_mapping_from_yaml "BLENDER_NEED_MOVE_WIN64"

declare -A BLENDER_NEED_MOVE_LINUX
load_mapping_from_yaml "BLENDER_NEED_MOVE_LINUX"

declare -A BLENDER_CHECKSUM_URL
load_mapping_from_yaml "BLENDER_CHECKSUM_URL"

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

    if [ ! "${move_from}" = "" ]; then
        echo "Moving downloaded Blender ${ver} files from \"${move_from}\" to \"${targetpath}\"."
        mv "${move_from}"/* .
    fi

    # go back to download folder
    popd 1> /dev/null
}

function wait_for_all() {
    local status=0
    for pid in "$@"; do
        wait "${pid}" &&:
        (exit $?) && (exit ${status}) &&:; status=$?
    done
    if [ ${status} -ne 0 ]; then
        exit ${status}
    fi
}

function check_os() {
    # shellcheck disable=SC2003,SC2308,SC2046
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
os=$(check_os)
echo "Operating System is ${os}"

# check if the specified version is supported
supported=0
for v in "${SUPPORTED_VERSIONS[@]}"; do
    if [ "${v}" = "${version}" ]; then
        supported=1
    fi
done
if [ ${supported} -eq 0 ]; then
    echo "${version} is not supported."
    echo "Supported version is ${SUPPORTED_VERSIONS[*]}."
    exit 1
fi

if [ "${version}" = "all" ]; then
    pids=()
    if [ "${os}" == "Mac" ]; then
        for KEY in "${!BLENDER_DOWNLOAD_URL_MACOSX[@]}"; do
            url=${BLENDER_DOWNLOAD_URL_MACOSX[${KEY}]}
            move_from=""
            if [[ "${BLENDER_NEED_MOVE_MACOSX[${KEY}]+_}" == "_" ]]; then
                move_from=${BLENDER_NEED_MOVE_MACOSX[${KEY}]}
            fi
            download_blender "${KEY}" "${url}" "${move_from}" &
            pids+=($!)
        done
    elif [ "${os}" == "Cygwin64" ]; then
        for KEY in "${!BLENDER_DOWNLOAD_URL_WIN64[@]}"; do
            url=${BLENDER_DOWNLOAD_URL_WIN64[${KEY}]}
            move_from=""
            if [[ "${BLENDER_NEED_MOVE_WIN64[${KEY}]+_}" == "_" ]]; then
                move_from=${BLENDER_NEED_MOVE_WIN64[${KEY}]}
            fi
            download_blender "${KEY}" "${url}" "${move_from}" &
            pids+=($!)
        done
    elif [ "${os}" == "Linux" ]; then
        for KEY in "${!BLENDER_DOWNLOAD_URL_LINUX[@]}"; do
            url=${BLENDER_DOWNLOAD_URL_LINUX[${KEY}]}
            move_from=""
            if [[ "${BLENDER_NEED_MOVE_LINUX[${KEY}]+_}" == "_" ]]; then
                move_from=${BLENDER_NEED_MOVE_LINUX[${KEY}]}
            fi
            download_blender "${KEY}" "${url}" "${move_from}" &
            pids+=($!)
        done
    else
        echo "Not supported operating system (OS=${os})"
        exit 1
    fi
    wait_for_all "${pids[@]}"
else
    if [ "${os}" == "Mac" ]; then
        url=${BLENDER_DOWNLOAD_URL_MACOSX[${version}]}
        move_from=""
        if [[ "${BLENDER_NEED_MOVE_MACOSX[${version}]+_}" == "_" ]]; then
            move_from=${BLENDER_NEED_MOVE_MACOSX[${version}]}
        fi
        download_blender "${version}" "${url}" "${move_from}"
    elif [ "${os}" == "Cygwin64" ]; then
        url=${BLENDER_DOWNLOAD_URL_WIN64[${version}]}
        move_from=""
        if [[ "${BLENDER_NEED_MOVE_WIN64[${version}]+_}" == "_" ]]; then
            move_from=${BLENDER_NEED_MOVE_WIN64[${version}]}
        fi
        download_blender "${version}" "${url}" "${move_from}"
    elif [ "${os}" == "Linux" ]; then
        url=${BLENDER_DOWNLOAD_URL_LINUX[${version}]}
        move_from=""
        if [[ "${BLENDER_NEED_MOVE_LINUX[${version}]+_}" == "_" ]]; then
            move_from=${BLENDER_NEED_MOVE_LINUX[${version}]}
        fi
        download_blender "${version}" "${url}" "${move_from}"
    else
        echo "Not supported operating system (OS=${os})"
        exit 1
    fi
fi
