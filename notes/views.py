from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from notes.models import Note
from notes.forms import NoteForm
from DarkCloud.services import slugify

class IndexNotes(ListView):
	'''Вывести все заметки'''
	model = Note
	template_name = 'notes/index_notes.html'
	context_object_name = 'notes_list'

class ChangeNote(UpdateView):
	'''Просмотреть и изменить заметку'''
	model = Note
	template_name = 'notes/change_note.html'
	form_class = NoteForm

class DeleteNote(DeleteView):
	'''Удалить заметку'''
	model = Note
	template_name = 'notes/delete_note.html'
	success_url = reverse_lazy('notes:index_notes')

class CreateNote(CreateView):
	'''Создать заметку'''
	model = Note
	template_name = 'notes/create_note.html'
	form_class = NoteForm

	def form_valid(self, form):
		form.instance.note_slug = slugify(form.instance.note_title)
		return super().form_valid(form)