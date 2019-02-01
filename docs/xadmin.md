### 1.   orderType = models.ForeignKey(OrderType, on_delete=models.CASCADE, verbose_name='指令类型', ),verbose_name用于设置外键的显示。

### 2.如何显示HTML而不是HTML代码

```html
{% autoescape off %}
    {{ bc.title }}
{% endautoescape %}
```
或者：
django.utils.safestring.mark_safe
mark_safe(val)

### 3.自定义模板过滤器

