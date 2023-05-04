from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.forms import ModelForm


User = get_user_model()


class UserSignUpForm(UserCreationForm):
    """Форма для регистрации новых пользователей."""

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
        labels = {
            "first_name": "Имя",
            "last_name": "Фамилия",
            "username": "Ник",
            "email": "E-Mail"
        }


class UserUpdateForm(ModelForm):
    """Форма обновления данных пользователя."""

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'birthdate', 'avatar',
                  'phone_number')

    def __init__(self, *args, **kwargs):
        """Обновление стилей формы под bootstrap."""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    def get_object(self, queryset=None):
        return self.request.user.profile

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username__iexact=username).exclude(username=username).exists()
        if user:
            raise ValidationError("Пользователь с таким именем уже существует.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        user = User.objects.filter(email__iexact=email).exclude(username=username).exists()
        if user:
            raise ValidationError("Пользователь с таким email уже существует.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        username = self.cleaned_data.get('username')
        user = User.objects.filter(phone_number__iexact=phone_number).exclude(username=username).exists()
        if user:
            raise ValidationError("Пользователь с таким номером телефона уже существует.")
        return phone_number
