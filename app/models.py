from django.db import models
from accounts.models import CustomUser  # CustomUserモデルをインポート


class Book(models.Model):
    STATUS_CHOICES = [
        ('record', 'Record'),
        ('favorite', 'Favorite'),
        ('delete', 'Delete'),
    ]
    
    id = models.AutoField(primary_key=True) 
    title = models.CharField(max_length=200)
    authors = models.JSONField()  # 文字列のリストを保存するためにJSONFieldを使用
    thumbnail = models.URLField(max_length=300, blank=True)  # URLは空でもよい場合
    createdAt = models.DateTimeField(auto_now_add=True)  # レコードが作成された時に自動的に現在の日時を設定
    memo = models.TextField(blank=True)  # メモは空でもよい場合
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)  # 状態は3つの選択肢から選ぶ
    userId = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # CustomUserモデルへの外部キー

    def __str__(self):
        return self.title
