from django.db import models
from django.db.models import fields
from rest_framework import serializers
from EmployeeApp.models import Departments, Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('Department_id',
                  'Department_name')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('Employee_id',
                  'Employee_name',
                  'Department',
                  'Date_of_joining',
                  'Phote_file_name')