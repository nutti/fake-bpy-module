#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: run.sh <target>"
    exit 1
fi

readonly PYTHON_SCRIPT_DIRECTORY=${1}
readonly YAMLLINT_CMD="yamllint"

# yamllint
error=0
for file in $(find "${PYTHON_SCRIPT_DIRECTORY}" -name "*.yml" | sort); do
    echo "======= yamllint ${file} ======="

    if ! ${YAMLLINT_CMD} --strict "${file}"; then
        ((error+=1))
    fi
done

if ((error > 0)); then
    echo "Error: ${error} files have errors."
    exit 1
fi

exit 0
