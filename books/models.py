from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=17, unique=True)
    publication_year = models.IntegerField()

    class Category(models.TextChoices):
        NOVEL = 'NOVEL', 'Novela'
        SCIENCE = 'SCIENCE', 'Ciencia'
        HISTORY = 'HISTORY', 'Historia'
        FANTASY = 'FANTASY', 'Fantasía'
        TECHNOLOGY = 'TECHNOLOGY', 'Tecnología'
        OTHER = 'OTHER', 'Otros'
    
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.OTHER
    )
         
    class Status(models.TextChoices):
        AVAILABLE = 'AVAILABLE', 'Disponible'
        BORROWED = 'BORROWED', 'Prestado'
        MAINTENANCE = 'MAINTENANCE', 'Mantenimiento'

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.AVAILABLE
    )
        
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title