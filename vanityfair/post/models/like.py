from django.db import models
from django.conf import settings


class Like(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )

    post = models.ForeignKey(
        'Post',
    )

    LIKED = 'LI'
    DISLIKED = 'DL'
    WATCHED = 'WA'
    POST_REACTION = (
        (LIKED, 'Liked'),
        (DISLIKED, 'Disliked'),
        (WATCHED, 'Watched'),
    )

    reaction = models.CharField(
        max_length=2,
        choices=POST_REACTION,
        default=WATCHED,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )
