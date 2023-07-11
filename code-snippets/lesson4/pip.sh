#!/bin/bash
set -e

rm -rf myvenv
virtualenv -p python3 myvenv
sleep 5

printf "\nLets install some packages\n"
pip3 install flake8 pylint

printf "\nLets freeze our project packages\n"
pip3 list --format=freeze > requirements.txt

printf "\nInstall them in virtualenv created on previous step\n"

source myenv/bin/activate
pip3 install --upgrade -r requirements.txt
deactivate
rm -rf myvenv