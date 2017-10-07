# docker-scripts

These are some helpful docker scripts for working with Dockerfiles and building them.

There is a makefile (`docker-makefile`) included here now that does the same job as these scripts, copy it you docker repo with the filename `Makefile` and then run make in your repo.

You may need to tweak the container name and the test parms for your docker container.

There are 3 scripts:

* `dockerfile-build.sh` this builds a dockerfile in the current directory and tags it correctly

* `dockerfile-run.sh` this runs the latest tag of the dockerfile in the current directory

* `dockerfile-deploy.sh` pushs a built docker container with a date based tag to our repo

The default name for the container is $PWD

## Makefile notes

Built be @timjdfletcher after seeing something in DevOps weekly.

Original post: https://container-solutions.com/tagging-docker-images-the-right-way/

Another docker and make gist: https://gist.github.com/mpneuried/0594963ad38e68917ef189b4e6a269db

Makefile notes:

* http://www.alexeyshmalko.com/2014/7-things-you-should-know-about-make/
* http://kirste.userpage.fu-berlin.de/chemnet/use/info/make/make_4.html
