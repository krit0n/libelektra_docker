# Node Binding for Elektra
## Set up a container for development
Initialize this repository.
```sh
$ git clone https://github.com/krit0n/libelektra_docker.git && cd libelektra_docker
$ git submodule init
$ git submodule update
```
Build the docker image and run it.
```sh
$ docker-compose build
$ docker-compose run elektra
```
Build and install libelektra inside the docker container
```sh
$ cd /root/build && cmake ../libelektra
$ make && make install
```

## Build the binding
The binding is inside ./node-kdb which is mapped to /node-kdb inside the container.
When inside the container build this binding with following commands:
```sh
$ cd /root/node-kdb
$ swig -c++ -javascript -node -I/usr/local/include kdb.i
$ node-gyp configure build
```

Now - again inside the container - you can run this binding from node
```sh
$ node
> var kdb = require('./build/Release/kdb')
> key = kdb.Key()
```

## TODO
Creating a key throws an error:
```
FATAL ERROR: v8::Object::SetAlignedPointerInInternalField() Internal field out of bounds
 1: node::Abort() [node]
 2: 0x10c913c [node]
 3: v8::Utils::ReportApiFailure(char const*, char const*) [node]
 4: 0x7f12d1fe35c6 [/node-kdb/build/Release/kdb.node]
 5: v8::internal::FunctionCallbackArguments::Call(void (*)(v8::FunctionCallbackInfo<v8::Value> const&)) [node]
 6: 0x9dfb88 [node]
 7: 0x9e04e6 [node]
 8: 0x21f9b14092a7
Aborted (core dumped)
```
