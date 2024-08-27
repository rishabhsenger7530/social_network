from django.db.models import Q
from rest_framework import serializers

from .models import *


class FriendRequestSerializer(serializers.ModelSerializer):
    """
    Serializer for creating friend request
    """
    class Meta:
        model = FriendRequest
        fields = ['request_to']
    def create(self, validated_data):
        request_from = self.context.get('request_from')
        request_to  =  validated_data.get('request_to')
        if request_from == request_to:
            raise serializers.ValidationError("You cannot send a friend request to yourself.")

        # Check if user has already send the request
        status_condition = Q(status='accepted') | Q(status='pending')
        frnd_obj = FriendRequest.objects.filter(
            Q(request_from=request_from) & 
            Q(request_to=request_to) & 
            status_condition
        )
        if not frnd_obj.exists():
            return  FriendRequest.objects.create(request_from = request_from, request_to=request_to, status='pending')
        return frnd_obj.first()


class FriendRequestSerializerGET(serializers.ModelSerializer):
    """
    Serializer for retrieving  Pending request
    """
    request_user_id = serializers.CharField(source='request_from.id')
    request_user_email = serializers.CharField(source='request_from.email')
    request_from = serializers.CharField(source='request_from.first_name')
    class Meta:
        model = FriendRequest
        fields = ['id' ,'request_user_id', 'request_user_email', 'request_from']

class FriendRequestUpdateSerializer(serializers.ModelSerializer):
    """ 
    Serializer for accepting and rejecting friend request 
    """
    STATUS_CHOICES = [
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    status = serializers.ChoiceField(choices=STATUS_CHOICES)
    class Meta:
        model = FriendRequest
        fields = ['status','id']

    def update(self, instance, validated_data):
        status = validated_data.get('status')
        instance.status = status
        instance.save()
        if status == 'accepted':
            instance.request_to.friends.add(instance.request_from)
        return instance

class FriendListSerializer(serializers.ModelSerializer):
    """
    CustomUser Serializer
    """
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'email', 'last_name')
