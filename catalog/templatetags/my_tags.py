from django import template


register = template.Library()


@register.simple_tag()
def media_tag(image):
    if image:
        return f'/media/{image}'
    return '#'


@register.filter()
def media_filter(image):
    if image:
        return f'/media/{image}'
    return '#'
