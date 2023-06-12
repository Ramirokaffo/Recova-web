from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()





@register.filter("filter_selected")
@stringfilter
def filter_selected(value):
    return "Toto"
