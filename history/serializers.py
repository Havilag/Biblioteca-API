from rest_framework import serializers
from .models import HistoryLog

class HistoryLogSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = HistoryLog
        fields = ['id', 'username', 'action', 'description', 'timestamp']