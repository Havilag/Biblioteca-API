from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.BookView.as_view()),
    path('books/<int:pk>/', views.ManageBookView.as_view() )
]