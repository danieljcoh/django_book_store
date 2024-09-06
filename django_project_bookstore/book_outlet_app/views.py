from django.shortcuts import render
from .models import Book

# Create your views here.


def index(request):
    books = Book.objects.all()  # caching
    return render(request, "book_outlet_app/index.html", {
        "books": books

    })
