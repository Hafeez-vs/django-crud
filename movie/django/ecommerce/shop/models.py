from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField()
    image=models.ImageField(upload_to='image',null=True,blank=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField()
    image=models.ImageField(upload_to='products',null=True,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    avaliable=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Register(models.Model):
    username=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    def __str__(self):
        return self.username
