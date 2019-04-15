from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/', views.view_students, name='view_students'),
    path('student/<student_id>/', views.student, name='student'),
    path('course/<course_id>/', views.course, name='course')


]
