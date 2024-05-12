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


def create_link(username, project_name, name, source, target):
    user = User.objects.get(username=username)
    project = Project.objects.get(user=user, name=project_name)
    Link.objects.create(
        project=project,
        name=name,
        source=Factor.objects.get(name=source),
        target=Factor.objects.get(name=target),
    )


def get_all_factors(username, project_name):
    user = User.objects.get(username=username)
    project = Project.objects.get(user=user, name=project_name)
    return list(Factor.objects.filter(project=project).values_list("name", flat=True))
