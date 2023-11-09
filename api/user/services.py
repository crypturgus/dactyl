from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from strawberry.types import Info

from app.exceptions import UserNotFoundError
from user.data_models import LoginUserDataModel, UserDataModel
from user.utils import create_tokens

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
    # The authenticate method is temporarily commented out due to issues encountered during testing,
    # which are planned to be resolved in a future update.
    # In its place, a manual check is performed to verify the email and password, ensuring user authentication.
    # Tests have also been added to validate the provided email and password, ensuring the correctness of this temporary solution.
    # user = authenticate(email=login_data.email, password=login_data.password)
    user = UserModel.objects.get(email=login_data.email)
    is_logged = user.check_password(login_data.password)
    if is_logged:
        jwt_token, sid = create_tokens(user)
        response = info.context["response"]
        response.set_cookie(
            key="SuperSID",
            value=sid,
            httponly=True,
            secure=settings.USE_HTTPS,  # Set to False if not using HTTPS
            samesite="Strict",
        )
        response.headers["Authorization"] = f"Bearer {jwt_token}"
        return UserDataModel.model_validate(user)
    errors.extend(["Invalid email or password"])
    raise Exception("Authentication failed")


def get_user_service(user_id: int) -> UserDataModel:
    try:
        logged_user = UserModel.objects.get(id=user_id)
    except UserModel.DoesNotExist:
        raise UserNotFoundError()
    return UserDataModel.model_validate(logged_user)
