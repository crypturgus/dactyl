#!/bin/bash
set +x

## 1. Install dependencies
pip install -r requirements.txt

# 2. Apply Django migrations
#echo "Apply database migrations"
python3 manage.py migrate

## 3. Create Django superuser
python3 manage.py createadmin
