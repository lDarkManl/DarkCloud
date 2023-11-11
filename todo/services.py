import calendar
from django.shortcuts import render, reverse, get_object_or_404
from django.contrib import messages

from todo.forms import TaskForm, SectionForm, ProjectCreateForm, ProjectUpdateForm
from todo.models import Task, Section, Project

months = {
	1: 'Январь',
	2: 'Февраль',
	3: 'Март',
	4: 'Апрель',
	5: 'Май',
	6: 'Июнь',
	7: 'Июль',
	8: 'Август',
	9: 'Сентябрь',
	10: 'Октябрь',
	11: 'Ноябрь',
	12: 'Декабрь',
}

def make_forms_from_instances(objects, form):
	'''Принимает объекты и форму, отдает словарь с формами, 
	соответствующими первичномым ключам объектов'''
	form_dict = {}
	for obj in objects:
		form_dict[obj.pk] = form(instance=obj)
	return form_dict

def make_project_sections(tasks, project):
	'''Распределяет задачи по секциям в одном проекте,
	также делает формы создания задачи для каждой секции в проекте'''
	sections = Section.objects.filter(project=project)
	context = {}
	objects_list = {}
	create_forms = {}
	section_forms = make_forms_from_instances(sections, SectionForm)
	for section in sections:
		tasks_list = tasks.filter(section_id=section.id)
		objects_list[section] = tasks_list
		create_forms[section.pk] = TaskForm(initial={'project': project, 'section': section})
		
	context['section_forms'] = section_forms
	context['objects_list'] = objects_list
	context['create_forms'] = create_forms
	return context

def create_or_update(request, model_class, form_class, pk=None):
	'''Создает или обновляет запись в базе по форме'''
	if request.method == 'POST':

		if pk:
			obj = get_object_or_404(model_class, pk=pk)
			form = form_class(request.POST, instance=obj)
		else:
			form = form_class(request.POST)

		if form.is_valid():
			form.save()
		else:
			messages.error(request, form.non_field_errors())

def delete_obj(request, model_class, pk):
	'''Удаляет объект'''
	obj = get_object_or_404(model_class, pk=pk)
	obj.delete()

def get_head_context(request, project):
	'''Получить контекст для head в приложении todo'''
	context = {}
	projects_list = Project.objects.all()
	context['create_project_form'] = ProjectCreateForm()
	context['project_form'] = ProjectUpdateForm(instance=project)
	return context

def get_tasks_forms_context(tasks_list, form_class, initial=None):
	'''Создать формы для изменения и добавления задачи 
	и добавить их в контекст'''
	context = {}
	context['update_forms'] = make_forms_from_instances(tasks_list, form_class)
	context['create_form'] = TaskForm(initial=initial)
	return context

def get_calendar(year, month):
	calendar_obj = calendar.Calendar().monthdatescalendar(year, month)
	calendar_array = [[day.day if day.month == month else 0 for day in week] for week in calendar_obj]
	return calendar_array

def get_ordered_sections():
	projects_list = Project.objects.all()
	sections_list = Section.objects.select_related('project')
	projects = {project.title: [] for project in projects_list}
	for section in sections_list:
		projects[section.project.title].append(section.title)
	return projects