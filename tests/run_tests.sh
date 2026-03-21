#!/usr/bin/env bash
set -eEu

if [ $# -ne 1 ]; then
    echo "Usage: run_tests.sh <packages_path>"
    exit 1
fi

PACKAGES_PATH=${1}
# shellcheck disable=SC2046,SC2155,SC2164
{
SCRIPT_DIR=$(cd $(dirname "$0"); pwd)
}
TMP_DIR_NAME="tmp"
PYTHON_BIN=${PYTHON_BIN:-python}

# check if PYTHON_BIN binary is availble
if ! command -v "${PYTHON_BIN}" > /dev/null; then
    echo "Error: Cannot find ${PYTHON_BIN} binary."
    exit 1
fi
python_bin=$(command -v "${PYTHON_BIN}")

# check if python version meets our requirements
"$python_bin" -c "
import sys
if sys.version_info < (3, 11):
    print(f'Error: Python 3.11+ required, got {sys.version_info[:3]}')
    sys.exit(1)
"

function check_pep440_compatible_version() {
    local version="${1}"
    ${python_bin} -c "from setuptools._vendor.packaging.version import Version; Version(\"${version}\")"
    return $?
}

tmp_dir_path="${SCRIPT_DIR}/${TMP_DIR_NAME}"

invalid_package=0
failed_test=0
found_zip=false

# shellcheck disable=SC2044
for pkg in $(find "${PACKAGES_PATH}" -name "*.zip"); do
    found_zip=true
    if [[ ${pkg} =~ (fake_(bpy|bge)_modules_([a-z0-9\.]+)-(.*)).zip ]]; then
        pkg_dir_name=${BASH_REMATCH[1]}
        pkg_version=${BASH_REMATCH[4]}
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

    mkdir -p "${tmp_dir_path}"
    unzip "${pkg}" -d "${tmp_dir_path}"
    pkg_dir_path=${tmp_dir_path}/${pkg_dir_name}

    # Remove -stub from directory name to supress error.
    find "${pkg_dir_path}" -type d -name "*-stubs" | while IFS= read -r dir; do
        if [[ "${dir}" == *-stubs ]]; then
            new_dir="${dir%-stubs}/"
            mv "${dir}" "${new_dir}"
        fi
    done

    if ! ${python_bin} "${SCRIPT_DIR}/python/import_module_test/run_tests.py" -p "${pkg_dir_path}"; then
        echo "Import module test failed: ${pkg}"
        ((failed_test+=1))
        continue
    fi
    rm -rf "${tmp_dir_path}"
done

if ((failed_test + invalid_package > 0)); then
    echo "Error: Found ${invalid_package} invalid packages and ${failed_test} failed tests."
    exit 1
fi

if ! $found_zip; then
    echo "Error: Couldn't find .zip files in '${PACKAGES_PATH}' to run the tests. Build .zip file using build_pip_package.sh first."
    exit 1
fi

exit 0
