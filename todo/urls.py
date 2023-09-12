from django.urls import path
from todo import views

app_name = 'todo'
urlpatterns = [
	path('today/', views.today_view, name='today'),
	path('project/<int:pk>/', views.project_view, name='project'),
	path('all/', views.all_view, name='all'),
	path('calendar/', views.calendar, name='calendar'),
	path('calendar/<int:year>/<int:month>/', views.calendar_main, name='calendar_main'),
	path('next_calendar/<int:year>/<int:month>/', views.next_calendar, name='next_calendar'),
	path('prev_calendar/<int:year>/<int:month>/', views.prev_calendar, name='prev_calendar'),
	path('completed/', views.completed, name='completed'),
	path('change_task/<int:pk>/', views.create_or_update_task, name='change_task'),
	path('create_task/', views.create_or_update_task, name='create_task'),
	path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
	path('change_status/<int:pk>/', views.change_status_task, name='change_status'),
	path('change_section/<int:pk>/', views.create_or_update_section, name='change_section'),
	path('create_section/', views.create_or_update_section, name='create_section'),
	path('delete_section/<int:pk>/', views.delete_section, name='delete_section'),
	path('create_project/', views.create_or_update_project, name='create_project'),
	path('change_project/<int:pk>/', views.create_or_update_project, name='change_project'),
	path('delete_project/<int:pk>/', views.delete_project, name='delete_project'),
	path('<int:year>/<int:month>/<int:day>/', views.date_view, name='date'),
]