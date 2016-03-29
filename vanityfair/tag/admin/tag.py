from django.contrib import admin

from tag.models import Tag


@admin.register(Tag)
class TagModelAdmin(admin.ModelAdmin):

    list_display = admin.ModelAdmin.list_display + (
        'name',
    )
