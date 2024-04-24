from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("about/", about_view, name='about'),
    path('login/', login_view, name='login'),
    path('create/', create_view, name='create'),
    path('project/<str:name>/', project_view, name='project'),
    path('register/', register_view, name='register'),
    path('projects/<str:username>/', projects_view, name='projects'),
]
