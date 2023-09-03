from django.shortcuts import render


def index_home(request):
    return render(request, "catalog/home_page.html")


def index_contact(request):
    return render(request, "catalog/contact_page.html")
