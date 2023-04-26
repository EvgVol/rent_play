from django.shortcuts import render

from blog.models import Post
from games.models import Tag


def index(request):
    template = 'core/index.html'
    return render(request, template)


def about(request):
    template = 'core/about.html'
    return render(request, template)


def services(request):
    template = 'core/services.html'
    return render(request, template)


def contacts(request):
    template = 'core/contact.html'
    return render(request, template)


def products(request):
    template = 'consoles/products.html'
    return render(request, template)


def product_list(request):
    template = 'consoles/product-list.html'
    return render(request, template)


def product_detail(request):
    template = 'consoles/product-detail.html'
    return render(request, template)


def cart(request):
    template = 'consoles/cart.html'
    return render(request, template)


def checkout(request):
    template = 'consoles/checkout.html'
    return render(request, template)


def work(request):
    template = 'games/work.html'
    return render(request, template)


def work_detail(request):
    template = 'games/work-detail.html'
    return render(request, template)


def blog(request):
    post_list = Post.objects.all()
    tags = Tag.objects.all()
    context = {'post_list': post_list}
    template = 'blog/blog.html'
    return render(request, template, context)


def post(request):
    template = 'blog/single-post.html'
    return render(request, template)
