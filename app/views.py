from django.shortcuts import render,get_object_or_404
from .models import Category,Product
# Create your views here.
def index(request):
    category = Category.objects.all()
    product = Product.objects.all()
    context = {
        'categories':category,
        'products':product
    }
    return render(request, 'app/home.html',context)



def detail(request, product_id):
    product = get_object_or_404(Product, id = product_id)
    return render(request, 'app/detail.html', {'product':product})