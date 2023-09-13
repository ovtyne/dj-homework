from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.simple_tag()
@stringfilter
def mediapath(img):
    if img == "":
        img = 'no_foto.jpg'
    return '/media/' + img
