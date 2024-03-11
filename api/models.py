from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)

class Teacher(models.Model):
    name = models.CharField(max_length=100)

class Group(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    course = models.IntegerField()

class Lesson(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)  
    room = models.CharField(max_length=20)
    numerator = models.BooleanField()  
    subgroup = models.IntegerField(default=1)  
