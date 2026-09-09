from django.contrib import admin
from django.urls import path, include, re_path
from academic.views import api_home, courses_view, students_view, teachers_view, custom_404_view

# ARCHIVO PRINCIPAL DE RUTAS:
# Este es el "panel de control" de direcciones web. 
# Aquí es donde llega primero cualquier petición web a todo el proyecto.

urlpatterns = [
    # Ruta reservada para acceder al panel de administración de Django (http://127.0.0.1:8000/admin/)
    path('admin/', admin.site.urls),
    
    # Ruta para nuestra API RESTful. 
    # Todo lo que empiece con 'api/' (ej: /api/courses/) será derivado a las rutas definidas en 'academic/urls.py'.
    path('api/', include('academic.urls')),
    
    # Ruta raíz (''). Es la página de inicio que los usuarios ven al entrar (http://127.0.0.1:8000/).
    path('', api_home, name='home'),
    
    # Rutas para el frontend visual (las páginas HTML de Cursos y Estudiantes que abren en el navegador).
    path('cursos/', courses_view, name='courses_view'),
    path('estudiantes/', students_view, name='students_view'),
    path('docentes/', teachers_view, name='teachers_view'),
    
    # Ruta comodín para capturar cualquier ruta que no exista y mostrar nuestro error personalizado
    re_path(r'^(?P<path>.*)/?$', custom_404_view),
]
