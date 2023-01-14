#!/usr/bin/env bash
# require: bash version >= 4
# usage example: bash collect_failure_state.sh failure_state
set -eEu

# check arguments
if [ $# -ne 1 ]; then
    echo "Usage: sh download_upbge.sh <output-dir>"
    exit 1
fi

# shellcheck disable=SC2046,SC2155,SC2164
{
SCRIPT_DIR=$(cd $(dirname "$0"); pwd)
}

OUTPUT_DIR=${1}

mkdir -p "${OUTPUT_DIR}"

INTERMIDIATE_DIR="${SCRIPT_DIR}/../.."
if [ -d "${INTERMIDIATE_DIR}" ]; then
    cp -r "${INTERMIDIATE_DIR}" "${OUTPUT_DIR}"
fi