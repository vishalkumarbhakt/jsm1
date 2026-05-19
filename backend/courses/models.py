from django.conf import settings
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name


class VideoLecture(models.Model):
    course = models.ForeignKey(Course, related_name="video_lectures", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_url = models.URLField(blank=True)
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="uploaded_videos",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
