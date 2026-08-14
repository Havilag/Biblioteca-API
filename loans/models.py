from django.db import models
from django.contrib.auth import get_user_model
from books.models import Book

class Loan(models.Model):
    
    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', 'Activo'
        RETURNED = 'RETURNED', 'Devuelto'
        OVERDUE = 'OVERDUE', 'Atrasado'
    
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='loans'
    )
    
    
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='loans'
    )
    
    loan_date = models.DateField()
    return_date = models.DateField(
        null=True,
        blank=True
    )
    
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE
    )
    
    created_at = models.DateTimeField(auto_now_add=True)