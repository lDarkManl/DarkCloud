from django import forms
from cards.models import Folder

class FolderForm(forms.ModelForm):
	class Meta:
		model = Folder
		fields = ('title',)

class ImportFolderForm(forms.ModelForm):
	class Meta:
		model = Folder
		fields = ('title', 'cards')

class CardForm(forms.Form):
	file_text = forms.CharField(widget=forms.Textarea())
	

