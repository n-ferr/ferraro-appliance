from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    ''' custom user model '''

    ROLES = [
        ('ADMIN', 'Admin'),
        ('TECH', 'Tech'),
        ('CUSTOMER', 'Customer'),
        ('STAFF', 'Staff'),
    ]

    role = models.CharField(
        max_length=10,
        choices=ROLES,
        default='CUSTOMER'
    )
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


