from django.forms import ModelForm
from cards.models import Folder, Card

class FolderForm(ModelForm):
	class Meta:
		model = Folder
		fields = ('title',)

class CardForm(ModelForm):
	class Meta:
		model = Card
		fields = ('front', 'back', 'folder')
