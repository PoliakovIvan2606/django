from django.shortcuts import render
from products.models import ProductCategory, Product


def index(request):
    context = {
        'title':'Store',
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title':'Store-продукты',
        'products': Product.objects.all(),
        'products_category': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)