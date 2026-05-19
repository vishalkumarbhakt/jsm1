from rest_framework import serializers

from .models import Course, VideoLecture


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class VideoLectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLecture
        fields = "__all__"
        read_only_fields = ("uploaded_by", "created_at")
