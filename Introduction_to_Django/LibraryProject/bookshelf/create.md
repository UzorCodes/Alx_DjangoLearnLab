# Creating a new book
from bookshelf.models import Book

Book.objects.create(
    title ='1984',
    author='George Orwell',
    published_year ='1949',
)
new_book.save()

#This performs an insert SQL statement behind the scenes