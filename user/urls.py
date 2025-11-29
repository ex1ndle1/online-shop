from django.urls import path
from .views import register,logout, login_by_username, login_by_email,login_by_phone,login_choice
app_name = 'user'
urlpatterns = [
    path('login_by_username/', login_by_username, name='login_by_username'),
    path('register/', register, name='register'),
    path('login_by_phone/', login_by_phone, name='login_by_phone'),
    path('login_by_email/', login_by_email, name='login_by_email' ),
   path('login_choice/',login_choice,name='login_choice'),
    path('logout/', logout, name='logout'),

]
