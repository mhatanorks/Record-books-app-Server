from rest_framework import generics
from .models import Book
from .serializers import BookSerializer, BookReadSerializer, BookStatusUpdateSerializer
from rest_framework.permissions import IsAuthenticated  # 認証されたユーザーのみアクセス許可
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


from accounts.models import CustomUser
from django.shortcuts import get_object_or_404

from django.views.generic import View
from django.shortcuts import render

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "app/index.html")



class BookCreateView(generics.CreateAPIView):
    # queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # 認証されたユーザーのみ許可


class BookListView(generics.ListAPIView):
    serializer_class = BookReadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # リクエストからメールアドレスを取得
        user_email = self.request.query_params.get('email')
        # メールアドレスに基づいてユーザーを取得
        user = get_object_or_404(CustomUser, email=user_email)
        # statusが'delete'以外、Bookオブジェクトを日付が新しい順に取得します
        return Book.objects.filter(userId=user).exclude(status='delete').order_by('-createdAt')


class BookStatusUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookStatusUpdateSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        book_id = request.data.get('id')
        status = request.data.get('status')

        try:
            book = self.queryset.get(id=book_id)
            serializer = self.serializer_class(
                book, data={'status': status}, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Book.DoesNotExist:
            return Response({'message': 'Book not found'}, status=404)
