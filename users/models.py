from django.db import models
from django.contrib.auth.models import User, AbstractUser


class User(AbstractUser):
    ROLE_CHOICE = (
        ('user', 'User'),
        ('admin', 'Admin'),
        ('superuser', 'SuperUser')
    )
    role = models.CharField(max_length=50, default='user', choices=ROLE_CHOICE)
    is_deleted = models.BooleanField(default=False)