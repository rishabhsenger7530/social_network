from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import *

from .serializers import *
from .throtling import FriendRequestThrottleRate


class FriendRequestViewSet(generics.ListCreateAPIView):
    """
    GET : list out all the pending request
    POST : send friend request 
    """
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [FriendRequestThrottleRate]
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        return self.queryset.filter(request_to=self.request.user, status='pending')
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request_from'] = self.request.user
        return context
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message: request sent "}, status=status.HTTP_201_CREATED, headers=headers)
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FriendRequestSerializerGET
        else:
            return self.serializer_class
    
    

class ListFriends(generics.ListAPIView):
    """
    View for listing all friends of User.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = FriendListSerializer
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        return self.request.user.friends.all()


class UpdateFriendRequestStatus(APIView):
    """
    View for handling friendrequest accept or reject status
    """
    serializer_class = FriendRequestUpdateSerializer
    permission_classes = [IsAuthenticated]
    
    def patch(self, request, pk):
        status_value = request.data.get('status')
        if status_value not in dict(self.serializer_class.STATUS_CHOICES):
            return Response({"error": "Invalid status choice."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            friend_request = FriendRequest.objects.get(pk=pk, request_to=self.request.user)
        except FriendRequest.DoesNotExist:
            return Response({"error": "Friend request not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(friend_request, data={'status': status_value})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data={"message": f"Friend request {status_value}"})
