from django_hosts import patterns, host

from mysite import settings

host_patterns = patterns('',
                         host(r'www', 'wap.urls', name='www'),
                         host(r'xb', settings.ROOT_URLCONF, name='xb'),
                         )
