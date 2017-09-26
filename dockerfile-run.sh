#!/bin/sh
REPO_URI=docker-registry.laterooms.io:5000
CONTAINER=$(basename $PWD)

docker run --rm -it \
    ${REPO_URI}/${CONTAINER}:latest $*
