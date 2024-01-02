#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
pushd ${SCRIPT_DIR}/..
docker build . -f ${SCRIPT_DIR}/Dockerfile -t grhawk/cookiecutter-cpp-test-environment:latest && \
docker push grhawk/cookiecutter-cpp-test-environment:latest
popd

