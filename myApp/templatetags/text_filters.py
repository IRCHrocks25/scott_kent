from django import template

register = template.Library()


@register.filter
def split_at_colon(value):
    """Split text at colon and return as tuple (headline, description)"""
    if ':' in value:
        parts = value.split(':', 1)
        return {'headline': parts[0].strip(), 'description': parts[1].strip()}
    return {'headline': value, 'description': value}

