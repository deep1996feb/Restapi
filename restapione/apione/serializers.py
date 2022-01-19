from dataclasses import field
from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    Name = serializers.CharField(max_length=30)
    Field = serializers.CharField(max_length=50)
    Employeeid = serializers.IntegerField()
    Address = serializers.CharField(max_length=100)
