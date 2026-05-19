from django.contrib import admin

from .models import Note, StudentProfile

admin.site.register(StudentProfile)
admin.site.register(Note)
