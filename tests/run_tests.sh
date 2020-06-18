#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: run_tests.sh <packages_path>"
    exit 1
fi

PACKAGES_PATH=${1}
SCRIPT_DIR=$(cd $(dirname $0); pwd)
TMP_DIR_NAME="tmp"
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

tmp_dir_path="${SCRIPT_DIR}/${TMP_DIR_NAME}"

package_list=`find ${PACKAGES_PATH} -name "*.zip"`
for pkg in ${package_list}; do
    if [[ ${pkg} =~ (fake_bpy_modules_([a-z0-9\.]+)-[0-9]{8}).zip ]]; then
        pkg_dir_name=${BASH_REMATCH[1]}
        blender_version=${BASH_REMATCH[2]}
    else
        echo "'${pkg}' is invalid package."
        continue
    fi

    mkdir ${tmp_dir_path}
    unzip ${pkg} -d ${tmp_dir_path}
    pkg_dir_path=${tmp_dir_path}/${pkg_dir_name}
    ${python_bin} ${SCRIPT_DIR}/python/run_tests.py -p ${pkg_dir_path} -v ${blender_version}
    if [ $? -ne 0 ]; then
        echo "Test Failure. (${pkg})"
        exit 1
    fi
    rm -rf ${tmp_dir_path}
done

exit 0
