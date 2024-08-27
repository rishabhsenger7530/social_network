from django.urls import path

from .views import *

"""
these are the urls for friends app
"""
urlpatterns = [
    path('friend-list/', ListFriends.as_view()),
    path('friend-request/', FriendRequestViewSet.as_view()),
    path('update-request/<int:pk>/', UpdateFriendRequestStatus.as_view()),
]
