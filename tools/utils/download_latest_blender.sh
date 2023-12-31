#!/usr/bin/env bash
set -eEu

if [ $# -ne 4 ] && [ $# -ne 5 ]; then
    echo "Usage: download_latest_blender.sh <owner> <repository> <workflow> <target_dir> <token_for_actions>"
    exit 1
fi

owner=${1}
repository=${2}
workflow=${3}
target_dir=${4}
token_for_actions=${5:-not-specified}

echo "Trying to get the artifact URL ..."
artifacts_url=
echo "  Artifact URL is ${artifacts_url}."

echo "Downloading the artifact ..."
mkdir -p "${target_dir}"
curl_args="--location --fail -s"
if [ "${token_for_actions}" != "not-specified" ]; then
    curl_args+=" -H 'Authorization: token ${token_for_actions}'"
fi
curl ${curl_args} "${artifacts_url}" -o artifact-blender.zip

echo "Decompressing the artifact ..."
unzip -o -d "${target_dir}" artifact-blender.zip

echo "Checking MD5 sum ..."
pushd "${target_dir}" 1> /dev/null
checksum=$(cat blender.tar.xz.md5)
if ! md5sum --check --status <<< "${checksum}"; then
    echo "Invalid checksum";
    exit 1
fi

echo "Decompressing the blender ..."
[ -e blender ] && rm -rf blender
tar xf blender.tar.xz
[ -e blender-latest-bin ] && rm -rf blender-latest-bin
mv blender blender-latest-bin
rm blender.tar.xz blender.tar.xz.md5
popd 1> /dev/null

echo "Done"
