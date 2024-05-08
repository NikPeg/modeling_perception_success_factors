from .models import *
from django.contrib.auth.models import User


def create_project(username: str, name: str):
    user = User.objects.get(username=username)
    Project.objects.create(
        user=user,
        name=name,
    )
