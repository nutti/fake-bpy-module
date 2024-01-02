#!/usr/bin/env bash
set -eEu -o pipefail

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
WORKSPACE_DIR=$( realpath "${SCRIPT_DIR}/../.." )
BUILD_DIR="${WORKSPACE_DIR}/build"
GITHUB_ACTIONS_TESTS_DIR="${WORKSPACE_DIR}/tools/github_actions_tests"

if [ $# -lt 1 ]; then
    echo "Usage: bash ${BASH_SOURCE[0]} <act_args>"
    echo "  For example: bash ${BASH_SOURCE[0]} --list"
    echo "  See: https://github.com/nektos/act#example-commands"
    exit 1
fi

if [[ ! -v GITHUB_TOKEN ]]; then
    echo "Error: GITHUB_TOKEN is not set. Please set GITHUB_TOKEN to your GitHub private access token, which must have Public Repositories (read-only) access."
    echo "  For example: GITHUB_TOKEN=github_pat_XXXXXXXXXXXXXXXXXXXXXXXX bash ${BASH_SOURCE[0]}" "$@"
    exit 2
fi

if ! command -v docker > /dev/null 2>&1; then
    echo "Error: Cannot find docker. Please install docker."
    exit 3
fi

[ ! -d "${BUILD_DIR}/act_artifacts" ] && mkdir -p "${BUILD_DIR}/act_artifacts"

docker run --rm \
    --mount type=bind,source=/var/run/docker.sock,target=/var/run/docker.sock \
    --mount type=bind,source="${BUILD_DIR}/act_artifacts",target=/act_artifacts \
    --mount type=volume,source=fake-bpy-module-act-cache,target=/act_cache \
    --mount type=volume,source=fake-bpy-module-act-cache-server,target=/act_cache_server \
    --mount type=bind,source="${WORKSPACE_DIR}",target=/workspace \
    --workdir /workspace \
    "$(docker build -q -f "${GITHUB_ACTIONS_TESTS_DIR}/Dockerfile" .)" \
    /bin/act \
    --secret GITHUB_TOKEN="${GITHUB_TOKEN}" \
    --secret TOKEN_FOR_ACTION_BLENDER_DAILY_BUILD="${GITHUB_TOKEN}" \
    --platform ubuntu-latest=catthehacker/ubuntu:act-latest \
    --platform ubuntu-22.04=catthehacker/ubuntu:act-22.04 \
    --platform ubuntu-20.04=catthehacker/ubuntu:act-20.04 \
    --action-cache-path /act_cache \
    --cache-server-path /act_cache_server \
    --artifact-server-path /act_artifacts \
    "$@"
