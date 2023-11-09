from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from app.models import DjangoModelMixin
from user.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, DjangoModelMixin):
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    display_name = models.CharField(max_length=128, blank=True, default="")

    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return self.email


class AccessToken(models.Model):
    sid = models.UUIDField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tokens")
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
