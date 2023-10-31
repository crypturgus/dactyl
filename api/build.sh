#!/bin/bash
set +x

pip install -r requirements.txt
python3 ./manage.py migrate
gunicorn app.wsgi:application --bind 0.0.0.0:8000
