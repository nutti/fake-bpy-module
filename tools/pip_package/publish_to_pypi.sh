#!/usr/bin/env bash
set -eEu

RELEASE_FILE="all.tar.gz"
RELEASE_DIR="./release"

if [ $# -ne 1 ]; then
    echo "Usage: bash publish_to_pypi.sh <target>"
fi

if [ ! -e ${RELEASE_FILE} ]; then
    echo "Can't find release file ${RELEASE_FILE}."
    exit 1
fi

if [ -e ${RELEASE_DIR} ]; then
    echo "Release dir ${RELEASE_DIR} already exists."
    exit 1
fi

target=$1
if [ "${target}" != "release" ] && [ "${target}" != "test" ]; then
    echo "Target must be 'release' or 'test.'"
    exit 1
fi

tar xvfz ${RELEASE_FILE}

# shellcheck disable=SC2044
for dir in $(find ${RELEASE_DIR} -type d); do
    if [ "${dir}" = ${RELEASE_DIR} ]; then
        continue
    fi
    if [ "${target}" = "release" ]; then
        twine upload --repository pypi "${dir}"/*
    elif [ "${target}" = "test" ]; then
        twine upload --repository testpypi "${dir}"/*
    else
        echo "Internal error: Invalid target."
        exit 1
    fi
done

rm -rf ${RELEASE_DIR}

exit 0
