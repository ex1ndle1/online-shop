
from django.contrib import admin
from django.urls import path,include

from .views import index,detail,create_product,delete_product

app_name = 'app'  
urlpatterns = [
    path('', index, name='index'), 
    path('delete/', delete_product , name='delete_product'),
    path('details/<int:product_id>/', detail, name='detail'),  
    path('create_product/',create_product, name='create_product')
]