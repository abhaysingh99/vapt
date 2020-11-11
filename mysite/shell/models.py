from django.db import models

# Create your models here.
class Student(models.Model):
    sid = models.CharField(max_length=20)
    sname = models.CharField(max_length=100)
    scontact = models.CharField(max_length=15)
    class Meta:
        db_table = "student"