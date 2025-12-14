
from django.contrib import admin
from django.urls import path
from .views import Index,ProductDetai,ProductCreate,ProductDelete,ProductUpdate,CategoryCreate,About

app_name = 'app'  
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('product/<int:product_id>/', ProductDetai.as_view(), name='detail'),
    path('product/create/', ProductCreate.as_view(), name='create_product'),
    path('product/delete/<int:pk>/', ProductDelete.as_view(), name='delete_product'),
    path('product/update/<int:pk>/', ProductUpdate.as_view(), name='product_update'),
    path('category/create/', CategoryCreate.as_view(), name='create_category'),
   
    path('about/', About.as_view(), name='about'),
]
