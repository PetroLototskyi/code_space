import os
from django import template

register = template.Library()

@register.filter
def basename(value):
    return os.path.basename(value)

@register.filter
def filter_by_drawing(approvals, drawing_id):
    return [approval for approval in approvals if approval.drawing_id == drawing_id]
