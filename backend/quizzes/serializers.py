from rest_framework import serializers

from .models import Quiz, QuizAttempt


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = "__all__"
        read_only_fields = ("created_by", "created_at")


class QuizAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAttempt
        fields = "__all__"
