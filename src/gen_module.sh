#!/usr/bin/env bash
set -eEuxo pipefail

TMP_DIR_NAME=gen_module-tmp
PROFILER_RESULT_FILENAME="profiler_result.prof"
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
env_temporary_dir=${TEMPORARY_DIR:-not-specified}
if [ "${env_temporary_dir}" == "not-specified" ]; then
    tmp_dir=${current_dir}/${TMP_DIR_NAME}
else
    tmp_dir=${env_temporary_dir}
fi

format=${GEN_MODULE_CODE_FORMAT:-ruff}
output_log_level=${GEN_MODULE_OUTPUT_LOG_LEVEL:-warn}
enable_python_profiler=${ENABLE_PYTHON_PROFILER:-false}

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
if [ "${python_version[0]}" -lt 3 ] || [[ "${python_version[0]}" -eq 3 && "${python_version[1]}" -lt 11 ]]; then
    echo "Error: Unsupported python version \"${python_version[0]}.${python_version[1]}\". Requiring python 3.11 or higher."
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

# Generate rst if sphinx_doc_gen.py is newer than output directory
if [[ "${tmp_dir}/sphinx-in" -ot "${source_dir}/doc/python_api/sphinx_doc_gen.py" ]]; then
    apply_workaround
    ${blender_bin} --background --factory-startup -noaudio --python-exit-code 1 --python "${source_dir}/doc/python_api/sphinx_doc_gen.py" -- --output "${tmp_dir}"
    revert_workaround
    touch "${tmp_dir}/sphinx-in"
    rm -rf "${tmp_dir}/sphinx-in.orig"
fi

if [[ ! -d "${tmp_dir}/sphinx-in.orig" && "${mod_version}" != "not-specified" ]]; then
    cp -rp "${tmp_dir}/sphinx-in" "${tmp_dir}/sphinx-in.orig"

    # Apply patches
    #   Note: patch is made by `diff -up gen_module-tmp/sphinx-in.orig/a.rst gen_module-tmp/sphinx-in/a.rst > patches/2.XX/sphinx-in/a.rst.patch`
    echo "Applying patches ..."
    # shellcheck disable=SC2044
    for patch_file in $(find "${SCRIPT_DIR}/patches/${target}/${mod_version}/sphinx-in" -name "*.patch"); do
        patch -u -p2 -d "${tmp_dir}/sphinx-in" < "${patch_file}"
    done
fi

# Fix invalid rst format.
echo "Fixing invalid rst format ..."
if [ "${target}" = "blender" ]; then
    if [ "${git_ref}" = "v3.5.0" ]; then
        # :file:`XXX` -> :file: `XXX`
        echo "  Fix: ':file:\`' -> ':file: \`"
        # shellcheck disable=SC2044
        for rst_file in $(find "${tmp_dir}/sphinx-in" -name "*.rst"); do
            search_str=":file:\`"
            replace_str=":file: \`"
            if grep -q "${search_str}" "${rst_file}"; then
                echo "    ${rst_file}"
                sed -i "s/${search_str}/${replace_str}/g" "${rst_file}"
            fi
        done
    elif [ "${git_ref}" = "v2.90.0" ]; then
        #       .. note:: Takes ``O(len(nodetree.links))`` time.
        #       (readonly)
        # ->
        #       .. note:: Takes ``O(len(nodetree.links))`` time.
        #
        #       (readonly)
        echo "  Fix: Invalid (readonly) position"
        # shellcheck disable=SC2044
        for rst_file in $(find "${tmp_dir}/sphinx-in" -name "*.rst"); do
            if ! perl -ne 'BEGIN{$/="";}{exit(1) if /(..note::.*?)\n(\s*\(readonly\))/;}' "${rst_file}"; then
                echo "    ${rst_file}"
                perl -i -pe 'BEGIN{$/="";}{s/(..note::.*?)\n(\s*\(readonly\))/$1\n\n$2/g;}' "${rst_file}"
            fi
        done
    elif [ "${git_ref}" = "v2.78c" ] || [ "${git_ref}" = "v2.79b" ]; then
        # .. code-block:: none -> .. code-block:: python
        echo "  Fix: Invalid code-block argument"
        # shellcheck disable=SC2044
        for rst_file in $(find "${tmp_dir}/sphinx-in" -name "*.rst"); do
            search_str=".. code-block:: none"
            replace_str=".. code-block:: python"
            if grep -q "${search_str}" "${rst_file}"; then
                echo "    ${rst_file}"
                sed -i "s/${search_str}/${replace_str}/g" "${rst_file}"
            fi
        done
    fi
