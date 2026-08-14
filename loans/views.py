from rest_framework import generics, serializers
from .models import Loan
from .serializers import LoanSerializer
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema(tags=['Loan'])
@extend_schema_view(
    get = extend_schema(
        summary='Listar Préstamos',
        description='Obtiene todos los préstamos registrados en la Biblioteca.'
    ),
    post = extend_schema(
        summary='Registrar un Préstamo',
        description='Se registrar un nuevo préstamo de un libro de la Biblioteca.'
    )
)

class LoanView(generics.ListCreateAPIView):
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Loan.objects.all()
        return Loan.objects.filter(user=user)
    
    
    def perform_create(self, serializer):
        book = serializer.validated_data['book']
        
        if book.status != 'AVAILABLE':
            raise serializers.ValidationError({'book': 'Este libro no esta disponible'})

        loan = serializer.save(user=self.request.user)
        book.status = 'BORROWED'
        book.save()

@extend_schema(tags=['Loan'])
@extend_schema_view(
    get = extend_schema(
        summary='Obtener un Préstamo',
        description='Obtiene un préstamo mediante su ID'
    ),
    put = extend_schema(
        summary='Actualiza un Préstamo',
        description='Actualiza el estado y la fecha de devolución de un préstamo mediante su ID.'
    ),
    delete = extend_schema(
        summary='Eliminar un Préstamo',
        description='Elimina un préstamo mediante su ID'
    )
)

class ManageLoanView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Loan.objects.all()
        return Loan.objects.filter(user=user)
    
    def perform_update(self, serializer):
        loan = serializer.save()
        
        if loan.status == 'RETURNED':
            loan.book.status = 'AVAILABLE'
            loan.book.save()
    
    
    def perform_destroy(self, instance):
        if not self.request.user.is_staff:
            raise serializers.ValidationError(
                {"detail": "No tienes permisos de administrador."}
            )

        book = instance.book
        book.status = 'AVAILABLE'
        book.save()
        instance.delete()