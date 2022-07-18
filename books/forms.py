from django import forms
from .models import *
##ModelForms
class BookForm(forms.ModelForm):
        class Meta:
            model = Books
            exclude = ['published_at','slug']
            
class UpdateForm(forms.ModelForm):
        class Meta:
            model = Books
            exclude = ['published_at','slug']
        