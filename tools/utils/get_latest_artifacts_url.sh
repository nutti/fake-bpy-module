#!/usr/bin/env bash
set -eEu

if [ $# -ne 3 ]; then
    echo "Usage: get_latest_artifacts_url.sh <owner> <repository> <workflow>"
    exit 1
fi

owner=${1}
repository=${2}
workflow=${3}

artifacts_url="null"
artifacts_cands=$(
    curl --location --fail -s -H "Accept: application/vnd.github.v3+json" "https://api.github.com/repos/${owner}/${repository}/actions/runs" | \
        jq -r ".workflow_runs[] |
            select(.name == \"${workflow}\" and .conclusion == \"success\" and .artifacts_url != null) |
            .artifacts_url"
)

# artifacts_cands are sorted in created_at order when retrieved
for artifacts_api_url in ${artifacts_cands}; do
    artifacts_url=$(
        curl --location --fail -s -H "Accept: application/vnd.github.v3+json" "${artifacts_api_url}" | \
            jq -r ".artifacts[0].archive_download_url"
    )
    if [ "${artifacts_url}" != "null" ]; then
        break
    fi
done

if [ "${artifacts_url}" == "null" ]; then
    echo "Artifacts are not found."
    exit 1
fi
echo -n "${artifacts_url}"
