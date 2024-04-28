from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.

def custombake(request):
    if request.method == 'POST':
        description=request.POST.get('Description')
        image=request.FILES.get('refimage')
        link=request.POST.get('reflink')
        name=request.POST.get('name')
        contact=request.POST.get('phonenumber')
        address=request.POST.get('address')
        order=customorder(description=description,refimage=image,reflink=link,phone=contact,address=address,name=name)
        order.save()
        return render(request,'index.html')
    else:
        return HttpResponse("else is being executed")