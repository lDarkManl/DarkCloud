from django.test import TestCase
from cards.models import Folder, Card
from django.core.exceptions import ValidationError

class CardFolderTest(TestCase):
	'''Тестирование обычного случая'''

	def setUp(self):
		self.folder = Folder.objects.create(title='Тестовая папка')
		self.card = Card.objects.create(front='Тест фронт', back='Тест бэк', folder=self.folder)
		self.id_card = self.card.id
		self.id_folder = self.folder.id

	def test_card_case(self):
		card = Card.objects.get(id=self.id_card)
		self.assertEqual(str(card), 'Тест фронт')
		

	def test_folder_case(self):
		folder = Folder.objects.get(id=self.id_folder)
		self.assertEqual(str(folder), 'Тестовая папка')

	