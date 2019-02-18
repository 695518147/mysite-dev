from threading import Thread
from mysite.settings import gather_information

from xiaobing.getIPInfo import ip_address

try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x


class SimpleMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path in gather_information:
            Thread(target=ip_address).start()
