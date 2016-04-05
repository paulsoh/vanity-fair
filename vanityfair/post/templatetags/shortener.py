from django import template


register = template.Library()


@register.filter
def shortener(value):
    if len(value) > 80:
        value = value[:80]+"..."
    return value
