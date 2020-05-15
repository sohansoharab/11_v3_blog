from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'blogpost/index.html')


def blog_page(request):
    return render(request, 'blogpost/blog.html')


def post(request):

    return render(request, 'blogpost/post.html')
