import os
from django.db import models
from django.shortcuts import reverse	
from django.core.files.base import ContentFile	

class Folder(models.Model):
	title = models.CharField('Название папки', max_length=255)
	cards = models.FileField('Карточки', upload_to='uploads/', blank=True)
	pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

	def __str__(self):
		return self.title
		
	def get_absolute_url(self):
		'''Получить url к папке'''
		return reverse('cards:folder', kwargs={'pk': self.id})
	
	class Meta:
		verbose_name = 'Папка'
		verbose_name_plural = 'Папки'	

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		

	def delete(self, *args, **kwargs):
		os.remove(self.cards.path)
		super().delete(*args, **kwargs)