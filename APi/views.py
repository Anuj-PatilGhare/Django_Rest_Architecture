# from django.shortcuts import render
# from django.http import JsonResponse
from students.models import Studnets
from . import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee

 ### Function Bases Views for Students Data Endpoints :


@api_view(['GET','POST'])
def studentsView(request):
    if request.method == 'GET':
        students_info = Studnets.objects.all()
        serialize_data = serializers.StudentSerializer(students_info, many=True)
        return Response(serialize_data.data, status=status.HTTP_200_OK)
    elif request.method =='POST':
        serializer = serializers.StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def studentDetailsView(request,pk):
    try:
        student = Studnets.objects.get(pk=pk)
    except Studnets.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer_data = serializers.StudentSerializer(student)
        return Response(serializer_data.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer_data = serializers.StudentSerializer(student, data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


## Class Bases views for Employee Class :

class Employees(APIView):
    def get(self, request):
        employee = Employee.objects.all()
        serialize_data = serializers.EmployeeSerializer(employee, many=True)
        return Response(serialize_data.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = serializers.EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
class EmployeeDetails(APIView):
    