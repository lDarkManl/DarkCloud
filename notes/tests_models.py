from django.test import TestCase
from notes.models import Note

class NoteModelTests(TestCase):

	def test_normal_case(self):
		note = Note.objects.create(note_title='Тест', note_text='')
		self.assertEquals(str(note), 'Тест')

	def test_get_absolute_url(self):
		note = Note.objects.create(note_title='Тест', note_text='')
		self.assertEquals(note.get_absolute_url(), '/notes/note/1/') 