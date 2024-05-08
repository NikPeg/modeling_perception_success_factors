from .models import *
from django.contrib.auth.models import User


def create_project(username: str, name: str):
    user = User.objects.get(username=username)
    Project.objects.get_or_create(
        user=user,
        name=name,
    )


def create_factor(username, project_name, name):
    user = User.objects.get(username=username)
    project = Project.objects.get(user=user, name=project_name)
    Factor.objects.create(project=project, name=name)
