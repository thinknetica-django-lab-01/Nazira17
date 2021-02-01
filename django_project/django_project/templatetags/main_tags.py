import datetime
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


@register.filter(name="string_reverse")
@stringfilter
def string_reverse(value):
    return value[::-1]
