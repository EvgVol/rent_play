from django import forms
from django.core.exceptions import ValidationError

from .models import Feedback


class FeedbackCreateForm(forms.ModelForm):
    """Форма отправки обратной связи."""

    class Meta:
        model = Feedback
        fields = ('name', 'email', 'phone', 'body', 'consent')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'consent': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_consent(self):
        if not self.cleaned_data.get('consent'):
            raise ValidationError("Необходимо дать согласие на обработку персональных данных!")
        return self.cleaned_data['consent']
