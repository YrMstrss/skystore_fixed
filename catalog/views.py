from django.shortcuts import render

from catalog.models import Product


def index_home(request):
    product = Product.objects.all()
    context = {
        'object_list': product
    }
    return render(request, "catalog/home_page.html", context)


def index_contact(request):
    return render(request, "catalog/contact_page.html")


def index_product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'object': product,
        'title': f'Товар - {product.name}'
    }
    return render(request, "catalog/product_page.html", context)
