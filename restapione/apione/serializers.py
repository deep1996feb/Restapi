from dataclasses import field
from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    Name = serializers.CharField(max_length=30)
    Field = serializers.CharField(max_length=50)
    Employeeid = serializers.IntegerField()
    Address = serializers.CharField(max_length=100)

    def create(self, validate_data):
        return Employee.objects.create(**validate_data)