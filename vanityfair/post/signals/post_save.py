from django.db.models.signals import post_save
from django.dispatch import receiver

from post.models import Post


@receiver(post_save, sender=Post)
def post_save_post(sender, instance, created, **kwargs):
    if not instance.hash_id:
        instance.generate_hash_id()
