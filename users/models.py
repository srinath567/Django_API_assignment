from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    telegram_username = models.CharField(max_length=255, blank=True, null=True)
    telegram_chat_id = models.CharField(max_length=255, blank=True, null=True)
    
    # Add related_name to avoid conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    
    def __str__(self):
        return self.username

    @classmethod
    def create_superuser(cls, username, email, password=None, **extra_fields):
        if not password:
            password = 'admin123'  # Default password
        return super().create_superuser(username, email, password, **extra_fields) 