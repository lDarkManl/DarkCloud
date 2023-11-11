from django.urls import path
from cards import views

app_name = 'cards'

urlpatterns = [
	path('', views.IndexFolders.as_view(), name='index_folders'),
	path('change_folder/<int:pk>/', views.ChangeFolder.as_view(), name='change_folder'),
	path('create_folder/', views.CreateFolder.as_view(), name='create_folder'),
	path('delete_folder/<int:pk>/', views.DeleteFolder.as_view(), name='delete_folder'),
	path('folder/<int:pk>/', views.folder, name='folder'),
	path('change_cards/<int:pk>/', views.change_cards, name='change_cards'),
	path('import_folder/', views.ImportFolder.as_view(), name='import_folder'),
	path('export_folder/<int:pk>/', views.export_folder, name='export_folder'),
	path('choose_cards/', views.choose_cards, name='choose_cards'),
]

