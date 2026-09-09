from rest_framework import serializers
# pyrefly: ignore [missing-import]
from .models import Author, Member, Book, Loan

# LOS SERIALIZADORES:
# Traducen (convierten) la información compleja de nuestra base de datos (los Modelos)
# a formato JSON, que es el estándar universal que usan las páginas web y aplicaciones para comunicarse.

# Serializador para el Autor
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author # Indicamos el modelo que vamos a convertir
        fields = '__all__' # Indicamos que queremos incluir todos los campos (id, first_name, last_name)

# Serializador para el Socio
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

# Serializador para el Libro
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# Serializador para el Préstamo
class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'
