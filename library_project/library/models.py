from django.db import models

# MODELO AUTHOR (Autor)
# Representa a los autores de los libros en nuestra base de datos.
class Author(models.Model):
    # CharField es un campo de texto corto. 'max_length' limita la cantidad de caracteres.
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    # __str__ define cómo se muestra este objeto en texto (por ejemplo, en el panel de administrador).
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# MODELO MEMBER (Socio/Miembro)
# Representa a los usuarios que piden libros prestados en la biblioteca.
class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# MODELO BOOK (Libro)
# Representa los libros disponibles en la biblioteca.
class Book(models.Model):
    title = models.CharField(max_length=200)
    
    # ForeignKey indica una relación "Uno a Muchos". 
    # Un autor puede escribir muchos libros, pero este libro pertenece a un solo autor.
    # on_delete=models.CASCADE significa que si borramos al autor, se borrarán todos sus libros automáticamente.
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

# MODELO LOAN (Préstamo)
# Es la tabla intermedia que registra qué socio pidió prestado qué libro.
class Loan(models.Model):
    # Relación "Uno a Muchos" con el Socio (quién pide el libro)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='loans')
    # Relación "Uno a Muchos" con el Libro (qué libro se lleva)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        # Muestra por ejemplo: "Cien años de soledad prestado a Juan Pérez"
        return f"{self.book} prestado a {self.member}"
