from django.contrib import admin

# Register your models here.
from .models import Department
from .models import Student
from .models import Course
from .models import Programme,Teacher
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Teacher)
