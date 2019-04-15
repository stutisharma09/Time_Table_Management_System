from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Course
from django.template import loader

def index(request):
    #html = '<h1>Welcome to the Home Page!</h1><br>'
    #html += '<a href = "' + 'student/' + '">' + 'Students' + '</a><br>'
    all_courses = Course.objects.all()
    template = loader.get_template('management/index.html')
    context = {'all_courses' : all_courses,}
    return HttpResponse(template.render(context,request))

def view_students(request):
    all_studs = Student.objects.all()
    html = ''
    html += '<h1>List of Students enrolled :</h1><br>'
    for stud in all_studs:
        url = str(stud.Student_ID) + '/'
        html += '<a href = "' + url + '">' + stud.First_Name + " " + stud.Last_Name + '</a><br>'
    return HttpResponse(html)

def student(request,student_id):
    return HttpResponse("<h2>Welcome to the Student Page! <br>" + str(student_id) + " </h2>")

def course(request,course_id):
    return HttpResponse("<h2>Welcome to the Course Page! <br>" + str(course_id) + " </h2>")


# Create your views here.
