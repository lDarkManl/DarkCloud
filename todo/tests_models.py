from django.test import TestCase
from todo.models import Task, Section, Project
from django.core.exceptions import ValidationError

class TaskTestList(TestCase):
	'''Тестирование случая без времени выполнения, проект типа список'''

	def setUp(self):
		project = Project.objects.create(title='Тестовый проект', project_type=Project.LIST)
		task = Task.objects.create(title='Тестовое задание', project=project)

	def test_normal_case(self):
		task = Task.objects.get(title='Тестовое задание')
		self.assertEqual(str(task), 'Тестовое задание')
		self.assertEqual(str(task.project), 'Тестовый проект')

	def test_list_section_fail(self):
		project = Project.objects.create(title='Тестовый проект', project_type=Project.LIST)
		section = Section.objects.create(title='Тестовая секция', project=project)
		task = Task.objects.create(title='Тестовое задание', section=section, project=project)

		with self.assertRaises(ValidationError):
			task.full_clean()
			task.save()


class TaskTestSection(TestCase):
	'''Тестирование случая без времени выполнения, проект типа секции'''

	def setUp(self):
		project = Project.objects.create(title='Тестовый проект', project_type=Project.SECTIONS)
		section = Section.objects.create(title='Тестовая секция', project=project)
		task = Task.objects.create(title='Тестовое задание', section=section, project=project)

	def test_normal_case(self):
		task = Task.objects.get(title='Тестовое задание')
		self.assertEqual(str(task), 'Тестовое задание')
		self.assertEqual(str(task.section), 'Тестовая секция')
		self.assertEqual(str(task.project), 'Тестовый проект')

	def test_different_section_project_fail(self):
		project1 = Project.objects.create(title='Тестовый проект1', project_type=Project.SECTIONS)
		project2 = Project.objects.create(title='Тестовый проект2', project_type=Project.SECTIONS)
		section = Section.objects.create(title='Тестовая секция', project=project1)
		task = Task.objects.create(title='Тестовое задание', section=section, project=project2)

		with self.assertRaises(ValidationError):
			task.full_clean()
			task.save()

	def test_none_section_fail(self):
		project = Project.objects.create(title='Тестовый проект', project_type=Project.SECTIONS)
		task = Task.objects.create(title='Тестовое задание', project=project)
		
		with self.assertRaises(ValidationError):
			task.full_clean()
			task.save()

class ProjectTest(TestCase):
	'''Тестирование проекта'''

	def test_project_type_fail(self):
		project = Project.objects.create(title='Тестовый проект', project_type=1)

		with self.assertRaises(ValidationError):
			project.full_clean()
			project.save()

class SectionTest(TestCase):
	'''Тестирование секции'''

	def test_section_with_project_list(self):
		'''Тестирование секции с проектом типа лист, тест должен поднять ValidationError'''
		project = Project.objects.create(title='Тестовый проект', project_type=Project.LIST)
		section = Section.objects.create(title='Тестовая секция', project=project)

		with self.assertRaises(ValidationError):
			section.full_clean()
			section.save()

