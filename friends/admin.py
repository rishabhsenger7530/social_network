from django.contrib import admin

from .models import FriendRequest


class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'request_from', 'request_to', 'status', 'created_at')

    search_fields = ('request_from__email', 'request_from__email', 'status')

    list_filter = ('status',)

admin.site.register(FriendRequest, FriendRequestAdmin)
