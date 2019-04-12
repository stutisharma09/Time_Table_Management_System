from django.db import models

# Create your models here.
class IntegerRangeField(models.BigIntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class Department(models.Model):
    Name =  models.CharField(max_length=100)
    Department_Code = models.CharField(max_length=3, primary_key = True)
    def __str__(self):
        return self.Name

class Student(models.Model):
    First_Name =  models.CharField(max_length=30)
    Middle_Name =  models.CharField(max_length=30,null=True,blank=True)
    Last_Name =  models.CharField(max_length=30)
    Address = models.CharField(max_length=30)
    City = models.CharField(max_length=30,default='Chandigarh')
    State = models.CharField(max_length=30,default='Chandigarh')
    Department =  models.ForeignKey(Department, on_delete=models.CASCADE)
    Student_ID = IntegerRangeField(min_value=17101001,max_value=17109200, primary_key = True)
    Phone_Number = IntegerRangeField(min_value=1000000000,max_value=9999999999)
    Date_of_Birth = models.DateField()
    def __str__(self):
        return str(self.Student_ID) + " : " + self.First_Name + " " + self.Middle_Name[0] + ". " + self.Last_Name

class Course(models.Model):
    Name =  models.CharField(max_length=100,primary_key = True)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    Course_Number = IntegerRangeField(min_value=101,max_value=999)
    Course_Credits = IntegerRangeField(min_value=1,max_value=4,default=4)
    def __str__(self):
        return  self.Department.Department_Code + str(self.Course_Number) + " : " + self.Name
