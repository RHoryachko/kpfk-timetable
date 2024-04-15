from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Subject, Teacher, Group, Specialty, Lesson, Exam
from rest_framework.generics import RetrieveAPIView
from .serializers import SubjectSerializer, TeacherSerializer
from .serializers import GroupSerializer, SpecialtySerializer
from .serializers import LessonSerializer, ExamSerializer

class SubjectListAPIView(APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

class TeacherListAPIView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

class GroupListAPIView(APIView):
    def get(self, request):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

class SpecialtyListAPIView(APIView):
    def get(self, request):
        specialties = Specialty.objects.all()
        serializer = SpecialtySerializer(specialties, many=True)
        return Response(serializer.data)

class LessonListAPIView(APIView):
    def get(self, request):
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)

class ExamListAPIView(APIView):
    def get(self, request):
        exams = Exam.objects.all()
        serializer = ExamSerializer(exams, many=True)
        return Response(serializer.data)


class SpecialtyGroupsAPIView(APIView):
    def get(self, request, specialty_id):
        groups = Group.objects.filter(specialty_id=specialty_id)
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

class SpecialtyCoursesGroupsAPIView(APIView):
    def get(self, request, specialty_id, course):
        groups = Group.objects.filter(specialty_id=specialty_id, course=course)
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

class TeacherLessonsAPIView(APIView):
    def get(self, request, teacher_id):
        lessons = Lesson.objects.filter(teacher_id=teacher_id)
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)

class TeacherExamsAPIView(APIView):
    def get(self, request, teacher_id):
        exams = Exam.objects.filter(teacher_id=teacher_id)
        serializer = ExamSerializer(exams, many=True)
        return Response(serializer.data)

class GroupLessonsAPIView(APIView):
    def get(self, request, group_id):
        lessons = Lesson.objects.filter(group_id=group_id)
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)

class GroupNumeratorSubgroupLessonsAPIView(APIView):
    def get(self, request, group_id, numerator, subgroup):
        lessons = Lesson.objects.filter(group_id=group_id, numerator=numerator, subgroup=subgroup)
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)

class GroupExamsAPIView(APIView):
    def get(self, request, group_id):
        exams = Exam.objects.filter(group_id=group_id)
        serializer = ExamSerializer(exams, many=True)
        return Response(serializer.data)


class SubjectDetailAPIView(RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class TeacherDetailAPIView(RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class GroupDetailAPIView(RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class SpecialtyDetailAPIView(RetrieveAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer

class LessonDetailAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class ExamDetailAPIView(RetrieveAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
