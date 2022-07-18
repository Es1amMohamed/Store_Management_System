
from tkinter import Button
from django.shortcuts import redirect, render
from django.urls import  reverse
from .models import *
from .forms import *

# Create your views here.
def book_list(request):
    
    books = Books.objects.all()
    context = {'books': books}
    
    return render(request,'books/books_list.html', context)

def book_update(request ,slug):
    book = Books.objects.get(slug=slug)
    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect(reverse('books:book_create'))
        else:
            return redirect(reverse('books:book_update', kwargs={'slug': slug})) 
    else:
        form = UpdateForm(instance=book)
        return render(request, 'books/book_update.html', {'form': form})                                     


def delete_book(request ,slug):
    book = Books.objects.get(slug=slug)    
    context = {'book': book}
    return render(request, 'books/delete_book.html' , context)

def delete_confirm(request, slug):
    book = Books.objects.get(slug=slug)
    context = {'books': book}
    book.delete()
    return render(request, 'books/delete_confirm.html', context)

def book_create(request):
    book = Books.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        form = BookForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('books:book_list'))
        else:
            return redirect(reverse('books:book_create'))
    else:
        form = BookForm()
        return render(request, 'books/book_create.html', {'form': form , 'books': book , 'categories': categories})

    
   
    


