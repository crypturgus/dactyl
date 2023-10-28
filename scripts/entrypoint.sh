#!/bin/bash

# 1. Wait for the database to be ready
/tmp/wait-for-it.sh $POSTGRES_HOST:$POSTGRES_PORT --timeout=60 -- echo "Database is up"

#until nc -z $POSTGRES_HOST $POSTGRES_PORT; do
#    echo "$(date) - waiting for database to start"
#    sleep 1
#done

# 2. Apply Django migrations
echo "Apply database migrations"
python manage.py migrate

# 3. Create Django superuser
echo "Create Django superuser"
echo "
import os
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

User = get_user_model()

username = os.environ['DJANGO_SUPERUSER_USERNAME']
email = os.environ['DJANGO_SUPERUSER_EMAIL']
password = os.environ['DJANGO_SUPERUSER_PASSWORD']

try:
    User.objects.create_superuser(email, password)
    print('Superuser created.')
except IntegrityError:
    print('Superuser already exists.')
" | python manage.py shell

# 4. Run Django development server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000
