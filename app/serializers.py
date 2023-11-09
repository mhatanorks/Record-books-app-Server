# app/serializers.py
from rest_framework import serializers
from .models import Book
from accounts.models import CustomUser
from django.shortcuts import get_object_or_404


class BookSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'thumbnail',
                  'memo', 'status', 'userId', 'email']
        extra_kwargs = {
            'userId': {'read_only': True}
        }

    def create(self, validated_data):
        user_email = validated_data.pop('email')
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


class BookStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'status']

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
