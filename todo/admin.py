from django.contrib import admin
from todo.models import Task, Section, Project

admin.site.register(Task)
admin.site.register(Section)
admin.site.register(Project)
