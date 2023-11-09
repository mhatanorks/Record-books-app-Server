# app.urls.py
from django.urls import path
from .views import BookCreateView, BookListView, BookStatusUpdateView
from app import views

urlpatterns = [
    path('create/', BookCreateView.as_view(), name='book-create'),
    path('list/', BookListView.as_view(), name='book-list'),
    path('update-status/', BookStatusUpdateView.as_view(), name='update-status'),
    path("", views.IndexView.as_view(), name="index"),
]
