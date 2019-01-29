#!/bin/bash

. /appenv/bin/activate

# Time to install stuff with pip
pip3 download -d /build -r requirements/requirements.txt --no-input

pip3 install -d /build -r requirements/requirements.txt --no-input

exec $@
