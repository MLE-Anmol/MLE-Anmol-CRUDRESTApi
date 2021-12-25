from django.db import models

# Create your models here.
class Student(models.Model):
    stu_name = models.CharField(max_length=20)
    stu_id = models.CharField(max_length=10)
    Course = models.CharField(max_length=10)