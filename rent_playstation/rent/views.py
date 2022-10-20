# from django.shortcuts import get_object_or_404, redirect, render
# from django.contrib.auth.decorators import login_required

# from .models import Console, Order
# from .forms import OrderForm


# # Главная страница -------------------------------------------------
# def index(request):
#     """Описывает работу главной страницы."""
#     console_list = Console.objects.select_related('author', 'group').all()
#     context = {'page_obj': paginator_posts(request, post_list)}
#     return render(request, 'posts/index.html', context)
