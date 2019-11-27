import ast
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product, Cart
# Create your views here.

def BasicView(request):
    return HttpResponse("Hi")

def CartForm(request):
    products = []
    
    for p in Product.objects.all():
        products.append(p.name)

    context = {
        'products': products
    }

    return render(request, 'list.html', context=context)

@csrf_exempt
def CartCreation(request):
    products = request.GET.get('products').split(',')
    cart = Cart()
    cart.save()
    total = 0
    for product in products:
        name = product.split()[0]
        quantity = int(product.split()[1])
        prod = Product.objects.get(name=name)
        prod.quantity -= quantity
        total += quantity * prod.price
        cart.products.add(prod)
        prod.save()
    
    cart.total = total
    cart.save()
    return HttpResponse(products.__class__.__name__)
