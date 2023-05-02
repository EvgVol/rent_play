from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.conf import settings

from blog.models import Post
from games.models import Tag, Genre


def blog(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    tags = Tag.objects.all()
    genres = Genre.objects.all()
    context = {'page_obj': page_obj,
               'tags': tags,
               'genres': genres}
    template = 'blog/blog.html'
    return render(request, template, context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    template = 'blog/single-post.html'
    context = {
        'author': post.author,
        'post': post,
    }
    return render(request, template, context)