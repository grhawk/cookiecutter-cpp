FROM ubuntu:focal
LABEL maintainer="Riccardo Petraglia" \
      description="Cookiecutter-cpp stuff for CircleCi repo." \
      version="0.1.0"
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Zurich
RUN apt-get update -y && \
    apt-get install -y tzdata
RUN apt-get install -y --no-install-recommends\
                    git \
                    g++ \
                    build-essential \
                    cmake \
                    python3 \
                    python3-pip \
                    ca-certificates && \
    apt-get autoclean && \
    apt-get autoremove && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
COPY requirements_dev.txt /tmp
RUN pip3 install -r /tmp/requirements_dev.txt
RUN conan profile detect --force

