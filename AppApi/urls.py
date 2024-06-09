from django.contrib import admin
from django.urls import path, include
from .views import TaskList

urlpatterns = [
    path('task/', TaskList.as_view(), name = "task-list"),
    path('', include('dj_rest_auth.urls')),
]