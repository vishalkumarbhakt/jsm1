from rest_framework import serializers

from .models import TeacherProfile


class TeacherProfileSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = TeacherProfile
        fields = ("id", "user", "user_name", "subject", "qualification")
