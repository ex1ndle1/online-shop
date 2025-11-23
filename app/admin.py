# from django.contrib import admin
from .models import Category,Product,Comment,Messages
from baton.autodiscover import admin







# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Messages)




admin.site.register(Comment)

