from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager

# Create your models here.
class Users(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    phoneNumber = models.CharField(max_length=10)
    address = models.TextField()
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)
    
    ROLES = [
        ("Consumer", "Consumer"),
        ("Producer", "Producer"),
    ]
    
    role = models.CharField(choices=ROLES, default="Consumer")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    objects = UserManager()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    