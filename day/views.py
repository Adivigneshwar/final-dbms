from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
    title="Home"
    return render(request,"home.html",{"title":title})
def product(request):
    title="Product"
    posts=Post.objects.all()
    return render(request,"Product.html",{"title":title,"item":posts})
def detail(request, id):
    posts = Post.objects.get(pk=id)
    return render(request, 'detail.html', {"item": posts})
def item(request):
    posts=Post.objects.all()
    title="Item"
    return render(request, 'item.html', {"title": title,"item": posts})
def one(request,id):
    posts = Post.objects.filter(id=1) 

    title="one"
    return render(request, '1.html', {"title": title,"item": posts})