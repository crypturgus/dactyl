#!/bin/bash
set +x

# 1. Install dependencies
poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi


# 2. Apply Django migrations
echo "Apply database migrations"
python3 manage.py migrate
#
## 3. Create Django superuser
#echo "Create Django superuser"
#echo "
#import os
#from django.contrib.auth import get_user_model
#from django.db.utils import IntegrityError
#
#User = get_user_model()
#
#username = os.environ['DJANGO_SUPERUSER_USERNAME']
#email = os.environ['DJANGO_SUPERUSER_EMAIL']
#password = os.environ['DJANGO_SUPERUSER_PASSWORD']
#
#try:
#    User.objects.create_superuser(email, password)
#    print('Superuser created.')
#except IntegrityError:
#    print('Superuser already exists.')
#" | python manage.py shell
