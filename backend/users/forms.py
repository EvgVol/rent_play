from django.contrib.auth import forms, get_user_model


User = get_user_model()


class UserForm(forms.UserCreationForm):
    """Форма для регистрации новых пользователей."""

    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = ('first_name',
                  'last_name',
                  'username',
                  'email',
                  'role',
                  'birthdate',
                  'avatar',
                  'phone_number',
                  )
