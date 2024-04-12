from django.db import models
from django.core.exceptions import ValidationError

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предмети"


class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вчитель"
        verbose_name_plural = "Вчителі"


class Group(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    course = models.IntegerField()

    def clean(self):
        if not 1 <= self.course <= 4:
            raise ValidationError({'course': 'Курс повинен бути в діапазоні від 1 до 4.'})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Група"
        verbose_name_plural = "Групи"


class Lesson(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)  
    room = models.CharField(max_length=20)
    numerator = models.BooleanField()  
    subgroup = models.IntegerField(default=1)  

    def __str__(self):
        return f"{self.subject} - {self.teacher} ({self.group})"

    class Meta:
        verbose_name = "Заняття"
        verbose_name_plural = "Заняття"
