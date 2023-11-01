from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from services.notification_service import NotificationService
from user.strawberry_models import RegisterUserInput, RegisterUserPayload

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
    else:
        if settings.SEND_NOTIFICATIONS:
            NotificationService().send_register_notification(user)
    return RegisterUserPayload(user=user, errors=errors)
