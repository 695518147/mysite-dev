from django.db import models

from django_ueditor.models import UEditorField as ModelUEditorField
from django.utils import timezone


# 模型创建

# 指令类型
class OrderType(models.Model):
    orderTypeName = ModelUEditorField(u"指令类型名称", blank=True, toolbars='mini', width=900, height=50, imagePath="images/",
                                      filePath="files/")
    number = models.IntegerField(u"排序号", default=1)
    createTime = models.DateTimeField(u"创建时间", default=timezone.now)

    class Meta:
        ordering = ('number',)
        verbose_name = '指令类型'
        verbose_name_plural = "指令类型列表"

    def __str__(self):
        return self.orderTypeName


# 指令
class Order(models.Model):
    orderName = ModelUEditorField(u"指令名称", blank=True, toolbars='mini', width=900, height=50, imagePath="images/",
                                  filePath="files/")
    orderType = models.ForeignKey(OrderType, on_delete=models.CASCADE, verbose_name='指令类型', )
    isShow = models.BooleanField(u"是否显示该条指令", default=True)
    isSplit = models.BooleanField(u"是否分栏", default=True)
    orderDescription = ModelUEditorField(u"指令说明", blank=True, toolbars='normal', width=900, height=200,
                                         imagePath="images/", filePath="files/")
    orderTypeDescription = ModelUEditorField(u"指令类型说明", blank=True, toolbars='normal', width=900, height=200,
                                             imagePath="images/", filePath="files/")
    number = models.IntegerField(u"排序号", default=1)
    createTime = models.DateTimeField(u"创建时间", default=timezone.now)

    class Meta:
        ordering = ('number',)
        # 实体中文名
        verbose_name = '指令'
        # 实体列表中文名
        verbose_name_plural = "指令列表"

    def __str__(self):
        return self.orderName


class IpInfo(models.Model):
    region = models.CharField(u"所属地区", max_length=100)
    province = models.CharField(u"所属省", max_length=100)
    city = models.CharField(u"所属城市", max_length=100)
    longitude = models.CharField(u"经度", max_length=100)
    latitude = models.CharField(u"纬度", max_length=100)
    accessTime = models.DateTimeField(u"访问时间", default=timezone.now)

    class Meta:
        ordering = ('-accessTime',)
