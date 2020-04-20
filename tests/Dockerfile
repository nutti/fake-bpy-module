FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /root

RUN env
RUN apt-get update -y
RUN apt-get install -y \
            git \
            python3 \
            python3-pip \
            python3-sphinx \
            curl \
            unzip \
            blender \
            pandoc \
            zip

RUN rm -f /usr/bin/python && ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip

RUN pip install pathlib

RUN git clone https://git.blender.org/blender.git

RUN git clone https://github.com/nutti/fake-bpy-module.git
RUN pip install -r fake-bpy-module/requirements.txt
RUN bash fake-bpy-module/tools/utils/download_blender.sh all blender-bin
RUN rm -rf fake-bpy-module
