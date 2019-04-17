#!/bin/sh

TMP_DIR_NAME=gen_module-tmp
SCRIPT_DIR=$(cd $(dirname $0); pwd)

if [ $# -ne 4 ]; then
    echo "Usage: sh gen_module.sh <source-dir> <blender-dir> <branch/tag/commit> <output-dir>"
    exit 1
fi

source_dir=${1}
blender_dir=${2}
branch_name=${3}
output_dir=${4}
current_dir=`pwd`
tmp_dir=${current_dir}/${TMP_DIR_NAME}

# make temporary directory
mkdir -p ${tmp_dir}

# change to the target branch/tag/commit
cd ${source_dir}
git fetch --prune
git checkout ${branch_name}
git pull origin ${branch_name}

# generate .rst documents
cd ${current_dir}
${blender_dir}/blender --background --factory-startup -noaudio --python ${source_dir}/doc/python_api/sphinx_doc_gen.py -- --output ${tmp_dir}

# convert .rst to .xml
mkdir -p ${tmp_dir}/sphinx-out-xml
sphinx-build -b xml ${tmp_dir}/sphinx-in ${tmp_dir}/sphinx-out-xml

# generate fake bpy modules
python3 ${SCRIPT_DIR}/gen.py -i ${tmp_dir}/sphinx-out-xml -o ${output_dir} -t pycharm -f pep8

# clear temporary directory
cd ${current_dir}
rm -rf ${tmp_dir}
