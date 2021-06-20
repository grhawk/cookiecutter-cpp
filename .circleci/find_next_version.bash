#!/usr/bin/env bash

set -xe

actual_version_changelog=$(grep -P '\*\*\[\d+\.\d+\.\d+\]\*\*' "${CHANGELOG_FILE}" | head -n 1 | grep -oP '\d+\.\d+\.\d+')
actual_version_git=$(git tag -l | grep -P 'v\d+\.\d+\.\d+' | sort -t "." -k1,1n -k2,2n -k3,3n | sort -r | head -n 1 | grep -oP '\d+\.\d+\.\d+')
if [[ "${actual_version_changelog}" != "${actual_version_git}" ]]; then
  echo "Git version and CHANGELOG version are different!"
  exit 2
fi

echo "${actual_version_changelog}"


