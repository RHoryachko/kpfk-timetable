from django.urls import path
from .views import SubjectListAPIView, TeacherListAPIView
from .views import SpecialtyGroupsAPIView, SpecialtyCoursesGroupsAPIView, SpecialtyCoursesGroupsAPIView
from .views import TeacherLessonsAPIView, TeacherExamsAPIView
from .views import GroupLessonsAPIView, GroupNumeratorSubgroupLessonsAPIView
from .views import GroupExamsAPIView, SubjectDetailAPIView
from .views import TeacherDetailAPIView, GroupDetailAPIView
from .views import SpecialtyDetailAPIView, LessonDetailAPIView
from .views import ExamDetailAPIView
from .views import GroupListAPIView, SpecialtyListAPIView
from .views import LessonListAPIView, ExamListAPIView

urlpatterns = [
    path('subjects/', SubjectListAPIView.as_view(), name='subject-list'),
    path('teachers/', TeacherListAPIView.as_view(), name='teacher-list'),
    path('groups/', GroupListAPIView.as_view(), name='group-list'),
    path('specialties/', SpecialtyListAPIView.as_view(), name='specialty-list'),
    path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
    path('exams/', ExamListAPIView.as_view(), name='exam-list'),
    path('specialties/<int:specialty_id>/groups/', SpecialtyGroupsAPIView.as_view(), 
                                                    name='specialty-groups'),
    path('specialties/<int:specialty_id>/groups/<int:course>/', 
                SpecialtyCoursesGroupsAPIView.as_view(), name='specialty-course-groups'),
    path('teachers/<int:teacher_id>/lessons/', TeacherLessonsAPIView.as_view(), 
                                                        name='teacher-lessons'),
    path('teachers/<int:teacher_id>/exams/', TeacherExamsAPIView.as_view(), name='teacher-exams'),
    path('groups/<int:group_id>/lessons/', GroupLessonsAPIView.as_view(), name='group-lessons'),
    path('groups/<int:group_id>/lessons/<str:numerator>/<int:subgroup>/', 
            GroupNumeratorSubgroupLessonsAPIView.as_view(), name='group-nsg-lessons'),
    path('groups/<int:group_id>/exams/', GroupExamsAPIView.as_view(), name='group-exams'),
    path('subjects/<int:pk>/', SubjectDetailAPIView.as_view(), name='subject-detail'),
    path('teachers/<int:pk>/', TeacherDetailAPIView.as_view(), name='teacher-detail'),
    path('groups/<int:pk>/', GroupDetailAPIView.as_view(), name='group-detail'),
    path('specialties/<int:pk>/', SpecialtyDetailAPIView.as_view(), name='specialty-detail'),
    path('lessons/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson-detail'),
    path('exams/<int:pk>/', ExamDetailAPIView.as_view(), name='exam-detail'),
]


