from rest_framework import viewsets
from django.http import JsonResponse
from django.shortcuts import render
from .models import Teacher, Course, Student, StudentCourse
# pyrefly: ignore [missing-import]
from .serializers import TeacherSerializer, CourseSerializer, StudentSerializer, StudentCourseSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCourseViewSet(viewsets.ModelViewSet):
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer

def api_home(request):
    return render(request, 'academic/home.html')

def courses_view(request):
    return render(request, 'academic/courses.html')

def students_view(request):
    return render(request, 'academic/students.html')

def teachers_view(request):
    # Devuelve la página web visual para mostrar la tabla de Docentes.
    return render(request, 'academic/teachers.html')

def custom_404_view(request, path=''):
    return render(request, 'academic/404.html', status=404)
