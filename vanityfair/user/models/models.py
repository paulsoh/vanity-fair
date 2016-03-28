from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    profile_image = models.ImageField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = "User info"
        verbose_name_plural = verbose_name
