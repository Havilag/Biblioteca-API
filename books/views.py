from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from history.models import HistoryLog
from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema(tags=['Book'])
@extend_schema_view(
    get = extend_schema(
        summary='Listar Libros',
        description='Obtiene todos los Libros registrados en la bilbioteca.'
    ),
    post = extend_schema(
        summary='Registrar un libro',
        description='Registrar un nuevo Libro en la biblioteca.'
    )
)

class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'status', 'author']
    
    def perform_create(self, serializer):
        book = serializer.save()
        
        HistoryLog.objects.create(
            user=self.request.user,
            action=HistoryLog.ActionTypes.BOOK_ADDED,
            description=f"Registró el libro '{book.title}'."
        )
    
    
@extend_schema(tags=['Book'])
@extend_schema_view(
    get = extend_schema(
        summary='Obtener un Libro.',
        description='Obtiene un Libro mediante su ID.'
    ),
    put = extend_schema(
        summary='Actualizar un Libro.',
        description='Actualiza los datos de un Libro mediante su ID.'
    ),
    delete = extend_schema(
        summary='Eliminar un Libro',
        description='Eliminar un Libro mediante su ID.'
    )
)
class ManageBookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

