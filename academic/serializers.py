from rest_framework import serializers
from .models import Teacher, Course, Student, StudentCourse

# LOS SERIALIZADORES:
# Toman los datos complejos de la base de datos (instancias de los modelos) 
# y los convierten en formatos nativos de Python que pueden ser fácilmente 
# renderizados en JSON (el formato universal para enviarlos a través de la API).

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher # Indicamos qué modelo vamos a serializar (Profesor)
        fields = '__all__' # Indicamos que queremos exponer todos los campos del modelo ('id', 'first_name', 'last_name')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course # Modelo Curso
        fields = '__all__' # Exponer todos los campos

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student # Modelo Estudiante
        fields = '__all__' # Exponer todos los campos

class StudentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourse
        fields = '__all__'
