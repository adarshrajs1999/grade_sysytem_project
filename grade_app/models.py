from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User_model(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


class Teacher(models.Model):
    user = models.ForeignKey(User_model,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
     

class Student(models.Model):
    user = models.ForeignKey(User_model,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    student_id = models.IntegerField(blank=True,null=True)
    bio = models.TextField()


class Course(models.Model):
    course_code = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.TextField()


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=2)
    year = models.DateField()

    




