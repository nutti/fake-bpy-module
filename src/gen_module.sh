#!/usr/bin/env bash
set -eEux

TMP_DIR_NAME=gen_module-tmp
# shellcheck disable=SC2046,SC2155,SC2164
{
SCRIPT_DIR=$(cd $(dirname "$0"); pwd)
}
PYTHON_BIN=${PYTHON_BIN:-python}

if [ $# -ne 6 ] && [ $# -ne 7 ]; then
    echo "Usage: bash gen_module.sh <source-dir> <blender-dir> <target> <branch/tag/commit> <target-version> <output-dir> [<mod-version>]"
    exit 1
fi

source_dir=${1}
blender_dir=${2}
target=${3}
git_ref=${4}
target_version=${5}
output_dir=${6}
mod_version=${7:-not-specified}
current_dir=$(pwd)
tmp_dir=${current_dir}/${TMP_DIR_NAME}
format=${GEN_MODULE_CODE_FORMAT:-pep8}
output_log_level=${GEN_MODULE_OUTPUT_LOG_LEVEL:-warn}

# find blender binary
# shellcheck disable=SC2003,SC2308,SC2046
{
if [ "$(uname)" == "Darwin" ]; then
    # macOSX
    blender_bin=${blender_dir}/blender.app/Contents/MacOS/blender
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    # Linux
    blender_bin=${blender_dir}/blender
else
    # Windows
    blender_bin=${blender_dir}/blender.exe
fi
}

echo "Checking if Blender binary exists ..."
if [ ! -e "${blender_bin}" ]; then
    echo "${blender_bin} is not exist"
    exit 1
fi

echo "Checking if Python binary exists ..."
if ! command -v "${PYTHON_BIN}" > /dev/null; then
    echo "Error: Cannot find ${PYTHON_BIN} binary."
    exit 1
fi
python_bin=$(command -v "${PYTHON_BIN}")

echo "Checking if Python version meets the requirements ..."
IFS=" " read -r -a python_version <<< "$(${python_bin} -c 'import sys; print(sys.version_info[:])' | tr -d '(),')"
if [ "${python_version[0]}" -lt 3 ] || [[ "${python_version[0]}" -eq 3 && "${python_version[1]}" -lt 7 ]]; then
    echo "Error: Unsupported python version \"${python_version[0]}.${python_version[1]}\". Requiring python 3.7 or higher."
    exit 1
fi

function get_remote_git_ref() {
    local ref=$1

    # 1. Try asking remote for ref. (git ls-remote)
    # 2. If multiple are found, take first one (head -n 1)
    # 3. Only save hash (cut -f1)
    # shellcheck disable=SC2155
    local remote_ref="$(git ls-remote origin "$ref" | head -n 1 | cut -f1)"

    # if remote ref was not found, it probably was a git hash
    if [ -z "${remote_ref}" ]; then
        remote_ref="$ref"
    fi

    echo "${remote_ref}"
}

# make temporary directory
mkdir -p "${tmp_dir}"

echo "Changing to the target git ref ..."
cd "${source_dir}"
remote_git_ref="$(get_remote_git_ref "${git_ref}")"
git fetch --depth 1 origin "${remote_git_ref}"
git checkout -f "${remote_git_ref}"

function apply_workaround() {
    local ref=${git_ref}
    local project_source=${source_dir}

    if [ "${target}" = "blender" ]; then
        if [ "${ref}" = "v2.90.0" ] || [ "${ref}" = "v2.91.0" ]; then
            pushd "${project_source}" > /dev/null

            # Workaround for an error of rst document generation.
            # See https://developer.blender.org/T80364 for detail.
            cp doc/python_api/sphinx_doc_gen.py doc/python_api/sphinx_doc_gen.py.orig
            sed -i -e "/Hair/s/^/#/" doc/python_api/sphinx_doc_gen.py
            sed -i -e "/PointCloud/s/^/#/" doc/python_api/sphinx_doc_gen.py

            popd > /dev/null
        fi
    fi
}

function revert_workaround() {
    local ref=${git_ref}
    local project_source=${source_dir}

    if [ "${target}" = "blender" ]; then
        if [ "${ref}" = "v2.90.0" ] || [ "${ref}" = "v2.91.0" ]; then
            pushd "${project_source}" > /dev/null
            git checkout doc/python_api/sphinx_doc_gen.py
            popd > /dev/null
        fi
    fi
}

echo "Generating rst documents ..."
cd "${current_dir}"
apply_workaround
${blender_bin} --background --factory-startup -noaudio --python-exit-code 1 --python "${source_dir}/doc/python_api/sphinx_doc_gen.py" -- --output "${tmp_dir}"
revert_workaround

# Apply patches
#   Note: patch is made by `diff -up gen_module-tmp/sphinx-in.orig/a.rst gen_module-tmp/sphinx-in/a.rst > patches/2.XX/sphinx-in/a.rst.patch`
cp -r "${tmp_dir}/sphinx-in" "${tmp_dir}/sphinx-in.orig"
if [ "${mod_version}" != "not-specified" ]; then
    echo "Applying patches ..."
    # shellcheck disable=SC2044
    for patch_file in $(find "${SCRIPT_DIR}/patches/${target}/${mod_version}/sphinx-in" -name "*.patch"); do
        patch -u -p2 -d "${tmp_dir}/sphinx-in" < "${patch_file}"
    done
fi

echo "Generating modfiles ..."

if ! find "${blender_dir}" -type d | grep -E "/[0-9.]{3,4}/scripts/startup$"; then
    echo "Could not find startup directory. (${blender_dir})"
    exit 1
fi
generated_mod_dir=${SCRIPT_DIR}/mods/generated_mods
mkdir -p "${generated_mod_dir}"
${blender_bin} --background --factory-startup -noaudio --python-exit-code 1 --python "${SCRIPT_DIR}/gen_modfile/gen_external_modules_modfile.py" -- -m addon_utils -o "${generated_mod_dir}/gen_modules_modfile"
${blender_bin} --background --factory-startup -noaudio --python-exit-code 1 --python "${SCRIPT_DIR}/gen_modfile/gen_external_modules_modfile.py" -- -m keyingsets_builtins -a -o "${generated_mod_dir}/gen_startup_modfile"
mkdir -p "${generated_mod_dir}/gen_bgl_modfile"
bgl_c_file="${source_dir}/source/blender/python/generic/bgl.c"
if [ ! -e "${bgl_c_file}" ]; then
    bgl_c_file="${source_dir}/source/blender/python/generic/bgl.cc"
fi
${python_bin} "${SCRIPT_DIR}/gen_modfile/gen_bgl_modfile.py" -i "${bgl_c_file}" -o "${generated_mod_dir}/gen_bgl_modfile/bgl.json"

echo "Generating fake bpy modules ..."
if [ "${mod_version}" = "not-specified" ]; then
    ${python_bin} "${SCRIPT_DIR}/gen.py" -i "${tmp_dir}/sphinx-in" -o "${output_dir}" -f "${format}" -T "${target}" -t "${target_version}" -l "${output_log_level}"
else
    ${python_bin} "${SCRIPT_DIR}/gen.py" -i "${tmp_dir}/sphinx-in" -o "${output_dir}" -f "${format}" -T "${target}" -t "${target_version}" -l "${output_log_level}" -m "${mod_version}"
fi

echo "Cleaning up ..."
cd "${current_dir}"
rm -rf "${tmp_dir}"
rm -rf "${generated_mod_dir}"
