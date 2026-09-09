from rest_framework import viewsets
from django.shortcuts import render
from .models import Author, Member, Book, Loan
from .serializers import AuthorSerializer, MemberSerializer, BookSerializer, LoanSerializer

# LAS VISTAS DE LA API (ViewSets):
# ModelViewSet es una herramienta muy potente de Django REST Framework que nos crea automáticamente 
# las 5 operaciones básicas (CRUD): Crear (POST), Leer lista (GET), Leer detalle (GET), Actualizar (PUT) y Eliminar (DELETE).

class AuthorViewSet(viewsets.ModelViewSet):
    # ¿De dónde sacamos los datos? De la base de datos (traemos todos los Autores).
    queryset = Author.objects.all()
    # ¿Cómo convertimos esos datos a JSON? Usando el AuthorSerializer que configuramos.
    serializer_class = AuthorSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

# LAS VISTAS VISUALES (HTML):
# Estas funciones no devuelven datos JSON ocultos, sino que devuelven el diseño de la página web que el usuario ve (archivos HTML).

def api_home(request):
    # Muestra la página principal de bienvenida al entrar a la raíz de la web
    return render(request, 'library/home.html')

def books_view(request):
    # Muestra la pantalla donde está la tabla visual de libros
    return render(request, 'library/books.html')

def members_view(request):
    # Muestra la pantalla donde está la tabla visual de socios
    return render(request, 'library/members.html')
