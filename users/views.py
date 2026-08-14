from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView


@extend_schema_view(
    post = extend_schema(
        tags=['Autenticación'],
        summary='Registrar usuario',
        description='Permite registrar un nuevo usuario de la biblioteca.'
    )
)
class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    


@extend_schema_view(
    post = extend_schema(
        tags=['Autenticación'],
        summary='Iniciar Sesión',
        description='Valida credenciales y devuelve el par de token JWT.'
    )
)
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer