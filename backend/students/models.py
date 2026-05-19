from django.conf import settings
from django.db import models

from courses.models import Course


class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="student_profile", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    roll_number = models.CharField(max_length=50, blank=True)
    attendance_percentage = models.FloatField(default=0)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Note(models.Model):
    course = models.ForeignKey(Course, related_name="notes", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="notes/")
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
