from typing import List

import strawberry
from django.contrib.auth import get_user_model

UserModel = get_user_model()

@strawberry.type
class User:
    email: str


@strawberry.type
class Query:
    @strawberry.field
    def users(self, info) -> List[User]:
        return UserModel.objects.all()


user_schema = strawberry.Schema(query=Query)
