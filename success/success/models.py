from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Project(models.Model):
    # One-to-many relationship with Django's built-in User model
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # Project name
    name = models.CharField(max_length=100)

    # Privacy setting: either 'public' or 'private'
    PRIVACY_CHOICES = (
        ('PUBLIC', 'Public'),
        ('PRIVATE', 'Private'),
    )
    privacy = models.CharField(max_length=7, choices=PRIVACY_CHOICES, default="PRIVATE")

    def __str__(self):
        return self.name

    constraints = [
        models.UniqueConstraint(fields=['user', 'name'], name='unique name for user')
    ]


class Template(models.Model):
    # Template name
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    constraints = [
        models.UniqueConstraint(fields=['name'], name='unique name for template')
    ]


class Factor(models.Model):
    # One-to-many relationship with project
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    # Factor name
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Link(models.Model):
    # One-to-many relationship with project
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    # link name
    name = models.CharField(max_length=100)

    source = models.ForeignKey(Factor, on_delete=models.CASCADE, related_name="source_links", default=None)
    target = models.ForeignKey(Factor, on_delete=models.CASCADE, related_name="target_links", default=None)

    def __str__(self):
        return self.name
