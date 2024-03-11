# views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    serializer = BookSerializer(book)
    return JsonResponse(serializer.data)

@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['PUT'])
def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    serializer = BookSerializer(instance=book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return JsonResponse({'message': 'Book deleted successfully!'}, status=204)
