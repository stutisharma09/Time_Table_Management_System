from django.contrib import admin

# Register your models here.
from .models import Department
from .models import Student
from .models import Course
from .models import Programme,Teacher,Venue,Lecture
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Venue)
admin.site.register(Lecture)
