from django.db import models

# MODELO TEACHER (Profesor)
# Representa a los profesores en la base de datos.
class Teacher(models.Model):
    # CharField es un campo de texto corto. 'max_length' es obligatorio e indica la longitud máxima.
    # 'verbose_name' es el nombre legible que aparecerá en el panel de administración de Django.
    first_name = models.CharField(max_length=100, verbose_name="Nombre")
    last_name = models.CharField(max_length=100, verbose_name="Apellido")

    # El método __str__ define cómo se mostrará el objeto cuando se imprima (por ejemplo, en el admin).
    # En este caso, devolverá el nombre completo del profesor.
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# MODELO COURSE (Curso)
# Representa las materias o cursos disponibles en el sistema.
class Course(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre del Curso")
    
    # ForeignKey indica una relación de "Uno a Muchos". 
    # Un profesor puede tener muchos cursos, pero un curso pertenece a un solo profesor.
    # 'on_delete=models.CASCADE' significa que si se borra el profesor, también se borrarán sus cursos asignados.
    # 'related_name' permite acceder a los cursos desde un objeto Teacher (ej: teacher.courses.all())
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.name

# MODELO STUDENT (Estudiante)
# Representa a los alumnos inscritos en la escuela.
class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Nombre")
    last_name = models.CharField(max_length=100, verbose_name="Apellido")
    
    # ManyToManyField define una relación de "Muchos a Muchos".
    # Un estudiante puede tomar muchos cursos, y un curso puede tener muchos estudiantes.
    # 'through' especifica qué modelo se usará como tabla intermedia (en este caso, StudentCourse).
    courses = models.ManyToManyField(Course, through='StudentCourse', related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# MODELO INTERMEDIO STUDENTCOURSE (Estudiante-Curso)
# Es la tabla "puente" o de unión que relaciona qué estudiante está en qué curso.
class StudentCourse(models.Model):
    # Se crean claves foráneas (ForeignKeys) que apuntan al Estudiante y al Curso.
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    # La clase Meta se usa para configuraciones adicionales del modelo.
    class Meta:
        # unique_together garantiza que un estudiante no pueda inscribirse dos veces en el mismo curso exacto.
        unique_together = ('student', 'course')
        verbose_name = "Student Course"
        verbose_name_plural = "Student Courses"

    def __str__(self):
        return f"{self.student} inscrito en {self.course}"
