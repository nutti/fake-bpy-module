#!/bin/sh

if [ $# -ne 1 ]; then
    echo "Usage: sh cleanup.sh <source-dir>"
    exit 1
fi

source_dir=${1}

# delete already created documents
cd ${source_dir}
rm -rf doc/python_api/sphinx-in doc/python_api/sphinx-in-tmp

