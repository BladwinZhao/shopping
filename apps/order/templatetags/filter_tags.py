from django import  template

#实例化注册器

register = template.Library()


#filter 过滤器
#simple_tags
@register.filter
def test1(value,number):
    return value*number

