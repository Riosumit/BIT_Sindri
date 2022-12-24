from django.contrib import admin
from django.urls import path, include, re_path
from .views import result, registration

urlpatterns = [
    path('result/', result, name="result"),
    path('registration', registration, name="registration")
]