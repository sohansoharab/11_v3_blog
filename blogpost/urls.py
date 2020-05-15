from django.urls import path
from blogpost.views import index, blog_page, post

urlpatterns = [
    path('', index, name='home'),
    path('blog/', blog_page, name='blog'),
    path('post/', post, name='post'),
]
