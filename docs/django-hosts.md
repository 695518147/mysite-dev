### 1.安装 ：pip install django-hosts

- [官方文档](https://django-hosts.readthedocs.io/en/latest/index.html)

这个Django应用程序将特定域名的请求路由到名为“hostconfs”的模块中定义的不同URL方案。  
例如，如果您拥有example.com但希望在api.example.com和beta.example.com上提供特定内容，
请将以下内容添加到 hosts.py文件中：

```python
from django_hosts import patterns, host

host_patterns = patterns('path.to',
    host(r'api', 'api.urls', name='api'),
    host(r'beta', 'beta.urls', name='beta'),
)
```
- 模式按顺序匹配。如果没有模式匹配，则以通常的方式处理请求，即。使用标准ROOT_URLCONF。

### 2.使用步骤

```
1.将“django_hosts”添加到INSTALLED_APPS设置中。

2.在中间件的开头和结尾分别添加：“django_hosts.middleware.HostsRequestMiddleware” 和 
“django_hosts.middleware.HostsResponseMiddleware”。

3.创建hosts.py。并设置不同主机的路由。

4.将ROOT_HOSTCONF设置为包含主机模式的模块的虚线Python导入路径，例如：
    ROOT_HOSTCONF ='mysite.hosts'
5.将DEFAULT_HOST设置为要作为默认模式引用的主机模式的名称。
如果没有其他模式匹配或者您没有为host_url模板标记指定名称，则会使用它。
```

在模板中，您可以使用 host_url()模板标签以Django的url模板标记的方式反转URL：

```
{% load hosts %}
<a href="{% host_url 'homepage' host 'www' %}">Home</a> |
<a href="{% host_url 'account' host 'wildcard' request.user.username %}">Your Account</a> |

```
