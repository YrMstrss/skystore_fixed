from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index_contact, ProductListView, ProductDetailsView, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', index_contact, name='contact'),
    path('product/<int:pk>', ProductDetailsView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('edit/<int:pk>', ProductUpdateView.as_view(), name='product_edit'),
]
