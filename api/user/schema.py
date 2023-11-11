from typing import Any, List

import strawberry
from django.contrib.auth import get_user_model
from strawberry import BasePermission
from strawberry.types import Info

from app.exceptions import (
    NotAuthenticatedError,
    SomethingWentWrongError,
    UserNotFoundError,
)
from user.data_models import LoginUserDataModel
from user.services import login_user_service, register_user_service
from user.strawberry_types import (
    LoggedUserType,
    LoginUserInput,
    RegisterUserInput,
    UserType,
)
from user.utils import validate_and_decode_token

UserModel = get_user_model()


class IsAuthenticated(BasePermission):
    message = "User is not authenticated"

    def has_permission(self, source: Any, info: Info, **kwargs) -> bool:
        sid = info.context.request.COOKIES.get("SuperSID")
        token = self._extract_token(info.context.request.headers.get("Authorization"))
        validate_and_decode_token(token)
        try:
            user = UserModel.objects.get(tokens__sid=sid, tokens__token=token)
        except UserModel.DoesNotExist:
            return False
        else:
            info.context.user = user
        return bool(token)

    def _extract_token(self, auth_header: str) -> str:
        parts = auth_header.split(" ")
        if len(parts) == 2 and parts[0] == "Bearer":
            return parts[1]


def get_users() -> List[UserType]:
    return UserModel.objects.all()


@strawberry.type
class Query:
    @strawberry.field
    def users(self, info: Info) -> List[UserType]:
        return get_users()

    @strawberry.field(permission_classes=[IsAuthenticated])
    def user(self, info: Info) -> UserType:
        return info.context.user.to_strawberry(UserType)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def register_user(self, info: Info, input: RegisterUserInput) -> UserType:
        login_data = LoginUserDataModel(email=input.email, password=input.password)
        try:
            user = register_user_service(login_data)
        except Exception:
            raise SomethingWentWrongError()
        return user.to_strawberry(UserType)

    @strawberry.mutation
    def login_user(self, info: Info, input: LoginUserInput) -> LoggedUserType:
        login_data = LoginUserDataModel(email=input.email, password=input.password)
        try:
            data = login_user_service(info, login_data)
        except (NotAuthenticatedError, UserNotFoundError):
            raise SomethingWentWrongError()
        return LoggedUserType(user=data.user.to_strawberry(UserType), token=data.token)
