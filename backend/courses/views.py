from rest_framework import viewsets

from config.permissions import IsTeacherOrAdmin
from .models import Course, VideoLecture
from .serializers import CourseSerializer, VideoLectureSerializer


class VideoLectureTeacherViewSet(viewsets.ModelViewSet):
    serializer_class = VideoLectureSerializer
    permission_classes = [IsTeacherOrAdmin]

    def get_queryset(self):
        queryset = VideoLecture.objects.all().select_related("course", "uploaded_by")
        if self.request.user.role == "teacher":
            return queryset.filter(uploaded_by=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)
