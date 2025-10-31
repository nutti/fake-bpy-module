#!/usr/bin/env bash
set -eEu -o pipefail

# Define directory variables
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
WORKSPACE_DIR=$( realpath "${SCRIPT_DIR}/../.." )
REPO_ROOT=$WORKSPACE_DIR

VERSIONS_YAML="$REPO_ROOT/src/versions.yml"

# Source the YAML loader
source "$REPO_ROOT/tools/utils/yaml_loader.sh"

load_sequence_from_yaml "SUPPORTED_UPBGE_VERSIONS"
readonly SUPPORTED_UPBGE_VERSIONS

declare -A UPBGE_TAG_NAME
load_mapping_from_yaml "UPBGE_TAG_NAME"

BUILD_DIR="build"
UPBGE_BIN_DIR="${BUILD_DIR}/upbge-bin"
UPBGE_SRC_DIR="${BUILD_DIR}/upbge-src"

# Check arguments
if [[ $# != 1 ]]; then
    echo "Usage: bash ${BASH_SOURCE[0]} <target_version>"
    echo "  Available <target_version>: " "${SUPPORTED_UPBGE_VERSIONS[@]}"
    exit 1
fi

target_version="${1}"

# Check target version is supported
if [[ ! " ${SUPPORTED_UPBGE_VERSIONS[*]} " == *" ${target_version} "* ]]; then
    echo "Error: Unsupported UPBGE version: ${target_version}"
    exit 2
fi

# Create BUILD_DIR if not exist
[[ ! -d "${WORKSPACE_DIR}/${BUILD_DIR}" ]] && mkdir -p "${WORKSPACE_DIR}/${BUILD_DIR}"

# Download UPBGE source code
if [[ ! -d "${WORKSPACE_DIR}/${UPBGE_SRC_DIR}" ]]; then
    git clone https://github.com/upbge/upbge.git "${WORKSPACE_DIR}/${UPBGE_SRC_DIR}"
fi

# Define docker run parameters
docker_run_parameters=(
    "-it" "--rm"
    "--user" "$(id -u):$(id -g)"
    "--mount" "type=bind,source=${WORKSPACE_DIR},target=/workspace"
    "--workdir" "/workspace"
    "$(cd "${WORKSPACE_DIR}" && docker build -q -f tools/gen_module/Dockerfile .)"
)

# Download UPBGE binary if not exist
UPBGE_TARGET_BIN_DIR="${UPBGE_BIN_DIR}/upbge-${target_version}-bin"
if [[ ! -d "${WORKSPACE_DIR}/${UPBGE_TARGET_BIN_DIR}" ]]; then
    # Run download_upbge.sh in docker to download the Linux version
    docker run "${docker_run_parameters[@]}" \
        /bin/bash "tools/utils/download_upbge.sh" "${target_version}" "${UPBGE_BIN_DIR}"
fi

# Define gen_module.sh parameters
gen_module_parameters=(
    "${UPBGE_SRC_DIR}"
    "${UPBGE_TARGET_BIN_DIR}"
    "upbge"
    "${UPBGE_TAG_NAME[${target_version}]}"
    "${target_version}"
    "${BUILD_DIR}/results"
)

# Run gen_module.sh in docker
docker run --env TEMPORARY_DIR="${BUILD_DIR}" "${docker_run_parameters[@]}" \
    /bin/bash src/gen_module.sh "${gen_module_parameters[@]}"
