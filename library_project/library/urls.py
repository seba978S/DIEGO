from django.urls import path, include
from rest_framework.routers import DefaultRouter
# pyrefly: ignore [missing-import]
from .views import AuthorViewSet, MemberViewSet, BookViewSet, LoanViewSet

# EL ENRUTADOR (Router):
# Se encarga de crear automáticamente todas las rutas de URL para nuestras APIs.
router = DefaultRouter()

# Registramos cada entidad en el enrutador para que cree sus rutas de acceso. 
# Esto habilitará automáticamente: /api/authors/, /api/members/, /api/books/ y /api/loans/
router.register(r'authors', AuthorViewSet)
router.register(r'members', MemberViewSet)
router.register(r'books', BookViewSet)
router.register(r'loans', LoanViewSet)

# Exportamos las URLs generadas para que el archivo principal (library_project/urls.py) las pueda leer e incluir.
urlpatterns = [
    # Incluimos todas las rutas que el router acaba de generar en nuestra aplicación.
    path('', include(router.urls)),
]
