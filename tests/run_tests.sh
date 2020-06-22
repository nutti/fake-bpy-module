#!/usr/bin/env bash
set -eEu

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

function check_pep440_compatible_version() {
    local version="${1}"
    ${python_bin} -c "from setuptools._vendor.packaging.version import Version; Version(\"${version}\")"
    return $?
}

tmp_dir_path="${SCRIPT_DIR}/${TMP_DIR_NAME}"

invalid_package=0
failed_test=0

package_list=`find ${PACKAGES_PATH} -name "*.zip"`
for pkg in ${package_list}; do
    if [[ ${pkg} =~ (fake_bpy_modules_([a-z0-9\.]+)-(.*)).zip ]]; then
        pkg_dir_name=${BASH_REMATCH[1]}
        blender_version=${BASH_REMATCH[2]}
        pkg_version=${BASH_REMATCH[3]}
        if ! check_pep440_compatible_version "${pkg_version}"; then
            echo "Invalid package: '${pkg}'. File version '${pkg_version}' does not conform with PEP440."
            ((invalid_package+=1))
            continue
        fi
    else
        echo "Invalid package: ${pkg}"
        ((invalid_package+=1))
        continue
    fi

    mkdir -p ${tmp_dir_path}
    unzip ${pkg} -d ${tmp_dir_path}
    pkg_dir_path=${tmp_dir_path}/${pkg_dir_name}
    if ! ${python_bin} "${SCRIPT_DIR}/python/run_tests.py" -p "${pkg_dir_path}" -v "${blender_version}"; then
        echo "Tests failed: ${pkg}"
        ((failed_test+=1))
        continue
    fi
    rm -rf ${tmp_dir_path}
done

if ((failed_test + invalid_package > 0)); then
    echo "Error: Found ${invalid_package} invalid packages and ${failed_test} failed tests."
    exit 1
fi

exit 0
