from django.urls import path
from . import views

urlpatterns = [
    path('history/', views.HistoryLogListView.as_view(), name='history-list'),
]