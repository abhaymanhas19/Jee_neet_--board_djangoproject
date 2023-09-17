from django import template
from education.models import Section

register = template.Library()


@register.simple_tag
def get_section(page_id, position):
    sections = Section.objects.filter(page_id=page_id, number=position)
    if sections:
        return sections[0]
    return {"title": "", "description": ""}
