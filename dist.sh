#!/usr/bin/env bash

python3 ./setup.py bdist_wheel upload
python ./setup.py bdist_wheel upload