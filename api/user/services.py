from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ValidationError
from strawberry.types import Info

from app.exceptions import UserNotFoundError
from user.data_models import LoginUserDataModel, UserDataModel
from user.utils import create_tokens, get_decoded_token

UserModel = get_user_model()


def register_user_service(input: LoginUserDataModel) -> UserDataModel:
    user = None
    try:
        user = UserModel.objects.create_user(
            password=input.password,
            email=input.email,
            is_active=True,
        )
    except ValidationError as e:
        Exception(e)  # TOOD: handle this exception

    return UserDataModel.model_validate(user)


def login_user_service(info: Info, login_data: LoginUserDataModel) -> UserDataModel:
    errors = []
    user = authenticate(email=login_data.email, password=login_data.password)
    if user:
        jwt_token, refresh_token = create_tokens(user)
        response = info.context["response"]
        response.set_cookie(
            key="accessToken",
            value=jwt_token,
            httponly=True,
            secure=False,  # Set to False if not using HTTPS
            samesite="Strict",
        )
        response.set_cookie(
            key="refreshToken",
            value=refresh_token,
            httponly=True,
            secure=False,  # Set to False if not using HTTPS
            samesite="Strict",
        )
        return UserDataModel.model_validate(user)
    errors.extend(["Invalid email or password"])
    raise Exception("Authentication failed")


def refersh_token_service(info: Info):
    token_payload = get_decoded_token(info, "refreshToken")
    user_id = token_payload["user_id"]
    try:
        logged_user = UserModel.objects.get(id=user_id)
    except UserModel.DoesNotExist:
        raise UserNotFoundError()
    jwt_token, refresh_token = create_tokens(logged_user)
    response = info.context["response"]
    response.set_cookie(
        key="accessToken",
        value=jwt_token,
        httponly=True,
        secure=False,  # Set to False if not using HTTPS
        samesite="Strict",
    )
    response.set_cookie(
        key="refreshToken",
        value=refresh_token,
        httponly=True,
        secure=False,  # Set to False if not using HTTPS
        samesite="Strict",
    )
    return UserDataModel.model_validate(logged_user)


def get_user_service(user_id: int) -> UserDataModel:
    try:
        logged_user = UserModel.objects.get(id=user_id)
    except UserModel.DoesNotExist:
        raise UserNotFoundError()
    return UserDataModel.model_validate(logged_user)
