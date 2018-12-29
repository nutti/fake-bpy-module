#!/bin/bash
# require: bash version >= 4
# usage example: bash full_auto_gen_module.sh 2.79 out

TMP_DIR_NAME=full_auto_gen_module-tmp
SUPPORTED_VERSIONS=(
    "2.78" "2.78a" "2.78b" "2.78c"
    "2.79" "2.79a" "2.79b" "2.79c"
    "2.80"
    "all"
)

declare -A BLENDER_DOWNLOAD_URL=(
    ["v278"]="https://download.blender.org/release/Blender2.78/blender-2.78-OSX_10.6-x86_64.zip"
    ["v278a"]="https://download.blender.org/release/Blender2.78/blender-2.78a-OSX_10.6-x86_64.zip"
    ["v278b"]="https://download.blender.org/release/Blender2.78/blender-2.78b-OSX_10.6-x86_64-fixed.zip"
    ["v278c"]="https://download.blender.org/release/Blender2.78/blender-2.78c-OSX_10.6-x86_64.zip"
    ["v279"]="https://download.blender.org/release/Blender2.79/blender-2.79-macOS-10.6.tar.gz"
    ["v279a"]="https://download.blender.org/release/Blender2.79/blender-2.79a-macOS-10.6.zip"
    ["v279b"]="https://download.blender.org/release/Blender2.79/blender-2.79b-macOS-10.6.zip"
    ["v280"]="https://builder.blender.org/download/blender-2.80-7c438e5366b2-OSX-10.9-x86_64.zip"
)

declare -A BLENDER_TAG_NAME=(
    ["v278"]="v2.78"
    ["v278a"]="v2.78a"
    ["v278b"]="v2.78b"
    ["v278c"]="v2.78c"
    ["v279"]="v2.79"
    ["v279a"]="v2.79a"
    ["v279b"]="v2.79b"
    ["v280"]="v2.80"
)


# check arguments
if [ $# -ne 2 ]; then
    echo "Usage: sh full_auto_gen_module.sh <version> <output-dir>"
    exit 1
fi

version=${1}
current_dir=`pwd`
output_dir=${2}
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

    # download Blender binary
    cd ${tmp_dir}
    target=blender-${ver}-bin
    mkdir -p ${tmp_dir}/${target}
    cd ${tmp_dir}/${target}

    url=${BLENDER_DOWNLOAD_URL[${ver}]}
    filename=${target}
    if [ ${url##*.} = "zip" ]; then
        filename=${filename}.zip
        curl ${url} -o ${filename}
        unzip ${filename}
    elif [ ${url##*.} = "gz" ]; then
        filename=${filename}.gz
        curl ${url} -o ${filename}
        tar xvfz ${filename}
    fi
    blender_dir=${tmp_dir}/${target}/blender.app/Contents/MacOS

    # change to the target branch/tag
    source_dir=${tmp_dir}/blender
    branch_name=${BLENDER_TAG_NAME[${ver}]}
    cd ${source_dir}
    git fetch --prune
    git checkout ${branch_name}
    git pull origin ${branch_name}

    # generate .rst documents
    ${blender_dir}/blender --background --factory-startup -noaudio --python ${source_dir}/doc/python_api/sphinx_doc_gen.py -- --output ${tmp_dir}

    # convert .rst to .xml
    mkdir -p ${tmp_dir}/sphinx-out-xml
    sphinx-build -b xml ${tmp_dir}/sphinx-in ${tmp_dir}/sphinx-out-xml

    # generate fake bpy modules
    cd ${current_dir}
    python ../src/gen.py -i ${tmp_dir}/sphinx-out-xml -o ${output_dir}/${ver} -t pycharm -f pep8
}

if [ ${version} = "all" ]; then
    for KEY in ${!BLENDER_DOWNLOAD_URL[@]}; do
        generate_module ${KEY}
    done
else
    generate_module v${1%.*}${1##*.}
fi


# clear temporary directory
cd ${current_dir}
rm -rf ${tmp_dir}
