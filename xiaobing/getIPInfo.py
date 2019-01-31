import os
from json import load
from urllib import request as re

import geoip2.database

from xiaobing.models import IpInfo


def ip_address():
    try:
        # 获取公网ip
        ipaddr = load(re.urlopen('https://api.ipify.org/?format=json'))['ip']
        rootPath = os.path.abspath(os.path.dirname(__file__))
        # todo地址路径需要修改
        reader = geoip2.database.Reader(rootPath + "/static/GeoLite2-City/GeoLite2-City.mmdb")
        response = reader.city(ipaddr)
        # 有多种语言,我们这里主要输出英文和中文
        info = IpInfo(region=response.continent.names["zh-CN"],
                      province=response.subdivisions.most_specific.names["zh-CN"],
                      city=response.city.names["zh-CN"], longitude=response.location.longitude,
                      latitude=response.location.latitude)
        info.save()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    ip_address()
