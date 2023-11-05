from datetime import timedelta

import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from strawberry.types import Info

from user.models import RefreshToken

UserModel = get_user_model()


def create_token(expiry_minutes: int, user_id: int) -> str:
    expiration_date = timezone.now() + timedelta(minutes=expiry_minutes)
    token = jwt.encode(
        {"user_id": user_id, "exp": expiration_date},
        settings.SECRET_KEY,
        algorithm="HS256",
    )
    return token


def create_tokens(user: UserModel) -> tuple[str, str]:
    jwt_token = create_token(settings.ACCESS_TOKEN_EXPIRY_MINUTES, user.id)
    refresh_token = create_token(settings.REFRESH_TOKEN_EXPIRY_MINUTES, user.id)
    RefreshToken.objects.create(user=user, token=refresh_token)
    return jwt_token, refresh_token


def get_decoded_token(info: Info, token_name) -> dict:
    try:
        token = info.context.request.COOKIES.get(token_name)
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    except Exception as e:
        raise e
    return decoded_token
