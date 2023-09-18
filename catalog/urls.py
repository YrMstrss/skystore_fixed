from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index_contact, ProductListView, ProductDetailsView, ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', index_contact, name='contact'),
    path('product/<int:pk>', ProductDetailsView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
]
