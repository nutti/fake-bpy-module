#!/usr/bin/env bash
# require: bash version >= 4
# usage example: bash download_upbge.sh 0.2.5 out
set -eEu

SUPPORTED_VERSIONS=(
    "0.2.5"
    "all"
)

declare -A UPBGE_DOWNLOAD_URL_LINUX=(
    ["v0.2.5"]="https://github.com/UPBGE/upbge/releases/download/v0.2.5/UPBGEv0.2.5b2.79Linux64.tar.xz"
)

declare -A NEED_MOVE_LINUX=(
    ["v0.2.5"]="UPBGEv0.2.5b2.79Linux64"
)

declare -A UPBGE_CHECKSUM_URL=(
    ["v0.2.5"]="https://raw.githubusercontent.com/nutti/fake-bge-module/ci_testing/tools/utils/md5sum/0.2.5.md5"
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

    echo "Found UPBGE ${version} download. Verifying the integrity."

    local target_filename download_dir checksum_url checksum_filename
    target_filename="$(basename "${target_filepath}")"
    download_dir="$(dirname "${target_filepath}")"
    checksum_url="${UPBGE_CHECKSUM_URL[${version}]}"
    checksum_filename="$(basename "${checksum_url}")"

    pushd "${download_dir}" 1> /dev/null

    curl --fail -s "${checksum_url}" -o "${checksum_filename}"

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
        echo "Checksum verification of UPBGE ${version} failed:"
        echo "  Expected: ${checksum}"
        echo "  Received: $(md5sum "${target_filename}")"
    else
        echo "Checksum of UPBGE ${version} verified."
    fi

    # if function had no critical errors, remove checksum file again.
    rm "${checksum_filename}"

    popd 1> /dev/null
    return ${returncode}
}

# download UPBGE binary
function download_upbge() {
    ver=${1}
    upbge_download_url=${2}
    move_from=${3}

    local download_dir target
    download_dir="$(pwd)/downloads"
    target=upbge-${ver}-bin

    local url file_extension filename filepath
    url=${upbge_download_url}
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
        echo "Downloading UPBGE ${ver}: ${upbge_download_url}"
        curl --fail -L -s "${url}" -o "${filepath}"

        # verify integrity of the download
        if ! verify_download_integrity "${ver}" "${filepath}"; then
            echo "Error: UPBGE ${ver} download failed, please retry. If this happens again, please open a bug report."
            echo "  URL: ${url}"
            exit 1
        fi
    else
        echo "Found verified UPBGE ${ver} download: \"${filepath}\""
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
    echo "Extracting UPBGE ${ver} using \"${extractor%% *}\"."
    ${extractor} "${filepath}"

    if [ ! "${move_from}" = "" ]; then
        echo "Moving downloaded UPBGE ${ver} files from \"${move_from}\" to \"${targetpath}\"."
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
    echo "Usage: sh download_upbge.sh <version> <output-dir>"
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
    if [ "${os}" == "Linux" ]; then
        for KEY in "${!UPBGE_DOWNLOAD_URL_LINUX[@]}"; do
            url=${UPBGE_DOWNLOAD_URL_LINUX[${KEY}]}
            move_from=""
            if [[ "${NEED_MOVE_LINUX[${KEY}]+_}" == "_" ]]; then
                move_from=${NEED_MOVE_LINUX[${KEY}]}
            fi
            download_upbge "${KEY}" "${url}" "${move_from}" &
            pids+=($!)
        done
    else
        echo "Not supported operating system (OS=${os})"
        exit 1
    fi
    wait_for_all "${pids[@]}"
else
    if [ "${os}" == "Linux" ]; then
        ver=v${version}
        url=${UPBGE_DOWNLOAD_URL_LINUX[${ver}]}
        move_from=""
        if [[ "${NEED_MOVE_LINUX[${ver}]+_}" == "_" ]]; then
            move_from=${NEED_MOVE_LINUX[${ver}]}
        fi
        download_upbge "${ver}" "${url}" "${move_from}"
    else
        echo "Not supported operating system (OS=${os})"
        exit 1
    fi
fi
