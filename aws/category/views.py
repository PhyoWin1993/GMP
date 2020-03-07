from django.shortcuts import render

# Create your views here.

def create_all(request):
    return render(request,'category/all.html')

def create(request):
    return render(request,'category/create.html')

def edit(request):
    return render(request,'category/edit.html')

def delete(request):
    return render(request,'category/all.html')

