FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /root

RUN env
RUN apt-get update -y
RUN apt-get install -y \
            git \
            python3.7 \
            python3.7-distutils \
            python3-sphinx \
            curl \
            unzip \
            blender \
            pandoc \
            wget \
            zip

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python3.7 get-pip.py && \
    rm -f get-pip.py

RUN rm -f /usr/bin/python && ln -s /usr/bin/python3.7 /usr/bin/python
RUN rm -f /usr/bin/pip && ln -s /usr/local/bin/pip3.7 /usr/bin/pip

RUN pip install pathlib

RUN git clone https://git.blender.org/blender.git

RUN git clone https://github.com/nutti/fake-bpy-module.git
RUN pip install -r fake-bpy-module/requirements.txt
RUN bash fake-bpy-module/tools/utils/download_blender.sh all blender-bin
RUN rm -rf fake-bpy-module
