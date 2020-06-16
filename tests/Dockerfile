FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /root

RUN env
RUN apt-get update -y
RUN apt-get install -y \
            git \
            python3.7 \
            python3-pip \
            python3-sphinx \
            curl \
            unzip \
            blender \
            pandoc \
            wget \
            zip

RUN python3.7 -m pip install pathlib wheel

RUN git clone https://git.blender.org/blender.git

RUN git clone https://github.com/nutti/fake-bpy-module.git
RUN python3.7 -m pip install -r fake-bpy-module/requirements.txt
RUN bash fake-bpy-module/tools/utils/download_blender.sh all blender-bin
RUN rm -rf fake-bpy-module

ENV PYTHON_BIN python3.7
