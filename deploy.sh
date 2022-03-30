#!/bin/bash

test -d venv || python3.10 -m virtualenv venv
rm -rfd dist

source venv/bin/activate
python -m pip install -U pip
python -m pip install -r requirements.txt
python -m pip install -U build twine

python -m build
if [ $? -ne 0 ]; then
    echo "Error on build !"
    exit 1
fi

python -m twine check dist/*
if [ $? -ne 0 ]; then
    echo "Error on check !"
    exit 1
fi

python3 -m twine upload --repository pypi -u QuentinN42 dist/*
if [ $? -ne 0 ]; then
    echo "Error push !"
    exit 1
fi
