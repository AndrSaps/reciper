from django import template
from django.template.defaultfilters import register


@register.filter(name = "sum_list")
def sum_list(value):
    return sum([x.reviews for x in value])



@register.filter(name = "saved_count")
def saved_count(value):
    return sum([len(x.severs.all()) for x in value])
