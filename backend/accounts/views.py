from django.contrib.auth import get_user_model
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from config.permissions import IsAdminRole
from courses.models import Course
from courses.serializers import CourseSerializer
from students.models import StudentProfile
from students.serializers import StudentProfileSerializer
from teachers.models import TeacherProfile
from teachers.serializers import TeacherProfileSerializer
from .serializers import RegisterSerializer, UserSerializer

User = get_user_model()


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "user": UserSerializer(user).data,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            },
            status=status.HTTP_201_CREATED,
        )


class LogoutView(APIView):
    def post(self, request):
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response({"detail": "Refresh token is required."}, status=400)

        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"detail": "Logged out successfully."})


class MeView(APIView):
    def get(self, request):
        return Response(UserSerializer(request.user).data)


class AdminStudentViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.select_related("user", "course")
    serializer_class = StudentProfileSerializer
    permission_classes = [IsAdminRole]


class AdminTeacherViewSet(viewsets.ModelViewSet):
    queryset = TeacherProfile.objects.select_related("user")
    serializer_class = TeacherProfileSerializer
    permission_classes = [IsAdminRole]


class AdminCourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminRole]


@api_view(["GET"])
@permission_classes([IsAdminRole])
def analytics_summary(request):
    return Response(
        {
            "students": StudentProfile.objects.count(),
            "teachers": TeacherProfile.objects.count(),
            "courses": Course.objects.count(),
        }
    )
