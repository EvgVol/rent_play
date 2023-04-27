from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import UserForm


class SignUp(CreateView):
    """Отображение формы для регистрации пользователей."""

    form_class = UserForm
    success_url = reverse_lazy('core:index')
    template_name = 'users/signup.html'
