from rest_framework import viewsets
from .models import Subject, Teacher, Group
from .models import Specialty, Lesson
from .serializers import SubjectSerializer, TeacherSerializer
from .serializers import GroupSerializer, LessonSerializer

# Create your views here.
class SpecialtyViewSet(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SubjectSerializer

    def groups_by_specialty(self, request, specialty_id):
        groups = Group.objects.filter(specialty_id=specialty_id)
        serializer = self.get_serializer(groups, many=True)
        return Response(serializer.data)

    def groups_by_specialty_and_course(self, request, specialty_id, course):
        groups = Group.objects.filter(specialty_id=specialty_id, course=course)
        serializer = self.get_serializer(groups, many=True)
        return Response(serializer.data)


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def lessons_for_teacher(self, request, teacher_id):
        lessons = Lesson.objects.filter(teacher_id=teacher_id)
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def lessons_for_group(self, request, group_id):
        lessons = Lesson.objects.filter(group_id=group_id)
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)

    def lessons_for_group_numerator_and_subgroup(self, request, group_id, numerator, subgroup):
        lessons = Lesson.objects.filter(
        	group_id=group_id, 
        	numerator=numerator, 
        	subgroup=subgroup
		)
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    

