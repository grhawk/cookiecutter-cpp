#!/usr/bin/env bash

set -xe

NEXT_VERSION=$1
PROJECT_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
CHANGELOG_FILE="${PROJECT_FOLDER}/../CHANGELOG.md"
SETUP_FILE="${PROJECT_FOLDER}/../setup.py"

# Update CHANGELOG_FILE.md
sed -i "s/\*\*\[Unreleased\]\*\*/\*\*\[Unreleased\]\*\*\n\n\*\*\[${NEXT_VERSION}\]\*\*/" "${CHANGELOG_FILE}"

# Update setup.py
last_version_setup=$(grep -P "version='\d+\.\d+\.\d+'," setup.py)
sed -i "s/${last_version_setup}/    version='${NEXT_VERSION}',/" "${SETUP_FILE}"
