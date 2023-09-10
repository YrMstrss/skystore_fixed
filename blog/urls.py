from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView

app_name = BlogConfig.name

urlpatterns = [
    path('blog/', BlogListView.as_view(), name='list'),
    path('blog/create/', BlogCreateView.as_view(), name='create_blog'),
]