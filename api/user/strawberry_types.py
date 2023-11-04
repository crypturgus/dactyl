import strawberry


@strawberry.type
class User:
    email: str


@strawberry.input
class RegisterUserInput:
    username: str
    password: str
    email: str


@strawberry.type
class RegisterUserPayload:
    user: User
    errors: list[str]
