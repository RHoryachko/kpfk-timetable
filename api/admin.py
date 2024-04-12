from django.contrib import admin
from .models import Subject, Teacher
from .models import Group, Lesson

# Register your models here.
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Lesson)