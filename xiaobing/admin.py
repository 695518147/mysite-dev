from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from xiaobing.models import Order, OrderType


class OrderAdmin(admin.ModelAdmin):
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

    fieldsets = [
        ('指令名称', {'fields': ['orderName']}),
        (None, {'fields': ['orderType']}),
        ("isShow", {'fields': ['isShow'], 'classes': ('collapse',)}),
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
    list_editable = ['number']
    # fk_fields 设置显示外键字段
    fk_fields = ('orderTypeId',)

    # 筛选器
    list_filter = ('orderType',)  # 过滤器
    search_fields = ('orderName',)  # 搜索字段
    date_hierarchy = 'createTime'  # 详细时间分层筛选　


# admin.TabularInline 水平显示   admin.StackedInline 垂直显示
class OrderInline(admin.StackedInline):
    model = Order
    extra = 0


# ModelAdmin继承此类  可以控制在admin界面的显示
class OrderTypeAdmin(admin.ModelAdmin):
    # 在admin总要显示的列
    list_display = ('orderTypeName_html', 'number', 'createTime')

    # 强制显示HTML而不是HTML代码
    def orderTypeName_html(self, obj):
        return format_html(obj.orderTypeName)

    orderTypeName_html.short_description = '指令类型名称'
    # 级联增加
    inlines = [OrderInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderType, OrderTypeAdmin)
