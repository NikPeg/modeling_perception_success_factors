from django.contrib import admin
from django.urls import path, re_path

from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("about/", about_view, name="about"),
    path("login/", login_view, name="login"),
    path("create/<str:username>/", create_view, name="create"),
    path("project/<str:username>/<str:name>/", project_view, name="project"),
    path("register/", register_view, name="register"),
    path("projects/<str:username>/", projects_view, name="projects"),
    path("d3/", d3_view, name="d3"),
    path("factor/<str:username>/<str:project_name>/", factor_view, name="factor"),
    path("link/<str:username>/<str:project_name>/", link_view, name="link"),
]
