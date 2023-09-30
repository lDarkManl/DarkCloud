from django.urls import path
from cards import views

app_name = 'cards'

urlpatterns = [
	path('', views.IndexFolders.as_view(), name='index_folders'),
	path('change_folder/<int:pk>/', views.ChangeFolder.as_view(), name='change_folder'),
	path('create_folder/', views.CreateFolder.as_view(), name='create_folder'),
	path('delete_folder/<int:pk>/', views.DeleteFolder.as_view(), name='delete_folder'),
	path('folder/<int:pk>/', views.DetailFolder.as_view(), name='folder'),
	path('create_card/', views.CreateCard.as_view(), name='create_card'),
	path('change_card/<int:pk>/', views.ChangeCard.as_view(), name='change_card'),
	path('delete_card/<int:pk>/', views.DeleteCard.as_view(), name='delete_card'),
	path('all/', views.AllCards.as_view(), name='all_cards'),
]

