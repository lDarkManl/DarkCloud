from django.test import TestCase, Client
from django.urls import reverse
from notes.models import Note

class NoteViewsTests(TestCase):

	def setUp(self):
		self.client = Client()

	def test_index_view(self):
		response = self.client.get(reverse('notes:index_notes'))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'notes/index_notes.html')

	def test_create_view(self):
		response = self.client.get(reverse('notes:create_note'))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'notes/create_note.html')

	def test_change_view(self):
		note = Note.objects.create(id=1, note_title='Тест', note_text='')
		response = self.client.get(reverse('notes:change_note', args=[1]))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'notes/change_note.html')

	def test_delete_view(self):
		note = Note.objects.create(id=1, note_title='Тест', note_text='')
		response = self.client.get(reverse('notes:delete_note', args=[1]))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'notes/delete_note.html')


