from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from shop.models import Product
from cart.models import Cart,Order,Account
from django.http import HttpResponse

# Create your views here.
@login_required
def addtocart(request,p):
    p=Product.objects.get(id=p)
    u=request.user
    try:
        cart=Cart.objects.get(user=u,product=p)
        if(p.stock>0):
            cart.quantity+=1
            cart.save()
            p.stock -= 1
            p.save()
    except:
        if(p.stock>0):
            cart=Cart.objects.create(product=p,user=u,quantity=1)
            cart.save()
            p.stock -= 1
            p.save()
    return cart_view(request)

@login_required
def cart_view(request):
    u=request.user
    total=0
    cart = Cart.objects.filter(user=u)
    for i in cart:
        total=total+i.quantity*i.product.price
    return render(request,'addtocart.html',{'cart':cart,'total':total})

def cartremove(request,p):
    p=Product.objects.get(id=p)
    u=request.user
    try:
        cart = Cart.objects.get(user=u, product=p)
        if(cart.quantity>1):
            cart.quantity -= 1
            cart.save()
            p.stock += 1
            p.save()
        else:
            cart.delete()
            p.stock+=1
            p.save()
    except:
        pass
    return cart_view(request)

def cartdelete(request,p):
    p=Product.objects.get(id=p)
    u=request.user
    try:
        cart = Cart.objects.get(user=u, product=p)
        cart.delete()
        p.stock += cart.quantity
        p.save()
    except:
        pass
    return cart_view(request)
@login_required
def orderform(request):
    if(request.method=='POST'):
        phone=request.POST['ph']
        address=request.POST['ad']
        accnum=request.POST['ac']
        u=request.user
        cart=Cart.objects.filter(user=u)
        total=0
        for i in cart:
            total=total+i.quantity*i.product.price
        try:
            acc=Account.objects.get(acctnum=accnum)
            if(acc.amount >= total):
                acc.amount=acc.amount-total
                acc.save()
                for i in cart:
                    o=Order.objects.create(user=u,product=i.product,address=address,phone=phone,no_of_items=i.quantity,order_status='paid')
                    o.save()
                cart.delete()
                msg="ORDER PLACED SUCCESSFULLY"
                return render(request, 'orderdetail.html', {'msg': msg})
            else:
                msg="INSUFFICIENT BALANCE"
                return render(request, 'orderdetail.html', {'msg': msg})
        except:
            pass
    return render(request, 'orderform.html')

def orderview(request):
    u=request.user
    cart=Order.objects.filter(user=u)
    return render(request,'orderview.html',{'cart':cart})
