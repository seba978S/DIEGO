from django.contrib import admin
from django.urls import path, include
from library.views import api_home, books_view, members_view

# RUTAS PRINCIPALES DEL PROYECTO:
# Este archivo es el "índice" central de todas las direcciones de tu página web.
# Aquí es a donde llega primero cualquier persona que escriba tu dirección en el navegador.

urlpatterns = [
    # Ruta para acceder al panel privado de administración de Django (http://127.0.0.1:8000/admin/)
    path('admin/', admin.site.urls),
    
    # Rutas para la API REST. 
    # Todo lo que empiece con "api/" se enviará al archivo library/urls.py para que él lo gestione.
    path('api/', include('library.urls')),
    
    # Ruta raíz ('')
    # Esta es la página de inicio que los usuarios ven al entrar directamente (http://127.0.0.1:8000/)
    path('', api_home, name='home'),
    
    # Rutas visuales para acceder a las pantallas HTML desde el navegador
    path('books/', books_view, name='books_view'),
    path('members/', members_view, name='members_view'),
]
