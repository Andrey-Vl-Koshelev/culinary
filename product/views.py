from django.shortcuts import render, get_object_or_404
from .models import Product

def products(request):
    product = Product.objects.order_by('-date')
    return render(request, 'product/products.html', {'products': product})

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product/details.html', {'product': product})
