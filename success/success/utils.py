from .models import *
from django.contrib.auth.models import User


COMMON_PROJECT_LABEL = "public"


def create_project(username: str, name: str):
    user = User.objects.get(username=username)
    Project.objects.get_or_create(
        user=user,
        name=name,
    )


def create_public_project(name: str):
    Project.objects.get_or_create(
        user=None,
        name=name,
    )


def create_factor(username, project_name, name):
    user = User.objects.get(username=username) if username != COMMON_PROJECT_LABEL else None
    project = Project.objects.get(user=user, name=project_name)
    Factor.objects.create(project=project, name=name)


def create_link(username, project_name, name, source, target):
    user = User.objects.get(username=username) if username != COMMON_PROJECT_LABEL else None
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


def get_all_factors_public(project_name):
    project = Project.objects.get(user=None, name=project_name)
    return list(Factor.objects.filter(project=project).values_list("name", flat=True))


def get_all_projects(username):
    user = User.objects.get(username=username)
    return list(Project.objects.filter(user=user).values_list("name", flat=True))


def get_all_public_projects():
    return list(Project.objects.filter(user=None).values_list("name", flat=True))


def get_all_templates():
    return list(Template.objects.values_list("name", flat=True))


def get_all_links(username, project_name):
    user = User.objects.get(username=username)
    project = Project.objects.get(user=user, name=project_name)
    links = list(Link.objects.filter(project=project).values_list("source__name", "target__name"))
    return [
        {"source": link[0], "target": link[1], "type": "heh"}
        for link in links
    ]


def get_all_links_public(project_name):
    project = Project.objects.get(user=None, name=project_name)
    links = list(Link.objects.filter(project=project).values_list("source__name", "target__name"))
    return [
        {"source": link[0], "target": link[1], "type": "heh"}
        for link in links
    ]
