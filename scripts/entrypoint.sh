#!/bin/bash

# 1. Wait for the database to be ready
/tmp/wait-for-it.sh $POSTGRES_HOST:$POSTGRES_PORT --timeout=5 -- echo "Database is up"


# 2. Apply Django migrations
echo "Apply database migrations"
python manage.py migrate

# 3. Create Django superuser
python manage.py createadmin

# 4. Run Django development server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000
