from django.db import models
from django.contrib.auth.models import AbstractUser ,Group, Permission

#Create a custom user model that extends Django’s AbstractUser, 

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    
    # Update related names to avoid conflicts
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Changed from 'user_set' to avoid conflict
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Changed from 'user_set' to avoid conflict
        blank=True,
    ) 