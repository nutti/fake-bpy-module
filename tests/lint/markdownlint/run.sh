#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: run.sh <target>"
    exit 1
fi

readonly MARKDOWN_DIRECTORY=${1}
# shellcheck disable=SC2155
{
readonly TMP_DIR=$(mktemp -d)
}
readonly MARKDOWN_CMD="markdownlint"

error=0
for file in $(find "${MARKDOWN_DIRECTORY}" -name "*.md" | sort); do
    MARKDOWN_INPUT_FILE="${TMP_DIR}/${file}"
    dir_name=$(dirname "${MARKDOWN_INPUT_FILE}")
    mkdir -p "${dir_name}" 

    SKIP_FILES=()

    skip=0
    for f in "${SKIP_FILES[@]}"; do
        if [[ ${file} =~ ${f} ]]; then
            skip=1
        fi
    done
    if [ ${skip} -eq 1 ]; then
        echo "'${file}' was skipped."
        continue
    fi

    cat "${file}" > "${MARKDOWN_INPUT_FILE}"

    echo "======= markdownlint ${file} ======="

    if ! ${MARKDOWN_CMD} "${MARKDOWN_INPUT_FILE}"; then
        ((error+=1))
    fi

    rm -rf "${TMP_DIR}"
done

if ((error > 0)); then
    echo "Error: ${error} files have errors."
    exit 1
fi

exit ${error}
