import json

from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page, never_cache
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from xiaobing.models import Order, OrderType, IpInfo
from xiaobing.serializers import OrderSerializers, OrderTypeSerializers, IpInfoSerializers


@cache_page(60 * 60)  # 秒数，这里指缓存 60 分钟，
def index(request):
    return render(request, "index.html")


@never_cache
def statistics(request):
    infos = IpInfo.objects.all()
    citys = {}
    attr = []  # 这样X坐标
    v1 = []
    for info in infos:
        if info.city in citys:
            citys[info.city] = citys[info.city] + 1
        else:
            citys[info.city] = 1
    for k, v in citys.items():
        attr.append(k)
        v1.append(v)

    return render(request, "tj.html", {"key": json.dumps(attr), "val": json.dumps(v1)})


class Pagination(PageNumberPagination):
    # 单页数据量
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    # 单页最大数据量
    max_page_size = 20


class OrderViewSet(
    mixins.ListModelMixin,  # -->用于序列化 用于get检索所有信息进行排列
    mixins.RetrieveModelMixin,  # -->用于get检索 可以根据id进行检索
    mixins.UpdateModelMixin,  # -->用于patch, put更新
    mixins.DestroyModelMixin,  # --> 用于delete去删除数据
    mixins.CreateModelMixin,  # --> 用于post去创建数据
    GenericViewSet  # --->用于去get所有的queryset信息,可以进行过滤,
):
    queryset = Order.objects.filter(isShow=1).prefetch_related()
    serializer_class = OrderSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # 注册使用的分页类
    # pagination_class = Pagination
    # filter_class = OrderFilter
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('orderName', 'orderType')

    # 重新定义排序顺序
    def get_queryset(self):
        query = self.queryset
        return query.order_by('number')

    # 重构了DELETE方法
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  # 获取当前对象
        instance.delete()
        return Response({'msg': '删除成功', 'code': 200})
    # 注意这里的Response应该是从 from rest_framework.response import Response 导入的


class OrderTypeViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin,
                       GenericViewSet
                       ):
    queryset = OrderType.objects.all()
    serializer_class = OrderTypeSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # 注册使用的分页类
    # pagination_class = Pagination


class IpInfoViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = IpInfo.objects.all()
    serializer_class = IpInfoSerializers
