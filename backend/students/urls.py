from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    AssignmentSubmitView,
    AttendanceView,
    ProgressReportView,
    StudentNoteViewSet,
    StudentNotificationView,
    StudentPaymentView,
    StudentQuizAttemptView,
    StudentQuizViewSet,
    StudentVideoViewSet,
)

router = DefaultRouter()
router.register(r"notes", StudentNoteViewSet, basename="student-notes")
router.register(r"videos", StudentVideoViewSet, basename="student-videos")
router.register(r"quizzes", StudentQuizViewSet, basename="student-quizzes")

urlpatterns = [
    *router.urls,
    path("assignments/submit/", AssignmentSubmitView.as_view(), name="assignment-submit"),
    path("quizzes/attempt/", StudentQuizAttemptView.as_view(), name="quiz-attempt"),
    path("attendance/", AttendanceView.as_view(), name="attendance-view"),
    path("progress/", ProgressReportView.as_view(), name="progress-report"),
    path("notifications/", StudentNotificationView.as_view(), name="student-notifications"),
    path("payments/", StudentPaymentView.as_view(), name="student-payments"),
]
