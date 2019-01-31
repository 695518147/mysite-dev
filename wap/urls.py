from django.urls import path, re_path
from django.views.static import serve

from mysite import settings
from wap import views

urlpatterns = [
    path('', views.index),
]

urlpatterns += [
    # 媒体文件前缀
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # 文件前缀
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
]