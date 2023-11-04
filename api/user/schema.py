from typing import List

import strawberry
from django.contrib.auth import get_user_model

from user.services import register_user_service
from user.strawberry_types import RegisterUserInput, RegisterUserPayload, User

UserModel = get_user_model()


@strawberry.type
class Query:
    @strawberry.field
    def users(self, info) -> List[User]:
        return UserModel.objects.all()


@strawberry.type
class Mutation:
    @strawberry.mutation
    def register_user(self, info, input: RegisterUserInput) -> RegisterUserPayload:
        return register_user_service(input)
