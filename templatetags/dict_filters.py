from django import template

register = template.Library()

@register.filter
def get_item(dictionary,key):
    """Custom filter to get dict item by key"""
    if dictionary and key in dictionary:
        return dictionary.get(key)
    return ""