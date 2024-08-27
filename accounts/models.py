from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    '''
    User Model .
    '''

    email = models.EmailField(
        unique=True, 
        validators=[EmailValidator(message=_("Enter a valid email address."))]
    )
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    friends = models.ManyToManyField("self",
                                     related_name="user_friends",
                                     blank=True) # Allows users to have no friends

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    @classmethod
    def search_users(cls, keyword):
        """
        Search users by email (exact match) or by name (partial match).
        """
        return cls.objects.filter(
            Q(email__iexact=keyword) | Q(first_name__icontains=keyword) | Q(last_name__icontains=keyword)
        )
 
    class Meta:
        verbose_name ='Custom User'
