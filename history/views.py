from rest_framework import generics, permissions
from .models import HistoryLog
from .serializers import HistoryLogSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Historial de Usuario'])
class HistoryLogView(generics.ListAPIView):
    serializer_class = HistoryLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return HistoryLog.objects.all().order_by('-timestamp')
        return HistoryLog.objects.filter(user=self.request.user).order_by('-timestamp')