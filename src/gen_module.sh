#!/bin/bash

TMP_DIR_NAME=gen_module-tmp
SCRIPT_DIR=$(cd $(dirname $0); pwd)

if [ $# -ne 4 ] && [ $# -ne 5 ]; then
    echo "Usage: bash gen_module.sh <source-dir> <blender-dir> <branch/tag/commit> <output-dir> [<mod-version>]"
    exit 1
fi

source_dir=${1}
blender_dir=${2}
branch_name=${3}
output_dir=${4}
mod_version=${5}
current_dir=`pwd`
tmp_dir=${current_dir}/${TMP_DIR_NAME}

# find blender binary
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

if [ ! -e ${blender_bin} ]; then
    echo "${blender_bin} is not exist"
    exit 1
fi

# make temporary directory
mkdir -p ${tmp_dir}

# change to the target branch/tag/commit
cd ${source_dir}
git fetch --prune
git checkout master
git pull origin master
git checkout -f ${branch_name}
git pull origin ${branch_name}

# generate .rst documents
cd ${current_dir}
${blender_bin} --background --factory-startup -noaudio --python ${source_dir}/doc/python_api/sphinx_doc_gen.py -- --output ${tmp_dir}

# convert .rst to .xml
mkdir -p ${tmp_dir}/sphinx-out-xml
sphinx-build -b xml ${tmp_dir}/sphinx-in ${tmp_dir}/sphinx-out-xml

# generate modfiles
startup_dir=`find ${blender_dir} -type d | egrep "/[0-9.]{4}/scripts/startup$"`
if [ $? -ne 0 ]; then
    echo "Could not find startup directory. (${blender_dir})"
    exit 1
fi
generated_mod_dir=${SCRIPT_DIR}/mods/generated_mods
mkdir -p ${generated_mod_dir}
${blender_bin} --background --factory-startup -noaudio --python ${SCRIPT_DIR}/gen_modfile/gen_modules_modfile.py -- -m addon_utils -o ${generated_mod_dir}/gen_modules_modfile
mkdir ${generated_mod_dir}/gen_startup_modfile
python ${SCRIPT_DIR}/gen_modfile/gen_startup_modfile.py -i ${blender_dir}/${startup_dir} -o ${generated_mod_dir}/gen_startup_modfile/bpy.json
mkdir ${generated_mod_dir}/gen_bgl_modfile
python ${SCRIPT_DIR}/gen_modfile/gen_bgl_modfile.py -i ${source_dir}/source/blender/python/generic/bgl.c -o ${generated_mod_dir}/gen_bgl_modfile/bgl.json

# generate fake bpy modules
if [ ${mod_version} = "" ]; then
    python ${SCRIPT_DIR}/gen.py -i ${tmp_dir}/sphinx-out-xml -o ${output_dir} -f pep8
else
    python ${SCRIPT_DIR}/gen.py -i ${tmp_dir}/sphinx-out-xml -o ${output_dir} -f pep8 -m ${mod_version}
fi

# clear temporary directory
cd ${current_dir}
rm -rf ${tmp_dir}
rm -rf ${generated_mod_dir}