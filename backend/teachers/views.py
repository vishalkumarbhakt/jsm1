from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from assignments.models import Assignment, AssignmentSubmission
from assignments.serializers import AssignmentSerializer, AssignmentSubmissionSerializer
from attendance.models import AttendanceRecord
from attendance.serializers import AttendanceRecordSerializer
from config.permissions import IsTeacherOrAdmin
from quizzes.models import Quiz
from quizzes.serializers import QuizSerializer
from students.models import Note
from students.serializers import NoteSerializer


class TeacherNoteCreateView(generics.CreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsTeacherOrAdmin]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)


class TeacherAssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    permission_classes = [IsTeacherOrAdmin]

    def get_queryset(self):
        queryset = Assignment.objects.select_related("course", "teacher")
        if self.request.user.role == "teacher":
            return queryset.filter(teacher=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


class MarkAttendanceView(generics.CreateAPIView):
    serializer_class = AttendanceRecordSerializer
    permission_classes = [IsTeacherOrAdmin]

    def perform_create(self, serializer):
        serializer.save(marked_by=self.request.user)


class EvaluateSubmissionView(generics.UpdateAPIView):
    queryset = AssignmentSubmission.objects.select_related("assignment", "student")
    serializer_class = AssignmentSubmissionSerializer
    permission_classes = [IsTeacherOrAdmin]

    def patch(self, request, *args, **kwargs):
        submission = self.get_object()
        submission.score = request.data.get("score", submission.score)
        submission.feedback = request.data.get("feedback", submission.feedback)
        submission.status = "evaluated"
        submission.save(update_fields=["score", "feedback", "status"])
        return Response(self.get_serializer(submission).data, status=status.HTTP_200_OK)


class TeacherQuizViewSet(viewsets.ModelViewSet):
    serializer_class = QuizSerializer
    permission_classes = [IsTeacherOrAdmin]

    def get_queryset(self):
        queryset = Quiz.objects.select_related("course", "created_by")
        if self.request.user.role == "teacher":
            return queryset.filter(created_by=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class StudentProgressTracker(APIView):
    permission_classes = [IsTeacherOrAdmin]

    def get(self, request):
        submissions = AssignmentSubmission.objects.select_related("student", "assignment")[:20]
        return Response(
            {
                "evaluated_submissions": AssignmentSubmission.objects.filter(status="evaluated").count(),
                "recent_submissions": AssignmentSubmissionSerializer(submissions, many=True).data,
            }
        )
