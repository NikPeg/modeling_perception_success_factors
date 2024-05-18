from django.contrib.auth.models import User

from .models import *

COMMON_PROJECT_LABEL = "public"


def create_project(username: str, name: str):
    user = User.objects.get(username=username) if username != COMMON_PROJECT_LABEL else None
    Project.objects.get_or_create(
        user=user,
        name=name,
    )


def create_factor(username, project_name, name, value):
    user = User.objects.get(username=username) if username != COMMON_PROJECT_LABEL else None
    project = Project.objects.get(user=user, name=project_name)
    Factor.objects.create(project=project, name=name, value=value)


def create_link(username, project_name, source, target, value):
    user = User.objects.get(username=username) if username != COMMON_PROJECT_LABEL else None
    project = Project.objects.get(user=user, name=project_name)
    Link.objects.create(
        project=project,
        source=Factor.objects.get(name=source, project=project),
        target=Factor.objects.get(name=target, project=project),
        value=value,
    )


def get_all_factors(username, project_name):
    user = User.objects.get(username=username) if username != COMMON_PROJECT_LABEL else None
    project = Project.objects.get(user=user, name=project_name)
    factors = list(Factor.objects.filter(project=project).values_list("name", "value"))
    return [{"id": factor[0], "value": factor[1]} for factor in factors]


def get_all_projects(username):
    user = User.objects.get(username=username)
    return list(Project.objects.filter(user=user).values_list("name", flat=True))


def get_all_public_projects(to_exclude=[]):
    return list(Project.objects.filter(user=None).exclude(name__in=to_exclude).values_list("name", flat=True))


def get_all_templates():
    return list(Template.objects.values_list("name", flat=True))


def get_all_links(username, project_name):
    user = User.objects.get(username=username) if username != COMMON_PROJECT_LABEL else None
    project = Project.objects.get(user=user, name=project_name)
    links = list(Link.objects.filter(project=project).values_list("source__name", "target__name", "value"))
    return [{"source": link[0], "target": link[1], "type": link[2]} for link in links]
