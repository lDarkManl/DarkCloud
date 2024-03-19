import calendar
import json
from datetime import date
from dateutil.relativedelta import relativedelta
from django.shortcuts import render, reverse, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.views.generic import ListView

from todo.models import Task, Section, Project
from todo.forms import TaskForm, SectionForm, ProjectCreateForm, ProjectUpdateForm
from todo import services

def create_or_update_project(request, pk=None):
	if pk:
		services.create_or_update(request, Project, ProjectUpdateForm, pk)
	else:
		services.create_or_update(request, Project, ProjectCreateForm, pk)
	return HttpResponseRedirect(request.META['HTTP_REFERER'])

def create_or_update_task(request, pk=None):
	services.create_or_update(request, Task, TaskForm, pk)
	return HttpResponseRedirect(request.META['HTTP_REFERER'])

def create_or_update_section(request, pk=None):
	services.create_or_update(request, Section, SectionForm, pk)
	return HttpResponseRedirect(request.META['HTTP_REFERER'])

def delete_project(request, pk):
	services.delete_obj(request, Project, pk)
	return HttpResponseRedirect(reverse('todo:today'))

def delete_section(request, pk):
	services.delete_obj(request, Section, pk)
	return HttpResponseRedirect(reverse('todo:today'))

def delete_task(request, pk):
	services.delete_obj(request, Task, pk)
	return HttpResponseRedirect(reverse('todo:today'))

def change_status_task(request, pk):
	'''Изменить статус задачи'''
	task = get_object_or_404(Task, pk=pk)
	task.completed = not(task.completed)
	task.save()
	return HttpResponseRedirect(request.META['HTTP_REFERER'])

def project_view(request, pk):
	'''View для действий с проектом'''
	tasks = Task.objects.filter(project_id=pk, completed=False).order_by('pub_date').select_related('project')
	project = Project.objects.get(id=pk)

	create_section_form = SectionForm(initial={'project': project})
	objects_list = tasks

	context = {}
	context.update(services.get_tasks_forms_context(tasks, TaskForm, {'project': project}))
	context['objects_list'] = objects_list
	
	if project.project_type == Project.SECTIONS:
		result = services.make_project_sections(tasks, project)
		context.update(result)
	context['create_section_form'] = create_section_form
	context['project'] = project
	context['project_type'] = {
		'LIST': Project.LIST,
		'SECTIONS': Project.SECTIONS
	}
	context.update(services.get_head_context(request, project))
	return render(request, 'todo/project.html', context)
	
def today_view(request):
	today = date.today()
	return HttpResponseRedirect(reverse('todo:date', args=(today.year, today.month, today.day)))

def all_view(request):
	tasks_list = Task.objects.filter(completed=False)
	context = {}
	context['tasks_list'] = tasks_list
	context.update(services.get_tasks_forms_context(tasks_list, TaskForm, {}))
	return render(request, 'todo/all.html', context)

def completed(request):
	tasks_list = Task.objects.filter(completed=True).order_by('pub_date')
	context = {}
	context['tasks_list'] = tasks_list
	context.update(services.get_tasks_forms_context(tasks_list, TaskForm))
	return render(request, 'todo/completed.html', context)

def date_view(request, year, month, day):
	formatted_date = date(year, month, day)
	tasks_list = Task.objects.filter(date=formatted_date, completed=False)
	context = {}
	context['tasks_list'] = tasks_list
	context.update(services.get_tasks_forms_context(tasks_list, TaskForm, {'date': formatted_date}))
	return render(request, 'todo/date.html', context)

def next_calendar(request, year, month):
	formatted_date = date(year, month, 1)
	new_date = formatted_date + relativedelta(months=1)
	year = new_date.year
	month = new_date.month
	return HttpResponseRedirect(reverse('todo:calendar_main', args=(year, month)))

def prev_calendar(request, year, month):
	formatted_date = date(year, month, 1)
	new_date = formatted_date - relativedelta(months=1)
	year = new_date.year
	month = new_date.month
	return HttpResponseRedirect(reverse('todo:calendar_main', args=(year, month)))

def calendar(request):
	today = date.today()
	year = today.year
	month = today.month
	return HttpResponseRedirect(reverse('todo:calendar_main', args=(year, month)))

def calendar_main(request, year, month):
	'''Работа с календарем'''
	day = None
	today = date.today()
	if month == today.month and year == today.year:
		day = today.day
	calendar_array = services.get_calendar(year, month)
	context = {}
	context['year'] = year
	context['month'] = month
	context['curr_day'] = day
	context['months'] = services.months
	context['calendar'] = calendar_array
	return render(request, 'todo/calendar.html', context)