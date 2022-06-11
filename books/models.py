from django.db import models

# Create your models here.
class Books(models.Model):
    book_title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    authors_name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    published_at = models.DateField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.book_title
    
# Create Category model
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category_name
   
