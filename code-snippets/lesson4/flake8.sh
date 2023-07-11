#!/bin/bash
set -e

rm -rf myvenv
virtualenv -p python3 myvenv
sleep 5

#install flake8 and pylint
source myenv/bin/activate
pip3 install flake8 pylint
python3 -m flake8 ../lesson3/example1.py

python3 -m pylint ../lesson3/example1.py

deactivate