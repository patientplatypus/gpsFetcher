#!/bin/bash

echo removing previous assets folder
rm -rf ./assets
echo making new assets folder
mkdir assets
echo giving read/write access to folder
chmod 777 ./assets
echo now running python file
echo killing previous venv
rm -rf venv
echo spinning new venv in python3
virtualenv -p python3 venv
echo installing requirements from requirements.txt
pip3 install -r requirements.txt
echo activating venv
source venv/bin/activate
echo running main.py
python3 main.py