# docker-scripts

These are some helpful docker scripts for working with Dockerfiles and building them.

There are 3 scripts:

* `dockerfile-build.sh` this builds a dockerfile in the current directory and tags it correctly

* `dockerfile-run.sh` this runs the latest tag of the dockerfile in the current directory

* `dockerfile-deploy.sh` pushs a built docker container with a date based tag to our repo

The default name for the container is $PWD
