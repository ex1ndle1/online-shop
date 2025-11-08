
from django.contrib import admin
from django.urls import path,include

from .views import index,detail

app_name = 'app'  
urlpatterns = [
    path('', index, name='index'), 
    path('details/<int:product_id>/', detail, name='detail'),  
]