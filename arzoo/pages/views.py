from django.shortcuts import render,HttpResponse
from products.models import *
from django.http import JsonResponse
import json
from .models import *

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





def add_to_cart(request):
    if request.method == 'POST':
        # Retrieve JSON data from the request body
        data = json.loads(request.body)
        productname = data.get('productname')
        productprice = data.get('productprice')
        integer_price = int(productprice)
        
        # Initialize or retrieve session lists
        namelist = request.session.get('namelist', [])
        pricelist = request.session.get('pricelist', [])
        indexlist = request.session.get('indexlist', [])
        
        # Add product to lists
        namelist.append(productname)
        pricelist.append(integer_price)
        indexlist.append(len(namelist) - 1)  # Index of the newly added item
        
        # Update session data
        request.session['namelist'] = namelist
        request.session['pricelist'] = pricelist
        request.session['indexlist'] = indexlist
        request.session.modified = True
        

        return JsonResponse({'success': True})
        
    else:
        return JsonResponse({'success': False})

def cart(request):
    namelist = request.session.get('namelist', [])
    pricelist = request.session.get('pricelist', [])
    indexlist = request.session.get('indexlist', [])
    popular_items = popular.objects.all()
    baked_and_ready_items = baked_and_ready.objects.all()
    return render(request, 'cart.html',{'popular_items':popular_items,'baked_and_ready_items':baked_and_ready_items,'namelist': namelist, 'pricelist': pricelist,'indexlist':indexlist})



def remove_from_cart(request):
    if request.method == 'POST':
        Data = json.loads(request.body)
        index = Data.get('indexname')
        integer_number = int(index)
        if 'namelist' in request.session and 'pricelist' in request.session and 'indexlist' in request.session:
            # Remove the item at the specified index from both lists
            request.session['namelist'].pop(integer_number)
            request.session['pricelist'].pop(integer_number)
            request.session['indexlist'].pop(integer_number)
            del request.session['indexlist']
            request.session.modified = True

            request.session['indexlist'] = []
            for i in request.session['namelist']:
                a=request.session['namelist'].index(i)
                request.session['indexlist'].append(a)
            request.session.modified = True
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})
