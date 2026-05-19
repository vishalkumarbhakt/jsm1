from rest_framework import serializers

from .models import Note, StudentProfile


class StudentProfileSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = StudentProfile
        fields = ("id", "user", "user_name", "course", "roll_number", "attendance_percentage")


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"
        read_only_fields = ("uploaded_by", "created_at")
