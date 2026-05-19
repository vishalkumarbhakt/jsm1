from django.conf import settings
from django.db import models


class Notification(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="notifications",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
