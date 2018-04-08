# FROM phusion/baseimage:latest
FROM ubuntu:xenial

RUN apt-get update && apt-get -y upgrade && \
    apt-get install software-properties-common -y && \
    apt-get install git -y && \
    apt-get install silversearcher-ag -y && \
    apt-get install curl -y

RUN add-apt-repository ppa:ubuntu-elisp/ppa -y && \
    apt-get update && \
    apt-get install emacs-snapshot -y

# common packages
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    ca-certificates curl file \
    build-essential \
    autoconf automake autotools-dev libtool xutils-dev && \
    rm -rf /var/lib/apt/lists/* 

# install rustup toolchain
RUN curl https://sh.rustup.rs -sSf | \
    sh -s -- --default-toolchain nightly -y

ENV RUSTUP_HOME=/rust
ENV CARGO_HOME=/cargo 
ENV PATH=/cargo/bin:/rust/bin:$PATH

RUN echo "(curl https://sh.rustup.rs -sSf | sh -s -- -y --default-toolchain nightly --no-modify-path) && rustup default nightly" > /install-rust.sh && chmod 755 /install-rust.sh

RUN bash install-rust.sh

RUN rustup component add rust-src
RUN cargo install racer

RUN apt-get update && apt-get install opam -y && \
    opam init && \
    opam install utop -y && \
    opam install tuareg -y && \
    opam install merlin -y && \
    opam user-setup install  

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \
    apt-get install nodejs -y && \
    npm install -g bs-platform && \
    npm install npm --global && \
    apt-get update && apt-get install firefox -y

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh


RUN apt-get install -y curl grep sed dpkg && \
    TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb && \
    apt-get clean

ENV PATH /opt/conda/bin:$PATH

RUN conda update -n base conda && \
    conda install pytorch -c pytorch && \
    conda install virtualenv
    
RUN conda install torchvision && \
    conda install jupyter &&  \
    conda install pip

RUN apt-get install ninja -y && \
    apt-get install libclang-dev -y && \
    apt-get install pkg-config -y && \
    apt-get install clang -y && \
    apt-get install cmake -y

RUN pip install meson

RUN git clone --recursive https://github.com/Andersbakken/rtags.git && \
    cd rtags && cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=1 . && make && \
    export PATH=$PATH:/mnt/rtags/bin

RUN apt-get update && apt-get install -y \
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
    texinfo

# # docker run -v //C/Users/andre/Desktop/SerialDev:/mnt/working_dir --net="host" -it sdev-emacs