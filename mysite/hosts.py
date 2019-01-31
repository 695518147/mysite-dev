from django_hosts import patterns, host


host_patterns = patterns('',
                         host(r'www', 'wap.urls', name='www'),
                         host(r'xb', 'mysite.urls', name='xb'),
                         )
