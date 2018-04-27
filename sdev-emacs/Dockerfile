FROM ubuntu:xenial

# common packages
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    ca-certificates curl file \
    build-essential \
    autoconf automake autotools-dev libtool xutils-dev && \
    rm -rf /var/lib/apt/lists/*  && \
    apt-get update && apt-get -y upgrade && \
    apt-get install software-properties-common -y && \
    apt-get install git -y && \
    apt-get install silversearcher-ag -y && \
    apt-get install curl -y && \
    add-apt-repository ppa:ubuntu-elisp/ppa -y && \
    apt-get update && \
    apt-get install emacs-snapshot -y && \
    apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion && \
    apt-get update && apt-get install -y \
    automake \
    build-essential \
    curl \
    libgif-dev \
    libgnutls-dev \
    libgtk-3-dev \
    libjpeg-dev \
    libncurses5-dev \
    libtiff-dev \
    libxml2-dev \
    libxpm-dev \
    texinfo && \
    apt-get install ninja -y && \
    apt-get install libclang-dev -y && \
    apt-get install pkg-config -y && \
    apt-get install clang -y && \
    apt-get install cmake -y


RUN curl -fsSL https://raw.githubusercontent.com/cask/cask/master/go | python && \
    export PATH="/root/.cask/bin:$PATH"
