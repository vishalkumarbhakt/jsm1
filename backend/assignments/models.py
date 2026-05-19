from django.conf import settings
from django.db import models

from courses.models import Course


class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    course = models.ForeignKey(Course, related_name="assignments", on_delete=models.CASCADE)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="teacher_assignments", on_delete=models.CASCADE)
    due_date = models.DateField(null=True, blank=True)
    attachment = models.FileField(upload_to="assignments/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class AssignmentSubmission(models.Model):
    class Status(models.TextChoices):
        SUBMITTED = "submitted", "Submitted"
        EVALUATED = "evaluated", "Evaluated"

    assignment = models.ForeignKey(Assignment, related_name="submissions", on_delete=models.CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="assignment_submissions", on_delete=models.CASCADE)
    file = models.FileField(upload_to="assignment_submissions/")
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.SUBMITTED)
    score = models.FloatField(default=0)
    feedback = models.TextField(blank=True)

    class Meta:
        unique_together = ("assignment", "student")

    def __str__(self):
        return f"{self.assignment.title} - {self.student.username}"
