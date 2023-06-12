from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter("addcent")
def addcent(value):
    return value + 1000


@register.filter("couper")
@stringfilter
def couper(value, arg):
    return value.replace(arg, "ooo")



@register.filter("majuscule")
@stringfilter
def majuscule(value):
    return value.upper()


@register.filter("filter_selected")
@stringfilter
def filter_selected(value, selected_type):

    return "" if selected_type != value else "selected-object-type"
