from urllib.parse import urlparse
from django.urls import URLPattern, path , include
from . import views
from .views import *

app_name = 'books'

urlpatterns = [
    path('',views.book_list,name='book_list'),
    path('<str:slug>',views.book_update,name='book_update'),
    path('delete/<str:slug>',views.delete_book,name='delete_book'),
    path('confirm/<str:slug>',views.delete_confirm,name='delete_confirm'),
]