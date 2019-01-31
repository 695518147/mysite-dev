from django.contrib import admin
from django.utils.html import format_html

import xadmin
from .models import Order, OrderType


class OrderAdmin(object):
    list_display = ['orderName_html', 'get_orderTypeName', 'isShow', 'isSplit', 'number',
                    'createTime']

    # 此obj为admin.site.register注册的对象
    def get_orderTypeName(self, obj):
        return obj.orderType

    get_orderTypeName.short_description = '指令类型名称'

    # 强制显示HTML而不是HTML代码
    def orderName_html(self, obj):
        return format_html(obj.orderName)

    orderName_html.short_description = '指令名称'

    # 注意这里是content字段是你要换成ueditor的字段
    style_fields = {
        'orderName': 'ueditor',
        'orderDescription': 'ueditor',
        'orderTypeDescription': 'ueditor',
    }

    fieldsets = [
        ('指令名称', {'fields': ['orderName']}),
        (None, {'fields': ['orderType']}),
        (None, {'fields': ['isShow']}),
        (None, {'fields': ['isSplit']}),
        (None, {'fields': ['orderDescription']}),
        (None, {'fields': ['orderTypeDescription']}),
        (None, {'fields': ['number']}),
        (None, {'fields': ['createTime']}),
    ]
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 10
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('number',)
    # list_editable 设置默认可编辑字段
    list_editable = ['isShow', 'isSplit', 'number']
    # fk_fields 设置显示外键字段
    fk_fields = ('orderType',)

    # 筛选器
    list_filter = ('orderType',)  # 过滤器
    search_fields = ('orderName',)  # 搜索字段
    date_hierarchy = 'createTime'  # 详细时间分层筛选　


class OrderInline(admin.StackedInline):
    model = Order
    extra = 0


class OrderTypeAdmin(object):
    # 在admin总要显示的列
    list_display = ('orderTypeName_html', 'number', 'createTime')

    # 强制显示HTML而不是HTML代码
    def orderTypeName_html(self, obj):
        return format_html(obj.orderTypeName)

    orderTypeName_html.short_description = '指令类型名称'
    # list_editable 设置默认可编辑字段
    list_editable = ['number']
    ordering = ('number',)

    style_fields = {
        'orderTypeName': 'ueditor'
    }
    # 级联增加
    # inlines = [OrderInline]


xadmin.site.register(Order, OrderAdmin)
xadmin.site.register(OrderType, OrderTypeAdmin)
