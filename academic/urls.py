from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, CourseViewSet, StudentViewSet, StudentCourseViewSet

# EL ENRUTADOR (Router):
# DefaultRouter es una herramienta de Django REST Framework que se encarga 
# de generar automáticamente las URLs para los ViewSets (por ejemplo: GET /teachers/, POST /teachers/, etc).
router = DefaultRouter()

# Registramos nuestras rutas en el enrutador. 
# El primer parámetro es la ruta URL que veremos en el navegador y el segundo es el ViewSet que manejará la petición.
router.register(r'teachers', TeacherViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'students', StudentViewSet)
router.register(r'enrollments', StudentCourseViewSet)

# urlpatterns es la lista donde Django busca las rutas disponibles dentro de esta aplicación ("academic").
urlpatterns = [
    # path('', include(router.urls)) significa que todas las rutas generadas por el router 
    # se incluirán directamente en el camino base donde se invoque este archivo.
    path('', include(router.urls)),
]
