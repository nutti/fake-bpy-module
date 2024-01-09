#!/usr/bin/env bash
set -eEu -o pipefail

# Define directory variables
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
WORKSPACE_DIR=$( realpath "${SCRIPT_DIR}/../.." )

BUILD_DIR="build"
BLENDER_BIN_DIR="${BUILD_DIR}/blender-bin"
BLENDER_SRC_DIR="${BUILD_DIR}/blender-src"

# Define dependency script paths
BUILD_PIP_PACKAGE_SCRIPT_PATH="${WORKSPACE_DIR}/tools/pip_package/build_pip_package.sh"

# Define supported versions and tag names
SUPPORTED_BLENDER_VERSIONS=()
declare -A BLENDER_TAG_NAME=()

## Import variables from build_pip_package.sh
## shellcheck disable=SC1090
eval "$(sed -n '/^SUPPORTED_BLENDER_VERSIONS/,/^TMP_DIR_NAME/{/^TMP_DIR_NAME/!p}' "${BUILD_PIP_PACKAGE_SCRIPT_PATH}")"

# Check arguments
if [[ $# != 1 ]]; then
    echo "Usage: bash ${BASH_SOURCE[0]} <target_version>"
	echo "  Available <target_version>: " "${SUPPORTED_BLENDER_VERSIONS[@]}"
    exit 1
fi

target_version="${1}"

# Check target version is supported
if [[ ! " ${SUPPORTED_BLENDER_VERSIONS[*]} " == *" ${target_version} "* ]]; then
	echo "Error: Unsupported Blender version: ${target_version}"
	exit 2
fi

# Create BUILD_DIR if not exist
[[ ! -d "${WORKSPACE_DIR}/${BUILD_DIR}" ]] && mkdir -p "${WORKSPACE_DIR}/${BUILD_DIR}"

# Download Blender source code
if [[ ! -d "${WORKSPACE_DIR}/${BLENDER_SRC_DIR}" ]]; then
	git clone https://github.com/blender/blender.git "${WORKSPACE_DIR}/${BLENDER_SRC_DIR}"
# else
	# (cd "${WORKSPACE_DIR}/${BLENDER_SRC_DIR}" && git fetch --all)
fi

# Checkout Blender source code to target_version
# Comment next line because gen_module.sh checkout target_version.
# (cd "${WORKSPACE_DIR}/${BLENDER_SRC_DIR}" && git checkout "${BLENDER_TAG_NAME["v${target_version}"]}")

# Define docker run parameters
docker_run_parameters=(
	"-it" "--rm"
	"--user" "$(id -u):$(id -g)"
	"--mount" "type=bind,source=${WORKSPACE_DIR},target=/workspace"
	"--workdir" "/workspace"
	"$(cd "${WORKSPACE_DIR}" && docker build -q -f tools/gen_module/Dockerfile .)"
)

# Download Blender binary if not exist
BLENDER_TARGET_BIN_DIR="${BLENDER_BIN_DIR}/blender-v${target_version}-bin"
if [[ ! -d "${WORKSPACE_DIR}/${BLENDER_TARGET_BIN_DIR}" ]]; then
	# Run download_blender.sh in docker to download the Linux version
	docker run "${docker_run_parameters[@]}" \
		/bin/bash "tools/utils/download_blender.sh" "${target_version}" "${BLENDER_BIN_DIR}"
fi

# Define gen_module.sh parameters
gen_module_parameters=(
	"${BLENDER_SRC_DIR}"
	"${BLENDER_TARGET_BIN_DIR}"
	"blender"
	"${BLENDER_TAG_NAME[v${target_version}]}"
	"${target_version}"
	"${BUILD_DIR}/results"
)

# Run gen_module.sh in docker
docker run --env TEMPORARY_DIR="${BUILD_DIR}" "${docker_run_parameters[@]}" \
	/bin/bash src/gen_module.sh "${gen_module_parameters[@]}"
