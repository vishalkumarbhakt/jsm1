from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    EvaluateSubmissionView,
    MarkAttendanceView,
    StudentProgressTracker,
    TeacherAssignmentViewSet,
    TeacherNoteCreateView,
    TeacherQuizViewSet,
)

router = DefaultRouter()
router.register(r"assignments", TeacherAssignmentViewSet, basename="teacher-assignments")
router.register(r"quizzes", TeacherQuizViewSet, basename="teacher-quizzes")

urlpatterns = [
    *router.urls,
    path("notes/upload/", TeacherNoteCreateView.as_view(), name="teacher-upload-note"),
    path("attendance/mark/", MarkAttendanceView.as_view(), name="teacher-mark-attendance"),
    path(
        "assignments/submissions/<int:pk>/evaluate/",
        EvaluateSubmissionView.as_view(),
        name="teacher-evaluate-submission",
    ),
    path("progress/", StudentProgressTracker.as_view(), name="teacher-student-progress"),
]
