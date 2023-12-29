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

echo "Trying to get URL candidates to get the artifact ..."
artifacts_cands=$(
    curl --location --fail -s -H "Accept: application/vnd.github.v3+json" "https://api.github.com/repos/${owner}/${repository}/actions/runs" | \
        jq ".workflow_runs[] |
            select(.name == \"${workflow}\" and .conclusion == \"success\" and .artifacts_url != null)" | \
        jq -s ''
)

artifacts_cands_count=$(
    echo "${artifacts_cands}" | \
        jq ". |
            length"
)
if [ "${artifacts_cands_count}" -eq 0 ]; then
    echo "  Candidates for artifacts are not found."
    exit 1
fi
echo "  Found ${artifacts_cands_count} candidate(s)."

echo "Trying to get the artifact URL ..."
artifacts_url="null"
for i in $(seq 1 "${artifacts_cands_count}"); do
    index=$((i-1))
    artifacts_api_url=$(
        echo "${artifacts_cands}" | \
            jq "sort_by(.created_at) |
                reverse[${index}] |
                .artifacts_url" | \
            sed 's/^"\(.*\)"$/\1/'
    )

    artifacts=$(
        curl --location --fail -s -H "Accept: application/vnd.github.v3+json" "${artifacts_api_url}"
    )

    artifacts_count=$(
        echo "${artifacts}" | \
            jq ".artifacts | length"
    )

    if [ "${artifacts_count}" -ne 0 ]; then
        artifacts_url=$(
            curl --location --fail -s -H "Accept: application/vnd.github.v3+json" "${artifacts_api_url}" | \
                jq ".artifacts[0].archive_download_url" | \
                sed 's/^"\(.*\)"$/\1/'
        )
        break
    fi
done

if [ "${artifacts_url}" == "null" ]; then
    echo "  Artifacts are not found."
    exit 1
fi
echo "  Artifact URL is ${artifacts_url}."

echo "Downloading the artifact ..."
mkdir -p "${target_dir}"
if [ "${token_for_actions}" = "not-specified" ]; then
    curl --location --fail -s "${artifacts_url}" -o artifact-blender.zip
else
    curl --location --fail -s -H "Authorization: token ${token_for_actions}" "${artifacts_url}" -o artifact-blender.zip
fi

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
