from django.contrib import admin
from .models import Subject, Teacher
from .models import Group, Lesson
from .models import Specialty, Exam

# Register your models here.
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Lesson)
admin.site.register(Specialty)
admin.site.register(Exam)