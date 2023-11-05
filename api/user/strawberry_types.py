import strawberry


@strawberry.type
class UserType:
    email: str


@strawberry.input
class RegisterUserInput:
    password: str
    email: str


@strawberry.type
class UserPayloadType:
    user: UserType
    errors: list[str]


@strawberry.input
class LoginUserInput:
    email: str
    password: str
