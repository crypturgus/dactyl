import strawberry

from user.schema import Mutation as UserMutation
from user.schema import Query as UserQuery


@strawberry.type
class RootQuery(UserQuery):
    pass


@strawberry.type
class RootMutation(UserMutation):
    pass


root_schema = strawberry.Schema(query=RootQuery, mutation=RootMutation)
