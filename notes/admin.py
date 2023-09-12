from django.contrib import admin
from notes.models import Note

class NoteAdmin(admin.ModelAdmin):
	list_display = ('id', 'note_title', 'pub_date', 'update_date')
	list_display_links = ('note_title',)
	search_fields = ('note_title',)

admin.site.register(Note, NoteAdmin)