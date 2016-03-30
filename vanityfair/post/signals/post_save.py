from django.db.models.signals import post_save
from django.dispatch import receiver

from post.models import Post
from tag.models import Tag


@receiver(post_save, sender=Post)
def post_save_post(sender, instance, created, **kwargs):
    if not instance.hash_id:
        instance.generate_hash_id()


@receiver(post_save, sender=Post)
def post_save_tags(sender, instance, created, **kwargs):
    tag_list = [
        tag[1::] for tag
        in instance.content.split()
        if tag.startswith("#")
    ]

    for tag_name in tag_list:
        tag_object, is_tag_created = Tag.objects.get_or_create(name=tag_name)
        instance.tag_set.add(tag_object)
