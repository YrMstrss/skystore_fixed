from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import index_contact, index_product, ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', index_contact, name='contact'),
    path('product/<int:pk>', index_product, name='product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
