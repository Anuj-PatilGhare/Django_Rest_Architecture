from rest_framework import serializers
from students.models import Studnets
from employees.models import Employee

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studnets
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fileds = '__all__'