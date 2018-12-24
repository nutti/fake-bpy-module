#!/bin/sh

TMP_DIR=./gen_module-tmp

if [ $# -ne 4 ]; then
    echo "Usage: sh gen_module.sh <source-dir> <blender-dir> <version> <output-dir>"
    exit 1
fi

source_dir=${1}
blender_dir=${2}
version=${3}
output_dir=${4}
current_dir=`pwd`

# make temporary directory
mkdir -p ${TMP_DIR}

# change to the target branch/tag
cd ${source_dir}
git fetch --prune
git checkout ${version}
git pull origin ${version}

cd ${current_dir}

# generate .rst documents
${blender_dir}/blender --background --factory-startup -noaudio --python ${source_dir}/doc/python_api/sphinx_doc_gen.py -- --output ${TMP_DIR}

# convert .rst to .xml
mkdir -p ${TMP_DIR}/sphinx-out-xml
sphinx-build -b xml ${TMP_DIR}/sphinx-in ${TMP_DIR}/sphinx-out-xml

# generate fake bpy modules
python gen.py -i ${TMP_DIR}/sphinx-out-xml -o ${output_dir} -t pycharm -f pep8

# clear temporary directory
cd ${current_dir}
rm -rf ${TMP_DIR}
