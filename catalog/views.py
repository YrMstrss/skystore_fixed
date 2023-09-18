from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from catalog.forms import ProductForm
from catalog.models import Product


def index_contact(request):
    return render(request, "catalog/contact_page.html")


class ProductListView(ListView):
    model = Product


class ProductDetailsView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
