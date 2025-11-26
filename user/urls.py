from django.urls import path
from .views import register,home
app_name = 'user'
urlpatterns = [
    path('home/', home, name='home'),
    path('register/', register, name='register'),
]
