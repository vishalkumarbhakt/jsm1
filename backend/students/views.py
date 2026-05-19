from django.db.models import Avg
from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from assignments.models import AssignmentSubmission
from assignments.serializers import AssignmentSubmissionSerializer
from attendance.models import AttendanceRecord
from attendance.serializers import AttendanceRecordSerializer
from courses.models import VideoLecture
from courses.serializers import VideoLectureSerializer
from notifications.models import Notification
from notifications.serializers import NotificationSerializer
from payments.models import Payment
from payments.serializers import PaymentSerializer
from quizzes.models import Quiz, QuizAttempt
from quizzes.serializers import QuizAttemptSerializer, QuizSerializer
from .models import Note, StudentProfile
from .serializers import NoteSerializer


class StudentNoteViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Note.objects.select_related("course", "uploaded_by")
        if self.request.user.role == "student" and hasattr(self.request.user, "student_profile"):
            course_id = self.request.user.student_profile.course_id
            if course_id:
                return queryset.filter(course_id=course_id)
        return queryset


class StudentVideoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = VideoLectureSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = VideoLecture.objects.select_related("course", "uploaded_by")
        if self.request.user.role == "student" and hasattr(self.request.user, "student_profile"):
            course_id = self.request.user.student_profile.course_id
            if course_id:
                return queryset.filter(course_id=course_id)
        return queryset




class StudentQuizViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Quiz.objects.select_related("course", "created_by")
        if self.request.user.role == "student" and hasattr(self.request.user, "student_profile"):
            course_id = self.request.user.student_profile.course_id
            if course_id:
                return queryset.filter(course_id=course_id)
        return queryset


class StudentQuizAttemptView(generics.CreateAPIView):
    serializer_class = QuizAttemptSerializer

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)


class AssignmentSubmitView(generics.CreateAPIView):
    serializer_class = AssignmentSubmissionSerializer

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)


class AttendanceView(generics.ListAPIView):
    serializer_class = AttendanceRecordSerializer

    def get_queryset(self):
        return AttendanceRecord.objects.filter(student=self.request.user).select_related("course", "marked_by")


class StudentNotificationView(generics.ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(recipient__in=[self.request.user, None]).order_by("-created_at")


class StudentPaymentView(generics.ListAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return Payment.objects.filter(student=self.request.user).order_by("-created_at")


class ProgressReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        attempts = QuizAttempt.objects.filter(student=request.user)
        attendance_count = AttendanceRecord.objects.filter(student=request.user, status="present").count()
        total_attendance = AttendanceRecord.objects.filter(student=request.user).count() or 1
        avg_score = attempts.aggregate(avg=Avg("score")).get("avg") or 0
        return Response(
            {
                "average_quiz_score": avg_score,
                "attendance_percentage": round((attendance_count / total_attendance) * 100, 2),
                "submitted_assignments": AssignmentSubmission.objects.filter(student=request.user).count(),
            },
            status=status.HTTP_200_OK,
        )
