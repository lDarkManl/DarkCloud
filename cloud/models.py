from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from sizefield.models import FileSizeField

class File(models.Model):
	'''Модель файла'''
	author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='file_author')
	file_name = models.CharField('Имя файла', max_length=255)
	file_path = models.FileField('Файл', upload_to='files/%Y/%m/%d/')
	pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
	file_folder = models.ForeignKey('Folder', on_delete=models.CASCADE, verbose_name='Файл', related_name='file_folder')
	file_size = FileSizeField()

	class Meta:
		verbose_name = 'Файл'
		verbose_name_plural = 'Файлы'
		ordering = ['-pub_date']

	def __str__(self):
		'''Возвращает название файла при печатании объекта класса'''
		return self.file_name

class Folder(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='file')
	folder_name = models.CharField('Имя папки', max_length=255)

	def __str__(self):
		'''Возвращает название папки при печатании объекта класса'''
		return self.folder_name

	class Meta:
		verbose_name = 'Папка'
		verbose_name_plural = 'Папки'
		ordering = ['folder_name']

	@property
	def folder_size(self):
		return sum((file.file_size for file in self.file.all()))