FROM python:3.8-bullseye

RUN apt-get update \
 && apt-get install --no-install-recommends -y \
    git \
    libglu1-mesa libegl1 libxxf86vm1 libxfixes3 libxi6 libxkbcommon0 libgl1 \
 && rm -rf /var/lib/apt/lists/*

COPY src/requirements.txt src/requirements.txt
RUN pip install --no-cache-dir -r src/requirements.txt
