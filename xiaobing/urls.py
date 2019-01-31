from django.urls import path, include
from rest_framework.routers import DefaultRouter

from xiaobing.views import OrderViewSet, OrderTypeViewSet, IpInfoViewSet
from xiaobing import views

# 默认在url结尾添加一个‘/’，可以通过设置trailing_slash为False，不添加尾斜杠
router = DefaultRouter(trailing_slash=False)
router.register('order', OrderViewSet, base_name='order')
router.register('orderType', OrderTypeViewSet, base_name='orderType')
router.register('ipInfo', IpInfoViewSet, base_name='ipInfo')

urlpatterns = [
    path('', include(router.urls)),
    path('tj', views.statistics),
]
