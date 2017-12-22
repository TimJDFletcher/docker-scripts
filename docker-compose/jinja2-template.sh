#!/bin/bash -e
FILENAME=image_full_tag.txt
CLI="--strict --format=json"

images=( images/* )            # load list of images
images=( "${images[@]##*/}" )  # strip off directory name

for ((i=0; i < ${#images[@]}; i++)) ; do
    export "${images[$i]}=$(cat images/${images[$i]}/${FILENAME})"
done

python -c 'import json, os;print(json.dumps(dict(os.environ)))' | jinja2 $CLI $1
