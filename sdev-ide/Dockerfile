FROM ubuntu:latest

RUN apt-get update && apt-get -y upgrade

RUN apt-get update
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:ubuntu-elisp/ppa -y
RUN apt-get update &&  apt-get install emacs-snapshot -y
RUN apt-get install git -y
RUN apt-get install silversearcher-ag -y
RUN apt-get install curl -y

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

RUN apt-get update && apt-get install opam -y
RUN opam init
RUN opam install utop -y
RUN opam install tuareg -y
RUN opam install merlin -y
RUN opam user-setup install 

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install nodejs -y
RUN npm install -g bs-platform
RUN npm install npm --global
RUN apt-get update && apt-get install firefox -y

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


# RUN npm install -g https://github.com/reasonml/reason-cli/archive/beta-v-1.13.7-bin-linux.tar.gz

# ADD ./ mnt/NewEmacs

# RUN cp /mnt/NewEmacs/PragmataPro.ttf /usr/local/share/fonts

# RUN echo "export DISPLAY=172.22.215.129:0" >> /mnt/NewEmacs/sdev-emacs.sh

# RUN echo "emacs -q -l /mnt/NewEmacs/sdev-emacs.el &" >> /mnt/NewEmacs/sdev-emacs.sh

# curl https://sh.rustup.rs -sSf | sh
# docker build ./ -t sdev-emacs
# docker run -v //C/Users/andre/Desktop/SerialDev:/mnt/working_dir --net="host" -it sdev-emacs
