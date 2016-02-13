from django import template

register = template.Library()

@register.filter(expects_localtime=True)
def datetime(value, arg):
    return value.strftime(arg)