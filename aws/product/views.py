from django.shortcuts import render,redirect
from .models import Products
from .forms import ProductsForm


# Create your views here.
def home(request):
    contex = {"title":"Product Home",
            "products":Products.objects.all()}
    return render(request,'product/home.html',contex)

def create(request):
    if request.method == "POST":
        form = ProductsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product-home')
    else:
        form = ProductsForm()
    return render(request,'product/create.html',{"title":"Product Creation","form":form})

def edit(request,id):
    instance = Products.objects.get(id=id)
    if request.method == "POST":
        form = ProductsForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            return redirect("/product/")
    else:
        form = ProductsForm(instance=instance)

    return render(request,'product/edit.html',{"title":"Product Edit","form":form})

def delete(request,id):
    Products.objects.get(id=id).delete()
    return redirect()

