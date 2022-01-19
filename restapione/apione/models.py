from django.db import models

# Create your models here.
class Employee(models.Model):
    Name = models.CharField(max_length=30)
    Field = models.CharField(max_length=50)
    Employeeid = models.IntegerField()
    Address = models.CharField(max_length=100)
