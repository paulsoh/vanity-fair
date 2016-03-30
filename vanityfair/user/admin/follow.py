from django.contrib import admin

from user.models import Follow


@admin.register(Follow)
class FollowModelAdmin(admin.ModelAdmin):

    list_display = admin.ModelAdmin.list_display + (
        'following_user',
        'followed_user',
        'created_at',
        'updated_at',
    )
