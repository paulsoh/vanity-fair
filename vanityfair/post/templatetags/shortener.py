from django import template


register = template.Library()


@register.filter
def shortener(value):
    if len(value) > 50:
        value = value[:50]+"..."
    return value
