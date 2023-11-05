from typing import Any, List

import strawberry
from django.contrib.auth import get_user_model
from strawberry import BasePermission
from strawberry.types import Info

from app.exceptions import UserNotFoundError
from user.data_models import LoginUserDataModel
from user.services import (
    get_user_service,
    login_user_service,
    refersh_token_service,
    register_user_service,
)
from user.strawberry_types import LoginUserInput, RegisterUserInput, UserType
from user.utils import get_decoded_token

UserModel = get_user_model()


class IsAuthenticated(BasePermission):
    message = "User is not authenticated"

    def has_permission(self, source: Any, info: Info, **kwargs) -> bool:
        token = get_decoded_token(info, "accessToken")
        return bool(token)


def get_users() -> List[UserType]:
    return UserModel.objects.all()


@strawberry.type
class Query:
    @strawberry.field
    def users(self, info: Info) -> List[UserType]:
        return get_users()

    @strawberry.field(permission_classes=[IsAuthenticated])
    def user(self, info: Info) -> UserType:
        decoded_token = get_decoded_token(info, "accessToken")

        try:
            data = get_user_service(decoded_token["user_id"])
        except UserNotFoundError:
            raise Exception("User not found")
        return data.to_strawberry(UserType)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def register_user(self, info: Info, input: RegisterUserInput) -> UserType:
        login_data = LoginUserDataModel(email=input.email, password=input.password)
        user = register_user_service(login_data)
        return user.to_strawberry(UserType)

    @strawberry.mutation
    def login_user(self, info: Info, input: LoginUserInput) -> UserType:
        login_data = LoginUserDataModel(email=input.email, password=input.password)
        user = login_user_service(info, login_data)
        return user.to_strawberry(UserType)
    @strawberry.mutation
    def refresh_token(self, info: Info) -> UserType:
        user = refersh_token_service(info)
        return user.to_strawberry(UserType)
