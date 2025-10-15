from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('book_list/', views.book_list, name='book list'),
    path('book_detail/', views.BookDetailView(), name='book_detail'),
]