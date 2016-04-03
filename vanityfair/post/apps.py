from django.apps import AppConfig


class PostAppConfig(AppConfig):

    name = "post"

    def ready(self):
        from post.signals import post_save, pre_save
