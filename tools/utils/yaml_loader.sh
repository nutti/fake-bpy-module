#!/usr/bin/env bash

# Check that required variables are defined
if [ -z "$REPO_ROOT" ]; then
    echo 'Error: REPO_ROOT must be defined before sourcing yaml_loader.sh (Path to the repository root)'
    exit 1
fi

if [ -z "$VERSIONS_YAML" ]; then
    echo 'Error: VERSIONS_YAML must be defined before sourcing yaml_loader.sh'
    # shellcheck disable=SC2016
    echo '  (Path to the versions.yml file, typically $REPO_ROOT/src/versions.yml)'
    exit 1
fi

# Function to load sequences from YAML into arrays
load_sequence_from_yaml() {
    local tag_name=$1
    declare -n arr=$tag_name
    local data

    data=$(yq ".${tag_name}" "$VERSIONS_YAML" -o=tsv)

    # Read data into array
    # shellcheck disable=SC2034
    IFS=$'\t' read -r -a arr <<< "$data"
}

# Function to load mappings from YAML into associative arrays
load_mapping_from_yaml() {
    local tag_name=$1
    declare -n mapping=$tag_name
    local data

    # Example data line is `key = value`.
    # ``... comments=""`` is needed to ensure comments are stripped.
    data=$(yq -r "... comments=\"\" | .$tag_name" "$VERSIONS_YAML" -oprops)

    # There are still empty mapping currently (e.g. `NEED_MOVE_WIN64`).
    [[ -z $data ]] && return

    # Populate the array
    while IFS=" = " read -r key value; do
        # shellcheck disable=SC2034
        mapping["$key"]="$value"
    done <<< "$data"
}
