from django.shortcuts import render

from blog.models import Post
from games.models import Tag


def blog(request):
    post_list = Post.objects.all()
    tags = Tag.objects.all()
    context = {'post_list': post_list}
    template = 'blog/blog.html'
    return render(request, template, context)


def post(request):
    template = 'blog/single-post.html'
    return render(request, template)