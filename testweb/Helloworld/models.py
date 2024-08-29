from django.db import models

# Create your models here.
class Person(models.Model):

    name = models.CharField(max_length=20,verbose_name='姓名')

    age = models.IntegerField(verbose_name='年龄')

    score = models.FloatField(verbose_name="成绩")

    sex = models.CharField(max_length=2,verbose_name="性别")

class Teacher(models.Model):
    name = models.CharField(max_length=20,verbose_name="姓名")

class Student(models.Model):
    name =  models.CharField(max_length=20,verbose_name="姓名")