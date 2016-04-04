import os
import requests

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from post.models import Post


@receiver(pre_save, sender=Post)
def pre_save_post(sender, instance, *args, **kwargs):
    instance.source_id = instance.get_source_id()


@receiver(pre_save, sender=Post)
def pre_save_get_thumbnail_image(sender, instance, *args, **kwargs):
    if not instance.coverimage:
        image_url = instance.get_source_id()
        image_src = "https://img.youtube.com/vi/{image_url}/maxresdefault.jpg".format(
            image_url=image_url,
        )

        r = requests.get(image_src)
        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(r.content)
        img_temp.flush()
        instance.coverimage.save(image_src, File(img_temp), save=False)
