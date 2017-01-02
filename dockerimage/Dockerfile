FROM ubuntu:xenial

RUN apt-get -qq update && apt-get -qq -y install \
    apt-transport-https \
    build-essential \
    valgrind \
    autotools-dev \
    automake \
    cmake \
    cmake-data \
    cmake-curses-gui \
    pkg-config \
    libpcre3-dev \
    libpcre++-dev \
    doxygen \
    graphviz \
    bison \
    ruby-dev \
    python-dev \
    liblua5.3-dev \
    tclcl-dev \
    libaugeas-dev \
    libyajl-dev \
    libgit2-dev \
    libboost-all-dev \
    libssl-dev \
    libdbus-1-dev \
    && gem install ronn

# Get node
#RUN apt-get -qq -y install nodejs nodejs-dev
ADD nodesource.gpg.key /tmp/nodesource.gpg.key
ADD nodesource.list /etc/apt/sources.list.d/nodesource.list
RUN apt-key add /tmp/nodesource.gpg.key && apt-get -qq update && \
    apt-get -qq -y install nodejs python && \
    npm install -g node-gyp

# Get Swig
ADD https://codeload.github.com/swig/swig/tar.gz/rel-3.0.11 /root/swig.tar.gz
RUN cd && tar xzf swig.tar.gz && cd swig-rel-3.0.11 && ./autogen.sh && ./configure && make && make install

# Housekeeping
RUN apt-get autoremove -qq -y \
    && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*
