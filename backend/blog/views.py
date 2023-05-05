from django.views.generic import ListView, DetailView

from blog.models import Post
from games.models import Tag, Genre


class BlogListView(ListView):
    """Отображает страницу блога с 8 постами."""

    model = Post
    template_name = "blog/blog.html"
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['genres'] = Genre.objects.all()
        return context


class BlogDetailView(DetailView):
    """Отображает страницу блога с данным постом"""

    model = Post
    template_name = "blog/single-post.html"

