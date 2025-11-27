from django.urls import path
from .views import register, login,logout
app_name = 'user'
urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout')
]
