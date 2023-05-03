from django import forms

from .models import Feedback


class FeedbackCreateForm(forms.ModelForm):
    """Форма отправки обратной связи."""

    class Meta:
        model = Feedback
        fields = ('name', 'email', 'subject', 'content')

    def __init__(self, *args, **kwargs):
        """Обновление стилей формы."""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {'class': 'form-control', 'autocomplete': 'off'}
            )
