from django import template

register = template.Library()


# Add your filter
# https://docs.djangoproject.com/zh-hans/3.0/howto/custom-template-tags/
@register.filter(name='cut')
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '-')


register.filter('cut', cut)
