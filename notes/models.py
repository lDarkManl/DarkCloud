from django.db import models
from django.shortcuts import reverse


class Note(models.Model):
	'''Модель заметки'''
	note_title = models.CharField('Название', max_length=255)
	note_text = models.TextField('Текст', blank=True)
	pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
	update_date = models.DateTimeField('Дата обновления', auto_now=True)

	def __str__(self):
		'''Возвращает название статьи при печатании объекта класса'''
		return self.note_title

	def get_absolute_url(self):
		'''Получить url объекта'''
		return reverse('notes:change_note', kwargs={'pk': self.id})

	class Meta:
		verbose_name = 'Заметка'
		verbose_name_plural = 'Заметки'
		ordering = ['-update_date']
	