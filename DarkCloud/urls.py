from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from DarkCloud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('notes/', include(('notes.urls'), namespace='notes')),
    path('todo/', include(('todo.urls'), namespace='todo')),
    path('cards/', include(('cards.urls'), namespace='cards')),
    path('chaining/', include('smart_selects.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

