from django.shortcuts import render
from .models import *

# Create your views here.
def book_list(request):
    
    return render(request,'books/books_list.html')

