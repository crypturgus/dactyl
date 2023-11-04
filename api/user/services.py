from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from user.strawberry_types import RegisterUserInput, RegisterUserPayload

UserModel = get_user_model()


def register_user_service(input: RegisterUserInput) -> RegisterUserPayload:
    errors = []
    user = None
    try:
        user = UserModel.objects.create_user(
            password=input.password,
            email=input.email,
            is_active=True,
        )
    except ValidationError as e:
        errors.extend(e.messages)

    return RegisterUserPayload(user=user, errors=errors)
