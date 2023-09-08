from django.urls import path

from blog.views import BlogListView, BlogCreateView

urlpatterns = [
    path('blog/', BlogListView.as_view(), name='home'),
    path('blog/create/', BlogCreateView.as_view(), name='create_blog'),
]