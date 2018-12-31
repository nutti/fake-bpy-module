#!/bin/bash
# require: bash version >= 4
# usage example: bash batch_gen_modules.sh 2.79 out

TMP_DIR_NAME=batch_gen_modules-tmp
SUPPORTED_VERSIONS=(
    "2.78" "2.78a" "2.78b" "2.78c"
    "2.79" "2.79a" "2.79b" "2.79c"
    "2.80"
    "all"
)

declare -A BLENDER_TAG_NAME=(
    ["v278"]="v2.78"
    ["v278a"]="v2.78a"
    ["v278b"]="v2.78b"
    ["v278c"]="v2.78c"
    ["v279"]="v2.79"
    ["v279a"]="v2.79a"
    ["v279b"]="v2.79b"
    ["v280"]="master"
)


# check arguments
if [ $# -ne 3 ]; then
    echo "Usage: sh batch_gen_module.sh <blender-dir-base> <version> <output-dir>"
    exit 1
fi

blender_dir_base=${1}
version=${2}
current_dir=`pwd`
output_dir=${3}
tmp_dir=${current_dir}/${TMP_DIR_NAME}

# check if the specified version is supported
supported=0
for v in "${SUPPORTED_VERSIONS[@]}"; do
    if [ ${v} = ${version} ]; then
        supported=1
    fi
done
if [ ${supported} -eq 0 ]; then
    echo "${version} is not supported."
    echo "Supported version is ${SUPPORTED_VERSIONS[@]}."
    exit 1
fi


# make temporary directory
mkdir -p ${tmp_dir}

# get Blender sources
cd ${tmp_dir}
git clone git://git.blender.org/blender.git


function generate_module() {
    ver=${1}

    target=blender-${ver}-bin
    blender_dir=${blender_dir_base}/${target}/blender.app/Contents/MacOS

    # change to the target branch/tag
    source_dir=${tmp_dir}/blender
    branch_name=${BLENDER_TAG_NAME[${ver}]}
    cd ${source_dir}
    git fetch --prune
    git checkout ${branch_name}
    git pull origin ${branch_name}

    # generate .rst documents
    docs_dir=${tmp_dir}/docs-${ver}
    cd ${current_dir}
    ${blender_dir}/blender --background --factory-startup -noaudio --python ${source_dir}/doc/python_api/sphinx_doc_gen.py -- --output ${docs_dir}

    # convert .rst to .xml
    cd ${current_dir}
    mkdir -p ${docs_dir}/sphinx-out-xml
    sphinx-build -b xml ${docs_dir}/sphinx-in ${docs_dir}/sphinx-out-xml

    # generate fake bpy modules
    cd ${current_dir}
    python ../src/gen.py -i ${docs_dir}/sphinx-out-xml -o ${output_dir}/${ver} -t pycharm -f pep8
}

if [ ${version} = "all" ]; then
    for KEY in ${!BLENDER_TAG_NAME[@]}; do
        generate_module ${KEY}
    done
else
    generate_module v${version%.*}${version##*.}
fi


# clear temporary directory
cd ${current_dir}
rm -rf ${tmp_dir}
