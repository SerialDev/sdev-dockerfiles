FROM python:3.5

ENV HOME /root
ENV PYTHONPATH "/usr/lib/python3/dist-packages:/usr/local/lib/python3.5/site-packages"

# Install dependencies
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get autoremove -y \
    && apt-get install -y \
        gcc \
        build-essential \
        zlib1g-dev \
        wget \
        unzip \
        cmake \
        python3-dev \
        gfortran \
        libblas-dev \
        liblapack-dev \
        libatlas-base-dev \
    && apt-get clean

# Install Python packages
RUN pip install --upgrade pip \
    && pip install \
        ipython[all] \
        numpy \
        nose \
        matplotlib \
        pandas \
        scipy \
        sympy \
        cython \
    && rm -fr /root/.cache

RUN apt-get update
RUN apt-get install libpq-dev -y
RUN apt-get install screen
RUN pip3 install --upgrade pip
RUN pip3 install setuptools --upgrade
RUN pip3 install cython --upgrade
RUN pip3 install pandas --upgrade
RUN apt-get install build-essential python-dev libapache2-mod-wsgi-py3 libmysqlclient-dev -y
RUN pip3 install mysqlclient
RUN pip3 install fastavro
RUN pip3 install requests
RUN pip3 install sklearn

WORKDIR /root
RUN git clone https://github.com/edenhill/librdkafka.git
WORKDIR /root/librdkafka
RUN /root/librdkafka/configure
RUN make
RUN make install
RUN pip3 install confluent-kafka
RUN pip3 install pykafka



ENTRYPOINT ["/bin/bash"]


