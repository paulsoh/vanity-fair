from django.db import models

from user.models import User


class Post(models.Model):

    user = models.ForeignKey(
        User,
    )

    image = models.ImageField(
        blank=True,
        null=True,
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = "포스트"
        verbose_name_plural = verbose_name
