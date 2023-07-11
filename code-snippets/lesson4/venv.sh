#!/bin/bash
set -e

rm -rf myvenv
printf "Default python3 executable\n"
which python3

printf "\nLets create venv\n"
python3 -m venv myenv
sleep 5
source myenv/bin/activate

printf "\nvenv python3 executable\n"
which python3
deactivate
rm -rf myvenv

