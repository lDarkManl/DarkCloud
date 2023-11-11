from django import template
from todo.models import Project
from todo.forms import TaskForm

register = template.Library()

@register.simple_tag()
def get_from_dict(d, key):
	return d.get(key, None)

@register.simple_tag()
def get_projects():
	return Project.objects.all()

@register.simple_tag()
def get_create_task_form():
	return TaskForm()

