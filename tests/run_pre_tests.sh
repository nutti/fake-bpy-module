#!/usr/bin/env bash
set -eEu

if [ $# -ne 1 ]; then
    echo "Usage: run_tests.sh <fake_bpy_module_package_path>"
    exit 1
fi

PACKAGES_PATH=${1}
SCRIPT_DIR=$(cd $(dirname $0); pwd)
PYTHON_BIN=${PYTHON_BIN:-python}

# check if PYTHON_BIN binary is availble
if ! command -v ${PYTHON_BIN} > /dev/null; then
    echo "Error: Cannot find ${PYTHON_BIN} binary."
    exit 1
fi
python_bin=$(command -v ${PYTHON_BIN})

# check if python version meets our requirements
IFS=" " read -r -a python_version <<< "$(${python_bin} -c 'import sys; print(sys.version_info[:])' | tr -d '(),')"
if [ ${python_version[0]} -lt 3 ] || [[ "${python_version[0]}" -eq 3 && "${python_version[1]}" -lt 7 ]]; then
    echo "Error: Unsupported python version \"${python_version[0]}.${python_version[1]}\". Requiring python 3.7 or higher."
    exit 1
fi

if ! ${python_bin} "${SCRIPT_DIR}/python/fake_bpy_module_test/run_tests.py" -p "${PACKAGES_PATH}"; then
    echo "Error: fake_bpy_module test failed"
    exit 1
fi

exit 0
