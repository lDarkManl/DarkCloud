from django import template

register = template.Library()

@register.simple_tag()
def get_from_dict(d, key):
	return d.get(key, None)