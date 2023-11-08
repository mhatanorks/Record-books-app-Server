# app/serializers.py
from rest_framework import serializers
from .models import Book
from accounts.models import CustomUser
from django.shortcuts import get_object_or_404


class BookSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Book
        fields = ['id','title', 'authors', 'thumbnail',
                  'memo', 'status', 'userId', 'email']
        extra_kwargs = {
            'userId': {'read_only': True}  # userIdは読み取り専用にする
        }

    def create(self, validated_data):
        user_email = validated_data.pop('email')
        # user = CustomUser.objects.get(email=user_email)  # ユーザーを取得
        user = get_object_or_404(CustomUser, email=user_email)  # 例外処理を追加
        status = validated_data.pop(
            'status', 'record')  # statusを取り出し、デフォルト値を設定

        # validated_dataからstatusを取り出した後に、Bookオブジェクトを作成
        book = Book.objects.create(
            userId=user, status=status, **validated_data)
        return book


class BookReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'authors',
                  'thumbnail', 'memo', 'status', 'createdAt']
