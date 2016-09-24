FROM debian:jessie

RUN apt-get -qq update && apt-get -qq -y install \
    build-essential \
    cmake \
    autotools-dev \
    automake \
    cmake \
    pkg-config \
    libpcre3 \
    libpcre3-dev \
    libpcre++-dev \
    doxygen \
    bison \
    apt-transport-https

# Get node
ADD nodesource.gpg.key /tmp/nodesource.gpg.key
ADD nodesource.list /etc/apt/sources.list.d/nodesource.list
RUN apt-key add /tmp/nodesource.gpg.key && apt-get -qq update && \
    apt-get -qq -y install nodejs python && \
    npm install -g node-gyp

# Get Swig
ADD swig /tmp/swig
RUN cd /tmp/swig && ./autogen.sh && ./configure && make && make install && cd -

# Housekeeping
RUN apt-get autoremove -qq -y \
    && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*