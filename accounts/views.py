from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.custom_pagination import UserSearchPagination

from .models import *
from .serializers import *
from .serializers import ObtainTokenPairSerializer


class ObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = ObtainTokenPairSerializer


class RegisterView(generics.CreateAPIView):
    """
    User Registration view , handles signup
    """
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserSearchViewSet(generics.ListAPIView):
    """
    View Returns  User  searched by name or  Email.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = UserSearchPagination

    def get_queryset(self):
        keyword = self.request.GET.get('search')
        if keyword:
            return CustomUser.search_users(keyword)
        return super().get_queryset()
