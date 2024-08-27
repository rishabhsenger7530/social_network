from django.contrib import admin

from .models import *


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'date_joined')

    search_fields = ('email', 'first_name', 'last_name')

admin.site.register(CustomUser, CustomUserAdmin)
