from django.db import models
from django.shortcuts import reverse

class Card(models.Model):
	front = models.CharField(max_length=255)
	back = models.CharField(max_length=255)
	pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
	folder = models.ForeignKey('Folder', on_delete=models.CASCADE, verbose_name='Папка', related_name='card')

	def __str__(self):
		return self.front

	class Meta:
		verbose_name = 'Карточка'
		verbose_name_plural = 'Карточки'		

class Folder(models.Model):
	title = models.CharField(max_length=255)
	pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

	def __str__(self):
		return self.title
		
	def get_absolute_url(self):
		'''Получить url к папке'''
		return reverse('cards:folder', kwargs={'pk': self.id})
	
	class Meta:
		verbose_name = 'Папка'
		verbose_name_plural = 'Папки'		