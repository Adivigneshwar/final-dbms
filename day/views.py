from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import Login, RegisterForm
from django.core.paginator import Paginator  # Corrected import
from django.contrib import messages
from .cart import Cart
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    title = "Home"  # Corrected variable
    return render(request, "home.html", {"title": title})

def product(request):
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, 4)  # Corrected import used
    page_no = request.GET.get('page')
    page_obj = paginator.get_page(page_no)
    return render(request, "Product.html", {"title": "Product", "page_obj": page_obj})

def detail(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'detail.html', {"item": post})

def item(request):
    posts = Post.objects.all()
    return render(request, 'item.html', {"title": "Item", "item": posts})

def category_view(request, id):
    posts = Post.objects.filter(cate_id=id)  # Filter by cate_id
    return render(request, f"{id}.html", {"title": f"Category {id}", "item": posts})
def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,"Succesfully Created ")
            return redirect("login")
    return render(request, "register.html", {"form": form})
def login(request):
    form = Login()
    if request.method =="POST":
        form = Login(request.POST) 
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                auth_login(request,user)
                return redirect("dashboard")
    return render(request,'login.html', {"form": form})
def cart_add(request):
    # Get the cart
    cart = Cart(request)

    # test for POST
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))

        # lookup product in DB
        product = get_object_or_404(Post, id=product_id)

        # Save to session
        cart.add(product=product)

        # Return response
        response = JsonResponse({'Product Name: ': product.name})
        return response
def dashboard (request):
    blog_title="My Orders"
    return render(request,"dashboard.html",{"blog_title":blog_title})
def logout(request):
    auth_logout(request)
    return render(request,"Home.html")

def cart_add(request):
    # Get the cart
    cart = Cart(request)

    # test for POST
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))

        # lookup product in DB
        product = get_object_or_404(Post, id=product_id)

        # Save to session
        cart.add(product=product)

        # Return response
        response = JsonResponse({'Product Name: ': product.name})
        return response
def one(request):
    posts = Post.objects.all()
    return render(request, "1.html", {'item': posts})  # Pass the posts as 'item'
def two(request):
    posts = Post.objects.all()
    return render(request,"2.html")
def three(request):
    posts = Post.objects.all()
    return render(request,"3.html")
def four(request):
    posts = Post.objects.all()
    return render(request,"4.html")
def five(request):
    posts = Post.objects.all()
    return render(request,"5.html")
def six(request):
    posts = Post.objects.all()
    return render(request,"6.html")
def map(request):
    return render(request,"map.html")