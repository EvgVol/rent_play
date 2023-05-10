import re

from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import (PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.views.generic import CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.db import transaction

from .forms import UserSignUpForm, UserUpdateForm


User = get_user_model()


class SignUp(CreateView):
    """Отображение страницы для регистрации пользователей."""

    form_class = UserSignUpForm
    success_url = reverse_lazy('core:index')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid


class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'


class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy('core:password_change_done')
    template_name = 'users/password_change_form.html'


class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'


class PasswordResetConfirm(PasswordResetConfirmView):
    success_url = reverse_lazy('core:password_reset_complete')
    template_name = 'users/password_reset_confirm.html'


class PasswordResetDone(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class PasswordReset(PasswordResetView):
    success_url = reverse_lazy('core:password_reset_done')
    template_name = 'users/password_reset_form.html'


class ProfileView(DetailView):
    """Отображение страницы пользователя."""

    model = User
    template_name = 'users/profile.html'


class ProfileUpdateView(UpdateView):
    """Отображение страницы редактирования профиля пользователя."""

    model = User
    form_class = UserUpdateForm
    template_name = 'users/profile_edit.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование профиля пользователя: {self.request.user.username}'
        form = kwargs.get('form')
        if not form:
            form = self.form_class(instance=self.request.user)
        context['user_form'] = form
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        user_form = context['user_form']
        with transaction.atomic():
            if all([form.is_valid(), user_form.is_valid()]):
                user_form.save()
                form.save()
            else:
                context.update({'user_form': user_form})
                return self.render_to_response(context)
        return super(ProfileUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('core:profile', kwargs={'pk': self.object.pk})

# def validate_username(request):
#     """Проверка доступности логина"""
#     username = request.GET.get('username', None)
#     response = {
#         'is_taken': User.objects.filter(username__iexact=username).exists()
#     }
#     return JsonResponse(response)
