import os

from app.settings import *  # noqa: F403,F401

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("TEST_POSTGRES_DB"),
        "USER": os.environ.get("TEST_POSTGRES_USER"),
        "PASSWORD": os.environ.get("TEST_POSTGRES_PASSWORD"),
        "HOST": os.environ.get("TEST_POSTGRES_HOST"),
        "PORT": os.environ.get("TEST_POSTGRES_PORT"),
    }
}
