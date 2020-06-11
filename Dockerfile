FROM ubuntu:18.04
ENV PYTHONUNBUFFERED TRUE

## Basic installation of jdk, git, python, curl ....
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
    fakeroot \
    ca-certificates \
    dpkg-dev \
    g++ \
    python3-dev \
    curl \
    vim \
    && rm -rf /var/lib/apt/lists/* \
    && cd /tmp \
    && curl -O https://bootstrap.pypa.io/get-pip.py \
    && python3 get-pip.py
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1
RUN update-alternatives --install /usr/local/bin/pip pip /usr/local/bin/pip3 1

## Flask utils
RUN pip install Flask flask-restplus Flask-SSLify Flask-Admin gunicorn hdfs

## Preparing expose and configuration for users
USER root
COPY / /
WORKDIR /

EXPOSE 8078

CMD ["gunicorn", "-b", "0.0.0.0:8078", "ts_viz"]
