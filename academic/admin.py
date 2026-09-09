from django.contrib import admin
from .models import Teacher, Course, Student, StudentCourse

# Registro del modelo Teacher en el panel de administración
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')

# Registro del modelo Course
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'teacher')
    list_filter = ('teacher',)
    search_fields = ('name',)

# Registro del modelo Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')

# Registro de la tabla intermedia StudentCourse
@admin.register(StudentCourse)
class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ('student', 'course')
    list_filter = ('course',)
