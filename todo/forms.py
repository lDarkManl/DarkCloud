from django.forms import ModelForm, TimeInput, DateInput, DateTimeInput
from django.core.exceptions import ValidationError

from todo.models import Task, Project, Section

class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = ['title', 'description', 'time', 'date', 'notification', 'project', 'section']
		widgets = {
			'time': TimeInput(attrs={'type': 'time'}),
			'date': DateInput(attrs={'type': 'date'}),
			'notification': DateTimeInput(attrs={'type': 'datetime-local'})
		}

class SectionForm(ModelForm):
	class Meta:
		model = Section
		fields = ['title', 'project']

class ProjectCreateForm(ModelForm):
	class Meta:
		model = Project
		fields = ['title', 'description', 'project_type']

class ProjectUpdateForm(ModelForm):
	class Meta:
		model = Project
		fields = ['title', 'description']

