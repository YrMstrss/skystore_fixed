from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import index_contact, ProductListView, ProductDetailsView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', index_contact, name='contact'),
    path('product/<int:pk>', cache_page(60)(ProductDetailsView.as_view()), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('edit/<int:pk>', ProductUpdateView.as_view(), name='product_edit'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('category/', CategoryListView.as_view(), name='category_list'),
]
