#coding:utf-8
from django_ueditor.views import get_ueditor_controller
from django.contrib import admin
from django.urls import path

admin.autodiscover()

urlpatterns = [
    path("controller/", get_ueditor_controller),
]
