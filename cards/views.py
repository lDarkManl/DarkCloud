from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.core.files.base import ContentFile
from cards.models import Folder
from django.http import HttpResponseRedirect, FileResponse
from cards.forms import FolderForm, CardForm, ImportFolderForm
from cards import services

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

	def post(self, request, *args, **kwargs):
		form = FolderForm(request.POST)
		if form.is_valid():
			folder = form.save()
			folder.cards.save(f'{folder.id}.csv', ContentFile(''))
			return HttpResponseRedirect(reverse('cards:folder', args=(folder.id,)))
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class ImportFolder(CreateView):
	'''Импортировать папку'''
	model = Folder
	template_name = 'cards/import_folder.html'
	form_class = ImportFolderForm
	success_url = reverse_lazy('cards:index_folders')

def folder(request, pk):
	'''Вывести содержимое папки'''
	folder = get_object_or_404(Folder, pk=pk)
	cards_list = services.get_cards_from_folder(folder)
	form = FolderForm
	context = {}
	context['cards_list'] = cards_list
	context['id'] = folder.id
	context['form'] = form

	return render(request, 'cards/folder.html', context)

def change_cards(request, pk):
	'''View для изменения карточек'''
	if request.method == 'POST':
		return change_cards_post(request, pk)
	else:
		return change_cards_get(request, pk)

def change_cards_post(request, pk):
	folder = get_object_or_404(Folder, pk=pk)
	form = CardForm(request.POST)
	cards_list = services.serialize_cards(form, folder)
	services.write_cards_in_folder(cards_list, folder)
	return HttpResponseRedirect(reverse('cards:folder', args=[folder.id]))

def change_cards_get(request, pk):
	folder = get_object_or_404(Folder, pk=pk)
	cards_list = services.get_cards_from_folder(folder)
	card_form = services.write_cards_in_form(cards_list, CardForm)

	context = {}
	context['form'] = card_form
	context['id'] = folder.id

	return render(request, 'cards/change_cards.html', context)

def export_folder(request, pk):
	'''Экспортировать папку'''
	folder = get_object_or_404(Folder, pk=pk)
	filename = folder.cards.path
	response = FileResponse(open(filename, 'rb'))
	return response

def choose_cards(request):
	'''Выбрать карточки и создать отдельную папку с ними'''
	if request.method == 'POST':
		cards_list = request.POST.getlist('card')
		title = request.POST['title']
		folder = Folder.objects.create(title=title)
		folder.cards.save(f'{folder.id}.csv', ContentFile(''))
		services.write_cards_in_folder(cards_list, folder)
		return HttpResponseRedirect(reverse('cards:folder', args=(folder.id,)))
	return HttpResponseRedirect(reverse('cards:index_folders'))