from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

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

    def get_tags_by_word(self):
        tag_list = []
        for tags in self.tag_set.values_list():
            tag_id, tag_name = tags
            tag_list.append("#"+tag_name)
        return tag_list

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
