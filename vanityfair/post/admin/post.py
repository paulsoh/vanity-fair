from django.contrib import admin

from post.models import Post


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):

    list_display = admin.ModelAdmin.list_display + (
        'user',

        'title',
        'content',

        'created_at',
        'updated_at',
    )
