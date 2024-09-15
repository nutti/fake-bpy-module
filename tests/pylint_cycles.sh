#!/usr/bin/env bash
set -eEu

if [ $# -ne 4 ]; then
    echo "Usage: pylint_test.sh <target> <target-version> <target-source-dir> <fake-bpy-wheel-file>"
    exit 1
fi

declare -r IGNORED_PYLINT_ERRORS=(
    "C" # convention, for programming standard violation
    "R" # refactor, for bad code smell
    "W" # warning, for python specific problems
    "E0601" # used-before-assignment: Lots of false positives for cases like "if xxx in locals()"
    "E0602" # undefined-variable: Lots of false positives for cases like "if xxx in locals()"
    "E1111" # assignment-from-no-return: Is difficult to handle in fake-module, ignoring for now
)

declare -r SUPPORTED_BLENDER_VERSIONS=(
    "2.78" "2.79" "2.80" "2.81" "2.82" "2.83"
    "2.90" "2.91" "2.92" "2.93"
    "3.0" "3.1" "3.2" "3.3" "3.4" "3.5" "3.6"
    "4.0" "4.1" "4.2"
    "latest"
)
declare -r SUPPORTED_UPBGE_VERSIONS=(
    "0.2.5"
    "latest"
)

declare -A BLENDER_TAG_NAME=(
    ["v2.78"]="v2.78c"
    ["v2.79"]="v2.79b"
    ["v2.80"]="v2.80"
    ["v2.81"]="v2.81a"
    ["v2.82"]="v2.82a"
    ["v2.83"]="v2.83.9"
    ["v2.90"]="v2.90.0"
    ["v2.91"]="v2.91.0"
    ["v2.92"]="v2.92.0"
    ["v2.93"]="v2.93.0"
    ["v3.0"]="v3.0.0"
    ["v3.1"]="v3.1.0"
    ["v3.2"]="v3.2.0"
    ["v3.3"]="v3.3.0"
    ["v3.4"]="v3.4.0"
    ["v3.5"]="v3.5.0"
    ["v3.6"]="v3.6.0"
    ["v4.0"]="v4.0.0"
    ["v4.1"]="v4.1.0"
    ["v4.2"]="v4.2.0"
    ["vlatest"]="main"
)
declare -A UPBGE_TAG_NAME=(
    ["v0.2.5"]="v0.2.5"
    ["vlatest"]="master"
)

target=${1}
version=${2}
source_dir=${3}
fake_module_wheel=${4}
PYTHON_BIN=${PYTHON_BIN:-python}

# check if the specified version is supported
supported=0
if [ "${target}" = "blender" ]; then
    for v in "${SUPPORTED_BLENDER_VERSIONS[@]}"; do
        if [ "${v}" = "${version}" ]; then
            supported=1
        fi
    done
    if [ ${supported} -eq 0 ]; then
        echo "${version} is not supported."
        echo "Supported version is ${SUPPORTED_BLENDER_VERSIONS[*]}."
        exit 1
    fi
elif [ "${target}" = "upbge" ]; then
    for v in "${SUPPORTED_UPBGE_VERSIONS[@]}"; do
        if [ "${v}" = "${version}" ]; then
            supported=1
        fi
    done
    if [ ${supported} -eq 0 ]; then
        echo "${version} is not supported."
        echo "Supported version is ${SUPPORTED_UPBGE_VERSIONS[*]}."
        exit 1
    fi
else
    echo "${target} is not supported."
    exit 1
fi

# Create temporary folder and delete on ERR and EXIT
temp_venv="$(mktemp -d)"
trap 'rm -rf "${temp_venv}"' ERR EXIT

# check if PYTHON_BIN binary is availble
if ! command -v "${PYTHON_BIN}" > /dev/null; then
    echo "Error: Cannot find ${PYTHON_BIN} binary."
    exit 1
fi
python_bin=$(command -v "${PYTHON_BIN}")

# check if python version meets our requirements
IFS=" " read -r -a python_version <<< "$(${python_bin} -c 'import sys; print(sys.version_info[:])' | tr -d '(),')"
if [ "${python_version[0]}" -lt 3 ] || [[ "${python_version[0]}" -eq 3 && "${python_version[1]}" -lt 12 ]]; then
    echo "Error: Unsupported Python version \"${python_version[0]}.${python_version[1]}\". Requiring Python 3.12 or higher."
    exit 1
fi

function get_remote_git_ref() {
    local ref=$1

    # 1. Try asking remote for ref. (git ls-remote)
    # 2. If multiple are found, take first one (head -n 1)
    # 3. Only save hash (cut -f1)
    local remote_ref
    remote_ref="$(git ls-remote origin "$ref" | head -n 1 | cut -f1)"

    # if remote ref was not found, it probably was a git hash
    if [ -z "${remote_ref}" ]; then
        remote_ref="$ref"
    fi

    echo "${remote_ref}"
}


# generate pylint disable list
function join_array_by {
    local IFS="$1"
    shift
    echo "$*"
}

# generating a .pylintrc to ignore specific circumstances
# see here for specification: https://github.com/PyCQA/pylint/blob/master/pylintrc
function create_pylintrc() {
    local pylintrc=${1}
    local disabled_pylint_warning
    disabled_pylint_warning=$(join_array_by ',' "${IGNORED_PYLINT_ERRORS[@]}")

    echo "Generating ${pylintrc}"

    echo > "${pylintrc}"
    # shellcheck disable=SC2129
    echo "[MESSAGES CONTROL]" >> "${pylintrc}"
    echo "disable=${disabled_pylint_warning}" >> "${pylintrc}"

    echo "[TYPECHECK]" >> "${pylintrc}"
    echo "ignored-modules=_cycles" >> "${pylintrc}"
    echo "ignored-classes=CyclesPreferences" >> "${pylintrc}"
}

function workaround_quirks() {
    local target=$1
    local version=$2

    if [ "${target}" = "blender" ]; then
        if [[ $version =~ ^2.7[89]$ ]]; then
            # bpy.types.XXX related Cycle add-on classes are  not provided by fake-bpy-module
            echo "Fixing cycles class: \".bpy.types.CYCLES_MT_[a-z]*_presets\""
            sed -i 's/bpy.types.\(CYCLES_MT_[a-z]*_presets\)/\1/' intern/cycles/blender/addon/ui.py

            echo "Fixing pylint bug: https://github.com/pylint-dev/pylint/issues/3105"
            sed -i 's/for \(.*\?\) in self\.devices:/for \1 in [self.devices]:/' intern/cycles/blender/addon/properties.py
        fi

        # pylint does not respect a `hasattr` in `if hasattr(myclass, field) and myclass.field == test`
        echo "Ignoring pylint bug: https://github.com/PyCQA/pylint/issues/801"
        sed -i '/^\s*if hasattr(.*/i # pylint: disable=no-member' intern/cycles/blender/addon/*.py
    elif [ "${target}" = "upbge" ]; then
        if [[ $version =~ ^0.2.5$ ]]; then
            # bpy.types.XXX related Cycle add-on classes are not provided by fake-module
            echo "Fixing cycles class: \".bpy.types.CYCLES_MT_[a-z]*_presets\""
            sed -i 's/bpy.types.\(CYCLES_MT_[a-z]*_presets\)/\1/' intern/cycles/blender/addon/ui.py

            echo "Fixing pylint bug: https://github.com/pylint-dev/pylint/issues/3105"
            sed -i 's/for \(.*\?\) in self\.devices:/for \1 in [self.devices]:/' intern/cycles/blender/addon/properties.py
        fi
    fi
}


function run_pylint_test() {
    local path=${1}
    local path_to_pylintrc=${2}
    local additional_parameters=${3:-}

    local returncode=0

    # shellcheck disable=SC2086
    PYLINTRC=${path_to_pylintrc} pylint ${additional_parameters} "${path}" || returncode=$?

    return ${returncode}
}

# Generate a venv, so it does not interfere with local setup
echo "Creating temporary virtualenv for ${python_bin} at ${temp_venv}"
${python_bin} -m venv "${temp_venv}"
# shellcheck source=/dev/null
source "${temp_venv}"/bin/activate

# install pylint
pip install --quiet pylint

# Install dependencies
pip install numpy

# Enter source
pushd "${source_dir}"

if [ "${target}" = "blender" ]; then
    git_tag="${BLENDER_TAG_NAME[v${version}]}"
elif [ "${target}" = "upbge" ]; then
    git_tag="${UPBGE_TAG_NAME[v${version}]}"
fi
remote_git_ref="$(get_remote_git_ref "${git_tag}")"

echo "Checking out git tag ${git_tag}"
git fetch --quiet --depth 1 origin "${remote_git_ref}"
git checkout -f "${remote_git_ref}"

# Generate and print pylintrc
pylintrcpath="${temp_venv}/pylintrc"

create_pylintrc "${pylintrcpath}"
echo "Testing with the following pylintrc:"
cat "${pylintrcpath}"
echo

# Fixing addon code to workaround some quirks
workaround_quirks "${target}" "${version}"
echo

# Expect failure before fake-module is installed, otherwise following test has no meaning
echo "Verifying that there are errors on the targeted test before fake-module is installed."
if run_pylint_test ./intern/cycles/blender/addon/ "${pylintrcpath}" 1> /dev/null; then
    echo "Error: Test was successfull even without the fake-module installed."
    exit 1
else
    echo "PASS: Test before installing fake-module had errors."
fi

# Leave source folder to support relative wheel installations
popd > /dev/null

# install fake-module
echo
pip install "${fake_module_wheel}"

# Re-enter source
pushd "${source_dir}" > /dev/null

# Run the "real" test now
echo
echo "Running test again with fake-module:"
run_pylint_test ./intern/cycles/blender/addon/ "${pylintrcpath}"
echo "PASS: Final test has been passed."

popd

# disable venv
deactivate
