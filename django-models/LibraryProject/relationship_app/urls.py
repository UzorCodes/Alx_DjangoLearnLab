from django.contrib import admin
from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('book_list/', views.book_list, name='book list'),
    path('library_detail/', views.LibraryDetailView(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='register/login.html'), name='login'),
path('logout/', LogoutView.as_view(), name='logout'),

]