from django.conf import settings
from django.db import models

from courses.models import Course


class AttendanceRecord(models.Model):
    class Status(models.TextChoices):
        PRESENT = "present", "Present"
        ABSENT = "absent", "Absent"

    student = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="attendance_records", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name="attendance_records", on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PRESENT)
    marked_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="marked_attendance_records",
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        unique_together = ("student", "course", "date")

    def __str__(self):
        return f"{self.student.username} - {self.date}"
