from rest_framework import serializers

from xiaobing.models import Order, OrderType, IpInfo


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id', 'orderName', 'orderType', 'isShow', 'isSplit', 'orderDescription', 'orderTypeDescription', 'number',
            'createTime')


class OrderTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderType
        fields = ('id', 'orderTypeName', 'number', 'createTime')


class IpInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = IpInfo
        fields = ('id', 'region', 'province', 'city', 'longitude', 'latitude', 'accessTime')
