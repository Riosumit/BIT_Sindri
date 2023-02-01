from django.contrib import admin
from django.urls import path, include, re_path

from .views import login, admin_home, degree, add_degree, course, add_course, link, add_link

urlpatterns = [
    path('', login, name="login"),
    path('home', admin_home, name="admin_home"),
    path('degree', degree, name="degree"),
    path('add_degree', add_degree, name="add_degree"),
    path('course', course, name="course"),
    path('add_course', add_course, name="add_course"),
    path('link', link, name="link"),
    path('add_link', add_link, name="add_link")
]
