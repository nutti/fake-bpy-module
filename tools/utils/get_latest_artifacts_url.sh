#!/usr/bin/env bash
set -eEu

if [ $# -ne 3 ]; then
    echo "Usage: get_latest_artifacts_url.sh <owner> <repository> <workflow>"
    exit 1
fi

owner=${1}
repository=${2}
workflow=${3}

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
    echo "Candidates for artifacts are not found."
    exit 1
fi

artifacts_url="null"
for i in $(seq 1 "${artifacts_cands_count}"); do
    index=$((i-1))
    artifacts_api_url=$(
        echo "${artifacts_cands}" | \
            jq -r "sort_by(.created_at) |
                reverse[${index}] |
                .artifacts_url"
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
                jq -r ".artifacts[0].archive_download_url"
        )
        break
    fi
done

if [ "${artifacts_url}" == "null" ]; then
    echo "Artifacts are not found."
    exit 1
fi
echo -n "${artifacts_url}"
