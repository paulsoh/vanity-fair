from django.db import models

from user.models import User
from post.models import Post


class Comment(models.Model):

    user = models.ForeignKey(
        User,
    )

    post = models.ForeignKey(
        'Post',
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = verbose_name
