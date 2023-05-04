from django import forms

from .models import Feedback


class FeedbackCreateForm(forms.ModelForm):
    """Форма отправки обратной связи."""

    class Meta:
        model = Feedback
        fields = ('name', 'email', 'subject', 'content')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'autocomplete': 'off'}),
        }
