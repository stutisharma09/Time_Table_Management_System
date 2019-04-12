from django.db import models

# Create your models here.
class Department(models.Model):
    Name =  models.CharField(max_length=100)
    Department_Code = models.CharField(max_length=3, primary_key = True)
    def __str__(self):
        return self.Name
