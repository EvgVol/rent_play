from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from blog.models import Post
from games.models import Tag, Genre
from .forms import PostForm


class BlogListView(ListView):
    """Отображает страницу блога с 8 постами."""

    model = Post
    template_name = "blog/blog.html"
    paginate_by = 8
    ordering = '-pub_date'

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_slug = self.request.GET.get('tag')
        genre_slug = self.request.GET.get('genre')
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            queryset = queryset.filter(tags=tag)
        if genre_slug:
            genre = get_object_or_404(Genre, slug=genre_slug)
            queryset = queryset.filter(genre=genre)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['genres'] = Genre.objects.all()
        return context


class BlogDetailView(DetailView):
    """Отображает страницу блога с данным постом"""

    model = Post
    template_name = "blog/single-post.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/auth/login/'
    model = Post
    form_class = PostForm
    template_name = "blog/post_new.html"
    success_url = reverse_lazy('core:blog-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return self.success_url
 
class PostEditView(UpdateView):
    model = Post
    template_name = "blog/post_new.html"
    fields = ['name', 'description', 'game', 'image']