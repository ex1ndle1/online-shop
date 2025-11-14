
from django.contrib import admin
from django.urls import path,include

from .views import index,detail,create_product,delete_product,create_category,product_update,info

app_name = 'app'  
urlpatterns = [
    path('', index, name='index'), 
    path('delete/', delete_product , name='delete_product'),
    path('details/<int:product_id>/', detail, name='detail'),  
    path('create_product/',create_product, name='create_product'),
    path('create_category/',create_category, name='create_category'),
    path('product_update/', product_update, name='product_update' ),
    path('info/',info, name='info')
]