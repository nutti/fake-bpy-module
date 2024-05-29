#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: run.sh <target>"
    exit 1
fi

readonly PYTHON_SCRIPT_DIRECTORY=${1}
readonly RUFF_CMD="ruff"

# ruff
error=0
for file in $(find "${PYTHON_SCRIPT_DIRECTORY}" -name "*.py" | sort); do
    echo "======= ruff ${file} ======="

    if ! ${RUFF_CMD} check --fix "${file}"; then
        ((error+=1))
    fi
done

if ((error > 0)); then
    echo "Error: ${error} files have errors."
    exit 1
fi

exit 0
