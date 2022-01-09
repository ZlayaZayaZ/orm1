from django.http import HttpResponse
from django.shortcuts import render
from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {'books': Book.objects.all()}
    return render(request, template, context)


def paginator_book(request):
    return HttpResponse