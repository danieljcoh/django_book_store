from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Book

# Create your views here.


def index(request):
    books = Book.objects.all()  # caching
    return render(request, "book_outlet_app/index.html", {
        "books": books
    })


def book_detail(request, id):
    # book = get_object_or_404(Book, pk=id)
    try:
        book = Book.objects.get(pk=id)
    except:
        raise Http404()

    return render(request, "book_outlet_app/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    })
