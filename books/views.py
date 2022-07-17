
from tkinter import Button
from django.shortcuts import redirect, render
from django.urls import  reverse
from .models import *

# Create your views here.
def book_list(request):
    
    books = Books.objects.all()
    context = {'books': books}
    
    return render(request,'books/books_list.html', context)

# Update the book 
def book_update(request ,slug):
    book = Books.objects.get(slug=slug)
    books = Books.objects.all()
    context = {'book': book , 'books': books}
    return render(request, 'books/book_update.html', context)


def delete_book(request ,slug):
    book = Books.objects.get(slug=slug)    
    context = {'book': book}
    return render(request, 'books/delete_book.html' , context)

def delete_confirm(request, slug):
    book = Books.objects.get(slug=slug)
    context = {'books': book}
    book.delete()
    return render(request, 'books/delete_confirm.html', context)

    
   
    


