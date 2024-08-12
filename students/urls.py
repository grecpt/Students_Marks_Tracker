from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, CourseViewSet, MarksViewSet, ProgressTrackerViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'marks', MarksViewSet)
router.register(r'progress', ProgressTrackerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]