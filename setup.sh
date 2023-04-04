#!/usr/bin/env bash

apt-get install -y python3 python3-pip python3-dev

pip3 install -r /autograder/source/requirements.txt
pip3 install testbook
pip3 install gradescope_utils
python3 -m pip install ipykernel
python3 -m ipykernel install --user
