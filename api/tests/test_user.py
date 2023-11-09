import pytest
from django.contrib.auth import get_user_model
from django.test import Client

UserModel = get_user_model()


@pytest.mark.django_db
def test_some_query(user):
    client = Client()

    query = """
    query {
        users {
            email
        }
    }
    """

    response = client.post(
        "/graphql/v1/", {"query": query}, content_type="application/json"
    )

    assert response.status_code == 200
    json_response = response.json()
    assert json_response["data"]["users"][0]["email"] == "testuser@testuser.xd"


@pytest.mark.django_db
def test_register_user_returns_200():
    client = Client()

    query = """
    mutation {
    registerUser(input: { password: "xDpassword", email: "new@user.xd" }) {
        email
        }
    }
        """
    response = client.post(
        "/graphql/v1/", {"query": query}, content_type="application/json"
    )

    assert response.status_code == 200
    assert response.json()["data"]["registerUser"]["email"] == "new@user.xd"


@pytest.mark.django_db
def test_register_user_creates_active_user():
    client = Client()

    query = """
    mutation {
    registerUser(input: { password: "xDpassword", email: "new@user.xd" }) {
        email
    }
}
        """
    client.post("/graphql/v1/", {"query": query}, content_type="application/json")

    user = UserModel.objects.get(email="new@user.xd")
    assert user.is_active is True
    assert user.check_password("xDpassword") is True


@pytest.mark.django_db
def test_login_user_returns_200(user):
    client = Client()

    query = """
    mutation {
    loginUser(input: { email: "testuser@testuser.xd", password: "testpass" }) {
        email
        }
    }
    """
    response = client.post(
        "/graphql/v1/", {"query": query}, content_type="application/json"
    )

    assert response.status_code == 200
    assert response.json()["data"]["loginUser"]["email"] == "testuser@testuser.xd"
    token = response.headers["Authorization"].split(" ")[1]
    user = UserModel.objects.get(
        tokens__token=token, tokens__sid=response.cookies["SuperSID"].value
    )
    assert user.email == "testuser@testuser.xd"
