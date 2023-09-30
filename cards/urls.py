from django.urls import path
from cards import views

app_name = 'cards'

urlpatterns = [
	path('', views.IndexFolders.as_view(), name='index_folders'),
	path('change_folder/<int:pk>/', views.ChangeFolder.as_view(), name='change_folder'),
	path('create_folder/', views.CreateFolder.as_view(), name='create_folder'),
	path('delete_folder/<int:pk>/', views.DeleteFolder.as_view(), name='delete_folder'),
]

