# import django_filters
# from rest_framework import filters
#
# from xiaobing.models import Order
#
#
# class OrderFilter(filters.FilterSet):
#     #  从URL获得的name去模型里面进行过滤, 后面的参数是过滤规则, icontains代表模糊匹配,i代表忽略大小写,name是指定变量,
#     #  在域名上体现 如:http://localhost:8000/stu/student/?name=刘
#     name = django_filters.CharFilter('orderName', lookup_expr='icontains')
#     # tel = django_filters.CharFilter('s_tel', lookup_expr='exact') # lookup_expr匹配规则是exact代表精确匹配
#     operate_time_min = django_filters.DateTimeFilter('createTime', lookup_expr='gte')  # 请求的是大于该值的
#     operate_time_max = django_filters.DateTimeFilter('createTime', lookup_expr='lte')  # 请求的是小于该值的, 下同
#     isShow = django_filters.NumberFilter('isShow', lookup_expr='exact')
#
#     class Meta:
#         model = Order
#         fields = ['orderName', 'createTime', 'isShow']  # 设置过滤的字段
