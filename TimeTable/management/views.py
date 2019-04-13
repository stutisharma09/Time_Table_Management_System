from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def index(request):
    return HttpResponse("<h1>Welcome to the Home Page!</h1>")

def view_students(request):
    all_studs = Student.objects.all()
    html = ''
    for stud in all_studs:
        url = str(stud.Student_ID) + '/'
        html += '<a href = "' + url + '">' + stud.First_Name + " " + stud.Middle_Name[0] + ". " + stud.Last_Name + '</a><br>'
    return HttpResponse(html)

def student(request,student_id):
    
    return HttpResponse("<h2>Welcome to the Student Page! <br>" + str(student_id) + " </h2>")


# Create your views here.
