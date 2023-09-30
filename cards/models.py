from django.db import models
from django.shortcuts import reverse		

class Folder(models.Model):
	title = models.CharField(max_length=255)
	# cards = models.FileField(upload_to='uploads/')
	pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

	def __str__(self):
		return self.title
		
	def get_absolute_url(self):
		'''Получить url к папке'''
		return reverse('cards:folder', kwargs={'pk': self.id})
	
	class Meta:
		verbose_name = 'Папка'
		verbose_name_plural = 'Папки'		