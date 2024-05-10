from django.shortcuts import render,redirect
from django.http import HttpResponse
from shop.models import Category
from shop.models import Product
from shop.models import Register
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Category
@login_required
def allcategories(request):
    c=Category.objects.all()
    return render(request,'category.html',{'c':c})
@login_required
def allproducts(request,p):
    c=Category.objects.get(id=p)
    p=Product.objects.filter(category=c)
    return render(request,'product.html',{'c':c,'p':p})
@login_required
def detail(request,p):
    p=Product.objects.get(id=p)
    return render(request,'detail.html',{'p':p})

def reg(request):
    if(request.method=='POST'):
        username=request.POST['u']
        password=request.POST['p']
        confirm=request.POST['cp']
        email=request.POST['e']
        if(confirm==password):
            u=User.objects.create_user(username=username,password=password,email=email)
            u.save()
            return redirect('shop:allcategories')
        else:
            return HttpResponse("passwords are not same")
    return render(request,'reg.html')

def user_login(request):
    if(request.method=='POST'):
        username=request.POST['u']
        password=request.POST['p']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('shop:allcategories')
        else:
            return HttpResponse("invalid credentials")
    return render(request,'login.html')
@login_required
def user_logout(request):
    logout(request)
    return user_login(request)
def home(request):
    return render(request,'home.html')