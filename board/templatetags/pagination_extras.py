from django import template

register = template.Library()

@register.simple_tag
def pagination_reverse_numbering(paginator, page_obj, loop_count):
    return paginator.count - page_obj.start_index() - loop_count + 1