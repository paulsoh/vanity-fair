from django.db.models.signals import post_save
from django.dispatch import receiver

from post.models import Post
from tag.models import Tag


@receiver(post_save, sender=Post)
def post_save_post(sender, instance, created, **kwargs):
    if not instance.hash_id:
        instance.generate_hash_id()

    tags = getattr(instance, '_tags', None)
    for tag in tags:
        tag_name, created = Tag.objects.get_or_create(name=tag)
        instance.tag_set.add(tag_name)
