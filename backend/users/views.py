from django.contrib.auth import login, get_user_model
from django.http import JsonResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import UserForm

User = get_user_model()

class SignUp(CreateView):
    """Отображение формы для регистрации пользователей."""

    form_class = UserForm
    success_url = reverse_lazy('core:index')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid


def validate_username(request):
    """Проверка доступности логина"""
    username = request.GET.get('username', None)
    response = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)
