from datetime import date
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.core.exceptions import ValidationError
from smart_selects.db_fields import ChainedForeignKey


class Task(models.Model):
	'''Модель задачи'''
	
	title = models.CharField('Название задачи', max_length=255)
	description = models.TextField('Описание', blank=True)
	completed = models.BooleanField('Статус', default=False)
	section = ChainedForeignKey('Section',
        chained_field="project",
        chained_model_field="project",
        show_all=False,
        auto_choose=False,
        sort=False,
        null=True,
        blank=True
   	)
	project = models.ForeignKey('Project', on_delete=models.CASCADE, verbose_name='Проект', related_name='project_task')
	pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
	update_date = models.DateTimeField('Дата обновления', auto_now=True)
	time = models.TimeField('Время выполнения', null=True, blank=True)
	date = models.DateField('Дата выполнения', null=True, blank=True)
	notification = models.DateTimeField('Время уведомления', null=True, blank=True)

	def __str__(self):
		'''Возвращает название задачи при обращении к экземпляру'''
		return self.title

	def get_absolute_url(self):
		'''Получить url к задаче'''
		return reverse('todo:change_task', kwargs={'pk': self.id})

	def clean(self):
		'''
		Проверка на то, что выбранная секция связана с выбранным проектом типа секции
		либо нет выбранной секции при проекте типа список
		'''
		if self.project.project_type == Project.LIST and self.section is not None:
			raise ValidationError('Cannot use Section in Project type \'LIST\'')

		if self.project.project_type == Project.SECTIONS:
			if self.section is None:
				raise ValidationError('Cannot assign Task to Project type Sections without Section')

			elif self.section.project != self.project:
				raise ValidationError('Cannot use other project\'s Section in current Project')

	class Meta:
		'''Метакласс'''
		verbose_name = 'Задача'
		verbose_name_plural = 'Задачи'



class Section(models.Model):
	'''Класс секции, в секциях будут задачи'''

	title = models.CharField('Название секции', max_length=255)
	project = models.ForeignKey('Project', on_delete=models.CASCADE, verbose_name='Проект', related_name='section')

	def __str__(self):
		'''Возвращает название секции при обращении к экземпляру'''
		return self.title

	def get_absolute_url(self):
		'''Получить url к секции'''
		return reverse('todo:change_section', kwargs={'pk': self.id})

	def clean(self):	
		'''Проверка на то, что секция не принадлежит проекту с типом список'''
		if self.project.project_type == Project.LIST:
			raise ValidationError('Cannot assign Section to Project with project type \'LIST\'')

	class Meta:
		'''Метакласс'''
		verbose_name = 'Секция'
		verbose_name_plural = 'Секции'



class Project(models.Model):
	'''Класс проекта, по проектам будут распределены разделы'''

	LIST = 'L'
	SECTIONS = 'S'
	types = [
		(LIST, 'Список'),
		(SECTIONS, 'Секции')
	]

	title = models.CharField('Название проекта', max_length=255)
	description = models.TextField('Описание', blank=True)
	project_type = models.CharField('Тип проекта', choices=types, max_length=1)

	def __str__(self):
		'''Возвращает название проекта при обращении к экземпляру'''
		return self.title

	def get_absolute_url(self):
		'''Получить url к проекту'''
		return reverse('todo:project', kwargs={'pk': self.id})

	@property
	def get_sections_amount(self):
		return self.section.count()

	class Meta:
		'''Метакласс'''
		verbose_name = 'Проект'
		verbose_name_plural = 'Проекты'



		