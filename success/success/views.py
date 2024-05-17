import json

from django.contrib.admin import register
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .utils import *


def home_view(request):
    return render(request, 'home.html')


def about_view(request):
    return render(request, 'about.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_qs = User.objects.filter(email=email)
        if user_qs.exists() and authenticate(request, username=email, email=email, password=password):
            return redirect('projects', email)  # Redirect to a new URL
        else:
            messages.error(request, 'Invalid login credentials.')
            return redirect('home')
    return redirect('home')


def register_view(request):
    if request.method == 'POST':
        passwords = request.POST.getlist("password")
        if passwords[0] != passwords[1]:
            messages.error(request, "Passwords don't match!")
            return redirect('home')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create_user(email, email, password)
        return redirect('projects', email)


def projects_view(request, username):
    projects = get_all_projects(username)
    public_projects = get_all_public_projects()
    templates = get_all_templates()
    return render(request, 'projects.html', {'username': username, 'projects': projects, 'public_projects': public_projects, 'templates': templates})


def d3_view(request):
    return render(request, 'd3.html')


def project_view(request, username, name):
    if username == "public":
        create_public_project(name)
        factors = get_all_factors_public(name)
        links = get_all_links_public(name)
        return render(request, 'project.html', {'username': "public", 'name': name, 'factors': factors, 'links': links})
    create_project(username, name)
    factors = get_all_factors(username, name)
    links = get_all_links(username, name)
    return render(request, 'project.html', {'username': username, 'name': name, 'factors': factors, 'links': links})


def factor_view(request, username, project_name):
    if request.method == 'POST':
        factor_name = request.POST.get("factorName")
        create_factor(username, project_name, factor_name)
        return redirect('project', username, project_name)


def link_view(request, username, project_name):
    if request.method == 'POST':
        link_name = request.POST.get("linkName")
        source_name = request.POST.get("sourceFactor")
        target_name = request.POST.get("targetFactor")
        create_link(username, project_name, link_name, source_name, target_name)
        return redirect('project', username, project_name)


def create_view(request, username):
    if request.method == 'POST':
        name = request.POST.get("projectName")
        privacy = request.POST.get('projectType')
        if privacy == "public":
            return redirect('project', "public", name)
        return redirect('project', username, name)
