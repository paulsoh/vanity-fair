from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

from tag.models import Tag


class Post(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    """
    User input form
    """

    content = models.TextField()

    video_url = models.URLField(
        blank=True,
        null=True,
    )

    source_id = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )

    hash_id = models.CharField(
        max_length=8,
        blank=True,
        null=True,
        unique=True,
    )

    thumbnail = models.ImageField(
        blank=True,
        null=True,
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

    """
    Get video id from original source
    Currently only implemented for youtube
    """
    def get_source_id(self):
        import re
        reg_exp = "^.*(youtu\.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*"
        match = re.search(reg_exp, self.video_url)
        return match.group(2)

    def generate_hash_id(self):
        from vanityfair.utils import get_hash_id
        self.hash_id = get_hash_id(self)
        self.save()

    def get_content_by_word(self):
        temp = self.content.split()
        for word in temp:
            yield word

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "포스트"
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse(
            'post',
            kwargs={
                'pk': self.id,
            }
        )
