from django.db import models

# Create your models here.

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=2, default=20, null = False)
    address = models.CharField(max_length=500)
    phone_no = models.CharField(max_length=15)
    height = models.IntegerField(default = 2, null = True)


class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    level = models.CharField(max_length=100)
    students = models.IntegerField()

