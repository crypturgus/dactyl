from datetime import timedelta
from uuid import UUID, uuid4

import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone

from user.models import AccessToken

UserModel = get_user_model()


def create_token(expiry_days: int, user_id: int) -> str:
    expiration_date = timezone.now() + timedelta(days=expiry_days)
    token = jwt.encode(
        {"user_id": user_id, "exp": expiration_date},
        settings.SECRET_KEY,
        algorithm="HS256",
    )
    return token


def create_tokens(user: UserModel) -> tuple[str, UUID]:
    jwt_token = create_token(settings.ACCESS_TOKEN_EXPIRY_DAYS, user.id)
    sid = uuid4()
    AccessToken.objects.create(user=user, token=jwt_token, sid=sid)
    return jwt_token, sid


def validate_and_decode_token(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    except Exception as e:
        raise e
    return decoded_token
