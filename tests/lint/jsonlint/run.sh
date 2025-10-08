#!/usr/bin/env bash

if [ $# -ne 1 ]; then
    echo "Usage: run.sh <target>"
    exit 1
fi

readonly TARGET_DIRECTORY=${1}
readonly JSONLINT_CMD="jsonlint"

# jsonlint
error=0
for file in $(find "${TARGET_DIRECTORY}" -name "*.json" | sort); do
    echo "======= jsonlint ${file} ======="

    if ! ${JSONLINT_CMD} --quiet "${file}"; then
        ((error+=1))
    fi
done

if ((error > 0)); then
    echo "Error: ${error} files have errors."
    exit 1
fi

exit 0
