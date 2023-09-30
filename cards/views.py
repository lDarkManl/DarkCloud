from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from cards.models import Folder
from cards.forms import FolderForm

class IndexFolders(ListView):
	'''Вывести все папки'''
	model = Folder
	template_name = 'cards/index_folders.html'
	context_object_name = 'folders_list'

class ChangeFolder(UpdateView):
	'''Просмотреть и изменить папку'''
	model = Folder
	template_name = 'cards/change_folder.html'
	form_class = FolderForm
	success_url = reverse_lazy('cards:index_folders')

class DeleteFolder(DeleteView):
	'''Удалить папку'''
	model = Folder
	template_name = 'cards/delete_folder.html'
	success_url = reverse_lazy('cards:index_folders')

class CreateFolder(CreateView):
	'''Создать папку'''
	model = Folder
	template_name = 'cards/create_folder.html'
	form_class = FolderForm
	success_url = reverse_lazy('cards:index_folders')
