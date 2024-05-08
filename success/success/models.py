from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Project(models.Model):
    # One-to-one relationship with Django's built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Project name
    name = models.CharField(max_length=100)

    # Privacy setting: either 'public' or 'private'
    PRIVACY_CHOICES = (
        ('PUBLIC', 'Public'),
        ('PRIVATE', 'Private'),
    )
    privacy = models.CharField(max_length=7, choices=PRIVACY_CHOICES, default='private')

    def __str__(self):
        return self.name
