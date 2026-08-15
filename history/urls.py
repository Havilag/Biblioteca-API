from django.urls import path
from . import views

urlpatterns = [
    path('history/', views.HistoryLogView.as_view(), name='history-list'),
]