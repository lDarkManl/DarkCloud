from django.test import TestCase, Client
from django.urls import reverse
from todo.models import Task, Section, Project

class TestViews(TestCase):

	def setUp(self):
		self.client = Client()

	def test_all_view(self):
		response = self.client.get(reverse('todo:all'))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'todo/all.html')

	def test_project_view(self):
		project = Project.objects.create(id=1, title='test')
		response = self.client.get(reverse('todo:project', args=[1]))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'todo/project.html')

	def test_completed_view(self):
		response = self.client.get(reverse('todo:completed'))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'todo/completed.html')

	def test_today_view(self):
		response = self.client.get(reverse('todo:today'))

		self.assertEquals(response.status_code, 302)

	def test_date_view(self):
		response = self.client.get(reverse('todo:date', args=[2023, 9, 1]))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'todo/date.html')

	def test_calendar_view(self):
		response = self.client.get(reverse('todo:calendar'))

		self.assertEquals(response.status_code, 302)

	def test_next_calendar_view(self):
		response = self.client.get(reverse('todo:next_calendar', args=[2023, 9]))

		self.assertEquals(response.status_code, 302)

	def test_prev_calendar_view(self):
		response = self.client.get(reverse('todo:prev_calendar', args=[2023, 9]))

		self.assertEquals(response.status_code, 302)

