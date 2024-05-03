from django.shortcuts import render
from products.models import *

# Create your views here.
def home(request):
    popular_items = popular.objects.all()
    baked_and_ready_items = baked_and_ready.objects.all()
    return render(request,"index.html",{'popular_items':popular_items,'baked_and_ready_items':baked_and_ready_items})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def customcakeform(request):
    return render(request,'customform.html')

def product(request):
    popular_items = popular.objects.all()
    baked_and_ready_items = baked_and_ready.objects.all()
    return render(request,"product.html",{'popular_items':popular_items,'baked_and_ready_items':baked_and_ready_items})


def cart(request):
    return render(request,'cart.html')

def addtocart(request):
    pass