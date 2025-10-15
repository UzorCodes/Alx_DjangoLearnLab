from django.contrib import admin
from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('book_list/', views.book_list, name='book list'),
    path('library_detail/', views.LibraryDetailView(), name='library_detail'),
]