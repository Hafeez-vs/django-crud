from cart.models import Cart
def total(request):
    count=0
    if request.user.is_authenticated:
        u = request.user
        try:
            cart = Cart.objects.filter(user=u)
            for i in cart:
                count = count + i.quantity
        except:
            count = 0
    return {'count':count}