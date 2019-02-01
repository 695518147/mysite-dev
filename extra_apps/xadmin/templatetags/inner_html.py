from django.template import Library

# 将注册类实例化为register对象
from django.utils.safestring import mark_safe

register = Library()


# 使用装饰器注册
@register.filter
def inner_html(val):
    result = "<div style='display: inline-block;'>" + str(val) + "</div>"
    return result


@register.filter
def nowrap(val):
    if isinstance(val, str):
        val = mark_safe(val.replace("\"<p>", "").replace("</p>\"", "").strip())
    return val
