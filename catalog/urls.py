from django.urls import path

from catalog.views import index_home, index_contact

urlpatterns = [
    path('', index_home),
    path('contacts/', index_contact)
]