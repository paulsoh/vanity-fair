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

    hash_id = models.CharField(
        max_length=8,
        blank=True,
        null=True,
        unique=True,
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def generate_hash_id(self):
        from vanityfair.utils import get_hash_id
        self.hash_id = get_hash_id(self)
        self.save()

    class Meta:
        verbose_name = "포스트"
        verbose_name_plural = verbose_name
