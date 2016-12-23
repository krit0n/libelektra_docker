FROM ubuntu:xenial

RUN apt-get -qq update && apt-get -qq -y install \
    build-essential \
    valgrind \
    autotools-dev \
    automake \
    cmake \
    cmake-data \
    cmake-curses-gui \
    pkg-config \
    libpcre3 \
    libpcre3-dev \
    libpcre++-dev \
    doxygen \
    bison \
    apt-transport-https

# Get node
#RUN apt-get -qq -y install nodejs nodejs-dev
ADD nodesource.gpg.key /tmp/nodesource.gpg.key
ADD nodesource.list /etc/apt/sources.list.d/nodesource.list
RUN apt-key add /tmp/nodesource.gpg.key && apt-get -qq update && \
    apt-get -qq -y install nodejs python && \
    npm install -g node-gyp

# Get Swig
ADD https://codeload.github.com/swig/swig/tar.gz/rel-3.0.10 /tmp/swig.tar.gz
RUN cd /tmp && tar xzf swig.tar.gz && cd swig-rel-3.0.10 && ./autogen.sh && ./configure && make && make install

# Housekeeping
RUN apt-get autoremove -qq -y \
    && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*

ENV LD_LIBRARY_PATH /usr/local/lib
