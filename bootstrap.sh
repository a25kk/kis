#!/bin/sh
virtualenv -p python3 --clear .
env LDFLAGS="-L$(brew --prefix openssl)/lib" CFLAGS="-I$(brew --prefix openssl)/include" ./bin/pip install cryptography
./bin/pip3 install -r requirements.txt
./bin/buildout -c development.cfg