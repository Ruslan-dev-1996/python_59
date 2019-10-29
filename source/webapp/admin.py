from django.contrib import admin
from webapp.models import Tracker, Status, Type, Project

admin.site.register(Tracker)
admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Project)
