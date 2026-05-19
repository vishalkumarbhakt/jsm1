from rest_framework.routers import DefaultRouter

from .views import VideoLectureTeacherViewSet

router = DefaultRouter()
router.register(r"videos", VideoLectureTeacherViewSet, basename="teacher-videos")

urlpatterns = router.urls
