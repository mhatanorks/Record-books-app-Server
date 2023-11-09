from django.db import models
from accounts.models import CustomUser


class Book(models.Model):
    STATUS_CHOICES = [
        ('record', 'Record'),
        ('favorite', 'Favorite'),
        ('delete', 'Delete'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    authors = models.JSONField()
    thumbnail = models.URLField(max_length=300, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    memo = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    userId = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
