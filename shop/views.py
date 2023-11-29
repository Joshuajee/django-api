from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book
from .serializer import BookSerializers
# Create your views here.

@api_view(['GET'])
def books(req):
    all_books = Book.objects.all()
    serialized_data = BookSerializers(all_books, many=True)
    return Response(serialized_data.data)

@api_view(['GET'])
def book_by_id(req, id):
    book = Book.objects.get(id=id)
    serialized_data = BookSerializers(book)
    return Response(serialized_data.data)

@api_view(['GET'])
def books_by_author(req, author):
    all_books = Book.objects.filter(author__iexact=author)
    serialized_data = BookSerializers(all_books, many=True)
    return Response(serialized_data.data)

@api_view(['POST'])
def add_book(req):
    serialized_data = BookSerializers(data=req.data)
    if serialized_data.is_valid():
        serialized_data.save()
    return Response(serialized_data.data)

