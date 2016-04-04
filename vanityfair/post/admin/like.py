from django.contrib import admin

from post.models import Like


@admin.register(Like)
class LikeModelAdmin(admin.ModelAdmin):

    list_display = admin.ModelAdmin.list_display + (
        'user',
        'post',
        'reaction',

        'created_at',
        'updated_at',
    )
