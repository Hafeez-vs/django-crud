from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

# Create your views here.
def searchproducts(request):
    if(request.method=="POST"):
        q=""
        query=request.POST['q']
        if(query):
            p=Product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))
    return render(request,'searchproducts.html',{'p':p,'q':q})