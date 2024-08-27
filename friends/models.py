from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import *


class FriendRequest(models.Model):
    """
    Model that stores friendrequest information
    """
    class Status_Choices(models.TextChoices):
        PENDING  = "pending", _("Pending")
        ACCEPTED = "accepted", _("Accepted")
        REJECTED = "rejected", _("Rejected")
      
    request_from = models.ForeignKey(
        CustomUser,
        related_name='request_from',
        on_delete=models.CASCADE,
        help_text='User who sent the friend request')

    request_to = models.ForeignKey(
        CustomUser,
        related_name='request_to',
        on_delete=models.CASCADE,
        help_text='User who received the friend request')
    status = models.CharField(
        choices=Status_Choices.choices,
        default=Status_Choices.PENDING,
        max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.request_from.first_name} to {self.request_to.first_name} status-{self.status}"

    class Meta:
        verbose_name = 'Friend Request'
