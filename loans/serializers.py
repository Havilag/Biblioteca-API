from rest_framework import serializers
from .models import Loan


class LoanSerializer(serializers.ModelSerializer):
    
    book_title = serializers.CharField(source='book.title', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Loan
        fields = ['id', 'loan_date', 'return_date', 'status', 'created_at', 'user', 'username', 'book', 'book_title']