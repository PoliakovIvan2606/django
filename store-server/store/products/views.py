from django.shortcuts import render


def index(request):
    context = {
        'title':'Store',
    }
    return render(request, 'products/index.html',context)

def products(request):
    context = {
        'title':'Store-продукты',
    }
    return render(request, 'products/products.html', context)