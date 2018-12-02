#!/bin/sh

TMP_DIR=./gen_module-tmp

if [ $# -ne 4 ]; then
    echo "Usage: sh gen_module.sh <source-dir> <blender-dir> <version> <output-dir>"
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
git checkout v${version}

cd ${current_dir}

# generate .rst documents
${blender_dir}/blender --background --factory-startup -noaudio --python ${source_dir}/doc/python_api/sphinx_doc_gen.py

# convert .rst to .xml
sphinx-build -b xml ${source_dir}/doc/python_api/sphinx-in ${TMP_DIR}

# generate fake bpy modules
python gen.py -i ${TMP_DIR} -o ${output_dir} -t pycharm -f pep8

# clear temporary directory
cd ${current_dir}
rm -rf ${TMP_DIR}
