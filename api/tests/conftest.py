import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def user(db):  # The `db` fixture is provided by `pytest-django`.
    User = get_user_model()
    user = User.objects.create_user(email="testuser@testuser.xd", password="testpass")
    return user
