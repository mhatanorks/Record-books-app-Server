# app.views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer, BookReadSerializer
from rest_framework.permissions import IsAuthenticated  # 認証されたユーザーのみアクセス許可
from rest_framework.permissions import AllowAny 


from accounts.models import CustomUser
from django.shortcuts import get_object_or_404


class BookCreateView(generics.CreateAPIView):
    # queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [IsAuthenticated]  # 認証されたユーザーのみ許可
    permission_classes = [AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save() 


class BookListView(generics.ListAPIView):
    serializer_class = BookReadSerializer
    permission_classes = [AllowAny]  # または IsAuthenticated に戻すこともできます

    def get_queryset(self):
        # リクエストからメールアドレスを取得します
        user_email = self.request.query_params.get('email')
        # メールアドレスに基づいてユーザーを取得します
        user = get_object_or_404(CustomUser, email=user_email)
        # statusが 'delete' でない Book オブジェクトを取得します
        return Book.objects.filter(userId=user).exclude(status='delete')
