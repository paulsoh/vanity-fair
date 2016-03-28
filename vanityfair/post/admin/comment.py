from django.contrib import admin

from post.models import Comment


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):

    list_display = admin.ModelAdmin.list_display + (
        'content',

        'created_at',
        'updated_at',
    )
