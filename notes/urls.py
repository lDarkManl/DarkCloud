from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
	path('', views.IndexNotes.as_view(), name='index_notes'),
	path('create_note/', views.CreateNote.as_view(), name='create_note'),
	path('note/<int:pk>/', views.ChangeNote.as_view(), name='change_note'),
	path('delete_note/<int:pk>/', views.DeleteNote.as_view(), name='delete_note'),
]