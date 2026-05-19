from django.conf import settings
from django.db import models

from courses.models import Course


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, related_name="quizzes", on_delete=models.CASCADE)
    total_marks = models.PositiveIntegerField(default=100)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="created_quizzes", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class QuizAttempt(models.Model):
    quiz = models.ForeignKey(Quiz, related_name="attempts", on_delete=models.CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="quiz_attempts", on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    attempted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("quiz", "student")

    def __str__(self):
        return f"{self.quiz.title} - {self.student.username}"
