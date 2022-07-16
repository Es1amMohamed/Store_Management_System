from urllib.parse import urlparse
from django.urls import URLPattern, path , include
from . import views
from .views import *

app_name = 'books'

urlpatterns = [
    path('',views.book_list,name='book_list')
]