from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet, TeacherViewSet, GroupViewSet, LessonViewSet

router = DefaultRouter()
router.register(r'subjects', SubjectViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'lessons', LessonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
