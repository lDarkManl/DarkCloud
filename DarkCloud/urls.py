from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cloud/', include(('cloud.urls'), namespace='cloud')),
    path('notes/', include(('notes.urls'), namespace='notes')),
    path('todo/', include(('todo.urls'), namespace='todo')),
    path('chaining/', include('smart_selects.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

