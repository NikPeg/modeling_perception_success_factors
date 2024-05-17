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
    _NAME_TO_VALUE = {
        "Very poor": 0.1,
        "Poor": 0.2,
        "Fair": 0.3,
        "Satisfactory": 0.4,
        "Below average": 0.5,
        "Average": 0.6,
        "Above average": 0.7,
        "Good": 0.8,
        "Very good": 0.9,
        "Excellent": 1.0,
    }
    # One-to-many relationship with project
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    # Factor name
    name = models.CharField(max_length=100)

    value = models.FloatField(default=0.5)

    def __str__(self):
        return self.name

    @classmethod
    def term_to_value(cls, term):
        return cls._NAME_TO_VALUE[term]


class Link(models.Model):
    _NAME_TO_VALUE = {
        "No influence": 0.0,
        "Very low": 0.2,
        "Low": 0.4,
        "Moderate": 0.5,
        "High": 0.6,
        "Very high": 0.8,
        "Total": 1.0,
    }
    # One-to-many relationship with project
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    source = models.ForeignKey(Factor, on_delete=models.CASCADE, related_name="source_links", default=None)
    target = models.ForeignKey(Factor, on_delete=models.CASCADE, related_name="target_links", default=None)

    value = models.FloatField(default=0.5)

    def __str__(self):
        return f"{self.source.name}->{self.target.name}"

    @classmethod
    def term_to_value(cls, term):
        return cls._NAME_TO_VALUE[term]