elif [ "${target}" = "upbge" ]; then
    # .. code-block:: none -> .. code-block:: python
    echo "  Fix: Invalid code-block argument"
    # shellcheck disable=SC2044
    for rst_file in $(find "${tmp_dir}/sphinx-in" -name "*.rst"); do
        search_str=".. code-block:: none"
        replace_str=".. code-block:: python"
        if grep -q "${search_str}" "${rst_file}"; then
            echo "    ${rst_file}"
            sed -i "s/${search_str}/${replace_str}/g" "${rst_file}"
        fi
    done

    if [ "${git_ref}" = "v0.2.5" ]; then
        echo "  Fix: Inconsistent title levels."
        # shellcheck disable=SC2044
        for rst_file in $(find "${tmp_dir}/sphinx-in" -name "*.rst"); do
            rst_file_basename=$(basename "${rst_file}")
            if [ "${rst_file_basename}" = "bge.texture.rst" ]; then
                search_str="+++++++++++++*"
                replace_str=""
                echo "    ${rst_file}"
                sed -i "s/${search_str}/${replace_str}/g" "${rst_file}"
            fi
        done
    fi
fi

echo "Generating modfiles ..."

if ! find "${blender_dir}" -type d | grep -E "/[0-9.]{3,4}/scripts/startup$"; then
    echo "Could not find startup directory. (${blender_dir})"
    exit 1
fi
generated_mod_dir=${SCRIPT_DIR}/mods/generated_mods

# generate modfiles if gen_modfile.py is newer
[ ! -d "${generated_mod_dir}" ] && mkdir -p "${generated_mod_dir}"
if [[ "${generated_mod_dir}/gen_modules_modfile" -ot "${SCRIPT_DIR}/gen_modfile/gen_external_modules_modfile.py" ]]; then
    ${blender_bin} --background --factory-startup -noaudio --python-exit-code 1 --python "${SCRIPT_DIR}/gen_modfile/gen_external_modules_modfile.py" -- -m addon_utils -o "${generated_mod_dir}/gen_modules_modfile" -f rst
    touch "${generated_mod_dir}/gen_modules_modfile"
fi
if [[ "${generated_mod_dir}/gen_startup_modfile" -ot "${SCRIPT_DIR}/gen_modfile/gen_external_modules_modfile.py" ]]; then
    ${blender_bin} --background --factory-startup -noaudio --python-exit-code 1 --python "${SCRIPT_DIR}/gen_modfile/gen_external_modules_modfile.py" -- -m keyingsets_builtins -a -o "${generated_mod_dir}/gen_startup_modfile" -f rst
    touch "${generated_mod_dir}/gen_startup_modfile"
fi

# generate bgl modfile if gen_bgl_modfile.py and source is newer
bgl_c_file="${source_dir}/source/blender/python/generic/bgl.c"
if [ ! -e "${bgl_c_file}" ]; then
    bgl_c_file="${source_dir}/source/blender/python/generic/bgl.cc"
fi
if [[ "${generated_mod_dir}/gen_bgl_modfile/bgl.mod.rst" -ot "${SCRIPT_DIR}/gen_modfile/gen_bgl_modfile.py" || "${generated_mod_dir}/gen_bgl_modfile/bgl.mod.rst" -ot "${bgl_c_file}" ]]; then
    mkdir -p "${generated_mod_dir}/gen_bgl_modfile"
    ${python_bin} "${SCRIPT_DIR}/gen_modfile/gen_bgl_modfile.py" -i "${bgl_c_file}" -o "${generated_mod_dir}/gen_bgl_modfile/bgl.mod.rst" -f rst
fi

python_args=""
if "${enable_python_profiler}"; then
    python_args="-m profile -s cumtime -o ${SCRIPT_DIR}/../${PROFILER_RESULT_FILENAME}"
fi

echo "Generating fake bpy modules ..."
if [ "${mod_version}" = "not-specified" ]; then
    # shellcheck disable=SC2086
    ${python_bin} ${python_args} "${SCRIPT_DIR}/gen.py" -i "${tmp_dir}/sphinx-in" -o "${output_dir}" -f "${format}" -T "${target}" -t "${target_version}" -l "${output_log_level}"
else
    # shellcheck disable=SC2086
    ${python_bin} ${python_args} "${SCRIPT_DIR}/gen.py" -i "${tmp_dir}/sphinx-in" -o "${output_dir}" -f "${format}" -T "${target}" -t "${target_version}" -l "${output_log_level}" -m "${mod_version}"
fi

echo "Cleaning up ..."
cd "${current_dir}"
if [ "${env_temporary_dir}" == "not-specified" ]; then
    rm -rf "${tmp_dir}"
    rm -rf "${generated_mod_dir}"
fi
