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
