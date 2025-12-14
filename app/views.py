
from django.views.generic import TemplateView, ListView, DetailView,CreateView, DeleteView, UpdateView
from django.shortcuts import get_object_or_404, redirect
from .models import Category, Product
from .forms import ProductForm, CategoryForm,CommentForm, AboutForm
from django.shortcuts import render
from django.urls import reverse_lazy

# # Create your views here.
# def index(request):
#     # search_query = request.GET.get('q','')
#     # filter_type = request.GET.get('filter_type','')
    
#     # categories = Category.objects.all()
    
#     # if category_id:
#     #     products = Product.objects.filter(category = category_id)
#     # else:
#     #     products = Product.objects.all()
        
#     # if search_query:
#     #     products = products.filter(Q(name__icontains = search_query) | Q(description__icontains=search_query))

        
#     # if filter_type == 'expensive':
#     #     products = products.order_by('-price')
        
#     # elif filter_type == 'cheap':
#     #     products = products.order_by('price')
        
#     # else:
#     #     products = Product.objects.all()
    
#     category = Category.objects.all()
#     product = Product.objects.all()
#     context = {
#         'categories':category,
#         'products':product
#     }
#     return render(request, 'app/home.html',context)



# def detail(request, product_id):
#     product = get_object_or_404(Product, id=product_id)

#     if request.method == "POST":
#         if 'comment_form' in request.POST:
#          form = CommentForm(request.POST, request.FILES)
#          if form.is_valid():
#             comment = form.save(commit=False)
#             comment.product = product
#             comment.save()
#             product.rating_upd()
#             return redirect('app:detail', product_id=product.id)


     
#         else:
#          form = CommentForm()

#     else:
#         form = CommentForm()
#     comments = product.comments.all()
#     return render(request, 'app/detail.html', {'product': product,'comments': comments,'form': form})





# def create_product(request):
#     category = Category.objects.all()

#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():  
#             form.save()     
#             return redirect('app:index') #har bir ozagrishlardan keyin bosh sahifaga kochishni qoshdim
        
#     else:
#         form = ProductForm()
#     return render(request, 'app/crud/create_product.html', {'form': form, 'categories':category})



# def delete_product(request):

#     if request.method == 'POST':
#         product_id =request.POST.get("product_id")

#         product = get_object_or_404(Product,pk=product_id)
#         product.delete()
#         return redirect('app:index')
    
#     return render(request, 'app/crud/delete_product.html')


# # def create_product(request)


# def product_update(request):
#     product = None
#     form = None

#     if request.method == 'POST':
 
#         if 'load' in request.POST:
#             product_id = request.POST.get('product_id')
#             product = get_object_or_404(Product, id=product_id)
#             form = ProductForm(instance=product)

#         elif 'save' in request.POST:
#             product_id = request.POST.get('product_id')
#             product = get_object_or_404(Product, id=product_id)
#             form = ProductForm(request.POST, request.FILES, instance=product) #yangi productni yaratishni orniga, uni edit qilish uchun instanveni ishlatdim
#             if form.is_valid():
#                 form.save()
#                 return redirect('app:index')

#     return render(request, 'app/product_update.html', {'product': product, 'form': form})



# def create_category(request):
#     if request.method == 'POST':
#           form = CategoryForm(request.POST)
#           if form.is_valid():
#               form.save()
#               return redirect('app:index')
    
#     else:
#         form = CategoryForm()

#     return render(request, 'app/crud/create_category.html', {'form': form})



# def info(request):
#     product =  Product.objects.all()
#     return render(request, 'app/info.html' , {'products':product})




# def about(request):
#     if request.method == 'POST':
#         form = AboutForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('app:index')
        

#     else:
#         form = AboutForm()
#     return render(request, 'app/about.html', {'form':form})






# Create your views here.
class Index(ListView):
    model = Product
    template_name = 'app/home.html'
    context_object_name = 'products'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ProductDetai(DetailView):
    model = Product
    template_name = 'app/detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['form'] = CommentForm()
        return context
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = self.object
            comment.save()
            self.object.rating_upd()
        return redirect('app:detail', product_id=self.object.id)


class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'app/crud/create_product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
class ProductDelete(DeleteView):
    model = Product
    template_name = 'app/crud/delete_product.html'
    success_url = reverse_lazy('app:index')


# def create_product(request)
class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'app/product_update.html'
    success_url = reverse_lazy('app:index')

class CategoryCreate(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'app/crud/create_category.html'
    success_url = reverse_lazy('app:index')


class About(CreateView):
    form_class = AboutForm
    template_name = 'app/about.html'
    success_url = reverse_lazy('app:index')