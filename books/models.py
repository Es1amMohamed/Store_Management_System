from django.db import models
from django.utils.text import slugify

# Create your models here.


Status = (
    ('Available' , 'Available'),
    ('Unavailable' , 'Unavailable'),
)
    

class Books(models.Model):
    book_title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    authors_name = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=Status)
    price = models.DecimalField(max_digits=5, decimal_places=1)
    published_at = models.DateField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True , blank=True, null=True)
    picture = models.ImageField(upload_to='books/', blank=True, null=True)
    
    
    def save(self,*args,**kwargs):
        
        self.slug = slugify(self.book_title)
        super(Books,self).save(*args,**kwargs) 
        
    def __str__(self):
        return self.book_title
    

        
    
# Create Category model
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category_name
   
