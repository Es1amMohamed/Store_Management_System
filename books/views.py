from django.shortcuts import render
from .models import *

# Create your views here.
def book_list(request):
    context = {'books': Books.objects.all()}
    
    return render(request,'books/books_list.html', context)

