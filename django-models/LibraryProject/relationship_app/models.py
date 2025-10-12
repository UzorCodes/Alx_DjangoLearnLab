from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField
    return self.name

class Book(models.Model):
    title = models.CharField
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book')

class Library(models.Model):
    name = models.CharField
    books = models.ManyToManyField(Book, related_name='libraries')

class Librarian(models.Model):
    name = models.CharField
    library = models.OneToOneField(Library, om_delete=models.CASCADE)