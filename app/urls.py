# app.urls.py
from django.urls import path
from .views import BookCreateView, BookListView

urlpatterns = [
    path('create/', BookCreateView.as_view(), name='book-create'),
    path('list/', BookListView.as_view(), name='book-list'),
]
