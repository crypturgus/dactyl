#!/bin/bash
set +x

## 1. Install dependencies
pip install poetry==1.6.1
poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# 2. Apply Django migrations
#echo "Apply database migrations"
python3 manage.py migrate

## 3. Create Django superuser
python3 manage.py createadmin
