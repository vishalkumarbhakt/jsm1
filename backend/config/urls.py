from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from accounts.views import (
    AdminCourseViewSet,
    AdminStudentViewSet,
    AdminTeacherViewSet,
    analytics_summary,
)

admin_router = DefaultRouter()
admin_router.register(r"students", AdminStudentViewSet, basename="admin-students")
admin_router.register(r"teachers", AdminTeacherViewSet, basename="admin-teachers")
admin_router.register(r"courses", AdminCourseViewSet, basename="admin-courses")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("accounts.urls")),
    path("api/students/", include("students.urls")),
    path("api/teachers/", include("teachers.urls")),
    path("api/teacher-content/", include("courses.urls")),
    path("api/payments/", include("payments.urls")),
    path("api/admin/", include(admin_router.urls)),
    path("api/admin/analytics/", analytics_summary, name="admin-analytics"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
