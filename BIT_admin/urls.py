from django.contrib import admin
from django.urls import path, include, re_path

from .views import login, admin_home, degree, add_degree

urlpatterns = [
    path('', login, name="login"),
    path('home', admin_home, name="admin_home"),
    path('degree', degree, name="degree"),
    path('add_degree', add_degree, name="add_degree")
]
