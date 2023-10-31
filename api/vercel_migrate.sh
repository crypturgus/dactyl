#!/bin/bash
set +x
#pip install poetry
## 1. Install dependencies
#poetry config virtualenvs.create false \
#  && poetry install --no-interaction --no-ansi
pip install --upgrade pip
pip install -r requirements.txt
pip install gunicorn
pip install uvicorn

# 2. Apply Django migrations
echo "Apply database migrations"
python3 manage.py migrate

## 3. Create Django superuser
python3 manage.py createadmin
