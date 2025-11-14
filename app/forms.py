from .models import Product, Category, Comment
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model  = Product
        fields = ['name','description','price','discount','stock','category','image']


        

class CategoryForm(forms.ModelForm):
     class Meta:
         model = Category
         fields = ['title']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'text']
