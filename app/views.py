from django.shortcuts import render,get_object_or_404,redirect

from .models import Category,Product
from .forms import ProductForm

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



def create_product(request):
    category = Category.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():  
            form.save()     
            return redirect('app:index') #har bir ozagrishlardan keyin bosh sahifaga kochishni qoshdim
        
    else:
        form = ProductForm()
    return render(request, 'app/create_product.html', {'form': form, 'title': 'Add Product','categories':category})


def delete_product(request):

    if request.method == 'POST':
        product_id =request.POST.get("product_id")

        product = get_object_or_404(Product,pk=product_id)
        product.delete()
        return redirect('app:index')
    
    return render(request, 'app/delete_product.html')