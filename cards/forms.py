from django.forms import ModelForm
from cards.models import Folder

class FolderForm(ModelForm):
	class Meta:
		model = Folder
		fields = ('title',)

