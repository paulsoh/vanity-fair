from django.db import models
from django.conf import settings

from tag.models import Tag


class Post(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
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

    tag_set = models.ManyToManyField(
        Tag,
        blank=True,
        null=True,
    )

    like_user_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_post_set',
        through='Like',
    )

    def generate_hash_id(self):
        from vanityfair.utils import get_hash_id
        self.hash_id = get_hash_id(self)
        self.save()

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "포스트"
        verbose_name_plural = verbose_name
