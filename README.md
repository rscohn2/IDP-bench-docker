# IDP-bench-docker
Dockerfile to make an image for a containers used to benchmark python for [Intel Distribution for python](https://software.intel.com/en-us/intel-distribution-for-python)

Start a docker container for python with numpy/scipy & openblas installed with apt:

    docker run -i -t rscohn2/idpbench.sys_openblas.ubuntu python

## Images

There are several ways to install python and packages. You can use the system installer (e.g. apt-get on ubunutu), pip, or conda. We generate docker containers for the common methods.

rscohn2/idpbench.sys_{openblas,atlas,reference}.ubuntu: Install all the python components with apt-get. This will use the system BLAS/LAPACK implementations. The default is reference, and the script also generates images where openblas and atlas are used. Note that you are using the OS provided build of BLAS/LAPACK, which is configured to run on a wide variety of systems and will not perform well if you have modern hardware.

rscohn2/idpbench.pip.ubuntu: Install python with apt-get, and then use pip to upgrade pip and install numpy/scipy. This will use the blas and lapack that come in the wheels. This is configured to use AVX2 and will perform better than the OS provided BLAS/LAPACK, but will not take advantage of newer hardware.

## How to build the images

To build and publish all images do:

   python build.py --publish

You can use command line arguments to build a subset. To see the help:

   python build.py --help

## How the docker images are built

build.py generates Dockerfiles for each of the variants, using jinja2 to
subtitute the info specific to the image. Dockerfile.tpl is the jinja2
template. The docker layers are structured to share as much as possible between
images so downloads are smaller.

## Publishing images

Images are built on https://travis-ci.org/rscohn2/IDP-bench-docker and
published to https://hub.docker.com/r/rscohn2/

[![Build Status](https://travis-ci.org/rscohn2/IDP-bench-docker.svg?branch=master)](https://travis-ci.org/rscohn2/IDP-bench-docker)

