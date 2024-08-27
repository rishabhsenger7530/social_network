from django.urls import path

from .views import UserSearchViewSet

urlpatterns = [
    path('search-users/', UserSearchViewSet.as_view(), name='search-users')
]