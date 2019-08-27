from django import template


register = template.Library()


@register.filter
def a_class(page, selected_page):
    if page.id == selected_page.id:
        css_class = 'bg-dark-url-active'
    else:
        css_class = 'bg-dark-url'
    return css_class
