#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: run_tests.sh <packages_path>"
    exit 1
fi

PACKAGES_PATH=${1}
SCRIPT_DIR=$(cd $(dirname $0); pwd)
TMP_DIR_NAME="tmp"

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
    python3 ${SCRIPT_DIR}/python/run_tests.py -p ${pkg_dir_path} -v ${blender_version}
    if [ $? -ne 0 ]; then
        echo "Test Failure. (${pkg})"
        exit 1
    fi
    rm -rf ${tmp_dir_path}
done

exit 0
