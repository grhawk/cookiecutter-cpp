FROM debian:bookworm-slim
LABEL maintainer="Riccardo Petraglia" \
      description="Cookiecutter-cpp stuff for CircleCi repo." \
      version="0.1.1"
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Zurich
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get dist-upgrade -y && \
    apt-get install -y --no-install-recommends\
    tzdata \
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
RUN pip3 install -r /tmp/requirements_dev.txt --break-system-packages
RUN conan profile detect --force

