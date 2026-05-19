from django.conf import settings
from django.db import models


class TeacherProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="teacher_profile", on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username
