from django.contrib import admin

from user.models import User


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):

    list_display = admin.ModelAdmin.list_display + (

        'created_at',
        'updated_at',
    )
