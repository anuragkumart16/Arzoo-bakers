from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib import messages



# Create your views here.

def custombake(request):
    if request.method == 'POST':
        description=request.POST.get('Description')
        image=request.FILES.get('refimage')
        link=request.POST.get('reflink')
        name=request.POST.get('name')
        phone=request.POST.get('phonenumber')
        address=request.POST.get('address')
        order=customorder(description=description,refimage=image,reflink=link,phone=phone,address=address,name=name)
        order.save()
        messages.add_message(request, messages.INFO, "Order has been placed!")
        return redirect('home')
    else:
        return HttpResponse("else is being executed")