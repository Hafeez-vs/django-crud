from django.contrib import admin
from cart.models import Cart
from cart.models import Account
from cart.models import Order
from django.http import HttpResponse

# Register your models here.
admin.site.register(Cart)
admin.site.register(Account)
admin.site.register(Order)