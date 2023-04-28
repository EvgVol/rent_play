import re

from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import (PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.http import JsonResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy

from core.enum import Regex
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


class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'


class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy('users:password_change_done')
    template_name = 'users/password_change_form.html'


class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'


class PasswordResetConfirm(PasswordResetConfirmView):
    success_url = reverse_lazy('users:password_reset_complete')
    template_name = 'users/password_reset_confirm.html'


class PasswordResetDone(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class PasswordReset(PasswordResetView):
    success_url = reverse_lazy('core:password_reset_done')
    template_name = 'users/password_reset_form.html'


# def validate_username(request):
#     """Проверка доступности логина"""
#     username = request.GET.get('username', None)
#     response = {
#         'is_taken': User.objects.filter(username__iexact=username).exists()
#     }
#     return JsonResponse(response)
