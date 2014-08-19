from django import template


register = template.Library()


@register.filter
def remscores(value):
    return value.replace('_', ' ')
