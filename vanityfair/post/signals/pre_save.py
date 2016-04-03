from django.db.models.signals import pre_save
from django.dispatch import receiver

from post.models import Post


@receiver(pre_save, sender=Post)
def pre_save_post(sender, instance, *args, **kwargs):
    instance.source_id = instance.get_source_id()
