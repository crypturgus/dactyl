#!/bin/bash
set +x

pip install -r requirements.txt
python3 ./manage.py migrate
