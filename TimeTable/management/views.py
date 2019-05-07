from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.shortcuts import render
from .models import Student,Course,Lecture
#from django.template import loader
from django.views.generic.edit import CreateView

def index(request):
    #html = '<h1>Welcome to the Home Page!</h1><br>'
    #html += '<a href = "' + 'student/' + '">' + 'Students' + '</a><br>'
    all_courses = Course.objects.all()
    #template = loader.get_template('management/index.html')
    #context = {'all_courses' : all_courses}
    return render(request,'management/index.html',{'all_courses' : all_courses})
def logout(request):
    return render(request,'management/logout.html')

def view_students(request):
    all_studs = Student.objects.all()
    html = ''
    html += '<h1>List of Students enrolled :</h1><br>'
    for stud in all_studs:
        url = str(stud.Student_ID) + '/'
        html += '<a href = "' + url + '">' + stud.First_Name + " " + stud.Last_Name + '</a><br>'
    return HttpResponse(html)

def student(request,student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        raise Http404("Student does not exist")
    if student.Middle_Name == None:
        name = student.First_Name + " " + student.Last_Name
    else:
        name = student.First_Name + " " + student.Middle_Name + " " + student.Last_Name
    return render(request,'management/student.html',{'student' : student,'name' : name})
    #return #HttpResponse("<h2>Welcome to the Student Page! <br>" + str(student_id) + " </h2>")

def course(request,course_id):
    return HttpResponse("<h2>Welcome to the Course Page! <br>" + str(course_id) + " </h2>")

def studentTimeTable(request,student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        raise Http404("Student does not exist")
    all_courses = Course.objects.filter(Department = student.Department).filter(Semester = student.Semester).order_by('Course_Number')
    all_lectures = Lecture.objects.all()
    #for c in all_courses:
    #    all_lectures = Lecture.objects.filter(Course = c)
    all_lectures = all_lectures.order_by('Time_Slot')#.order_by('Day')
    all_lectures = all_lectures.order_by('Day')
    Mon_lectures = all_lectures.filter(Day=1)
    Tue_lectures = all_lectures.filter(Day=2)
    Wed_lectures = all_lectures.filter(Day=3)
    Thu_lectures = all_lectures.filter(Day=4)
    Fri_lectures = all_lectures.filter(Day=5)
    if student.Middle_Name == None:
        name = student.First_Name + " " + student.Last_Name
    else:
        name = student.First_Name + " " + student.Middle_Name + " " + student.Last_Name
    context = {'all_courses' : all_courses,'student' : student,'name' : name, 'all_lectures' : all_lectures, 'Mon_lectures' : Mon_lectures,'Tue_lectures' : Tue_lectures,'Wed_lectures' : Wed_lectures,'Thu_lectures' : Thu_lectures,'Fri_lectures' : Fri_lectures,}

    return render(request,'management/timetable.html',context)

class StudentCreate(CreateView):
    model = Student
    fields = ['Student_ID','Department','Programme','Year','Semester','First_Name','Middle_Name','Last_Name','Address','City','State','Phone_Number','Date_of_Birth']









# Create your views here.
