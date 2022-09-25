#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: run.sh <target>"
    exit 1
fi

# shellcheck disable=SC2046,SC2155,SC2164
{
readonly SCRIPT_DIR=$(cd $(dirname "$0"); pwd)
}
readonly PYTHON_SCRIPT_DIRECTORY=${1}
readonly PYLINT_CMD="pylint"

# pylint
error=0
for file in $(find "${PYTHON_SCRIPT_DIRECTORY}" -name "*.py" | sort); do
    echo "======= pylint ${file} ======="

    if ! ${PYLINT_CMD} --rcfile="${SCRIPT_DIR}/.pylintrc" "${file}"; then
        ((error+=1))
    fi
done

if ((error > 0)); then
    echo "Error: ${error} files have errors."
    exit 1
fi

exit 0
