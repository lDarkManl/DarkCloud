from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from cards.models import Folder, Card
from cards.forms import FolderForm, CardForm

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

class DetailFolder(ListView):
	model = Card
	template_name = 'cards/detail_folder.html'
	context_object_name = 'cards_list'

	def get_queryset(self):
		return Card.objects.filter(folder_id=self.kwargs['pk'])

class CreateCard(CreateView):
	model = Card
	template_name = 'cards/create_card.html'
	form_class = CardForm
	success_url = reverse_lazy('cards:index_folders')

class ChangeCard(UpdateView):
	model = Card
	template_name = 'cards/change_card.html'
	form_class = CardForm
	success_url = reverse_lazy('cards:index_folders')

class DeleteCard(DeleteView):
	model = Card
	template_name = 'cards/delete_card.html'
	success_url = reverse_lazy('cards:index_folders')

class AllCards(ListView):
	model = Card
	template_name = 'cards/all_cards.html'
	context_object_name = 'cards_list'
	
