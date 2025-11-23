from .models import Product, Category, Comment, Order, Messages
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
        fields = ['rating', 'name', 'email', 'message', 'file']

class OrderForm(forms.ModelForm):
    class Meta:
        model  = Order
        fields = ['name', 'phone'] 




class AboutForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['author', 'title' , 'email']