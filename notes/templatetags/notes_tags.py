from django import template

register = template.Library()

@register.filter
def limit_length(string):
	"""Ограничение количества символов при выводе в списке"""
	if len(string) > 50:
		return f'{string[:50]}...'
	return string
