from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment_number = models.CharField(max_length=20, unique=True)
    courses = models.ManyToManyField(Course)

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks_obtained = models.FloatField()
    total_marks = models.FloatField()
    date_recorded = models.DateField(auto_now_add=True)

class ProgressTracker(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    improvement_area = models.CharField(max_length=255)
    date_recorded = models.DateField(auto_now_add=True)
