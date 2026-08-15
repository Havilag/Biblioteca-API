from django.db import models
from django.contrib.auth import get_user_model

class HistoryLog(models.Model):
    class ActionTypes(models.TextChoices):
        LOAN_CREATED = 'LOAN_CREATED', 'Préstamo Creado'
        LOAN_RETURNED = 'LOAN_RETURNED', 'Préstamo Devuelto'
        BOOK_ADDED = 'BOOK_ADDED', 'Libro Registrado'

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='history_logs'
    )
    action = models.CharField(max_length=30, choices=ActionTypes.choices)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} ({self.timestamp.strftime('%Y-%m-%d %H:%M')})"