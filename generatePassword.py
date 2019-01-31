import sys;

print('Python %s on %s' % (sys.version, sys.platform))
import django

print('Django %s' % django.get_version())
if 'setup' in dir(django): django.setup()
from django.contrib.auth.hashers import make_password


def getPassword():
    django.run("/Users/zhangpeiyu/zhangpeiyu/mysite")
    return make_password('mm518147')


if __name__ == "__main__":
    getPassword()
