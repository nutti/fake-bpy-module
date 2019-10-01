FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /root

RUN env
RUN apt-get update -y
RUN apt-get install -y \
            git \
            python3 \
            python3-pip \
            python-sphinx \
            curl \
            unzip \
            blender \
            pandoc \
            zip

RUN pip3 install pathlib

RUN git clone https://git.blender.org/blender.git

RUN git clone https://github.com/nutti/fake-bpy-module.git
RUN pip3 install -r fake-bpy-module/requirements.txt
RUN bash fake-bpy-module/tools/utils/download_blender.sh all blender-bin
RUN rm -rf fake-bpy-module
