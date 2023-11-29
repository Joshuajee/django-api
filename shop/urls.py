from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("book/", views.add_book),
    path("book/<int:id>", views.book_by_id),
    path("books/", views.books),
    path("books/<str:author>", views.books_by_author)
]
