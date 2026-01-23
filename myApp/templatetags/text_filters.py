from django import template

register = template.Library()


@register.filter
def split_at_colon(value):
    """Split text at colon and return as tuple (headline, description)"""
    if ':' in value:
        parts = value.split(':', 1)
        return {'headline': parts[0].strip(), 'description': parts[1].strip()}
    return {'headline': value, 'description': value}

@register.filter
def split_paragraphs(value):
    """Split text by double newline (\n\n) or single newline (\n) and return as list"""
    if not value:
        return []
    # Try double newline first
    if '\n\n' in value:
        parts = value.split('\n\n')
    else:
        # Fall back to single newline
        parts = value.split('\n')
    return [part.strip() for part in parts if part.strip()]

