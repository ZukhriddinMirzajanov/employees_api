from django.db import models

# Create your models here.

class Departments(models.Model):
    Department_id = models.AutoField(primary_key=True)
    Department_name = models.CharField(max_length=100)


class Employees(models.Model):
    Employee_id = models.AutoField(primary_key=True)
    Employee_name = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    Date_of_joining = models.DateField()
    Phote_file_name = models.CharField(max_length=100)
