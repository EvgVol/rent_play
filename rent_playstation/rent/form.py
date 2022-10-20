from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    """Форма создание заказа."""

    class Meta:
        model = Order
        fields = ('console', 'created_at', 'updated_at',)
        labels = {
            "console": "Приставка",
            "created_at": "Дата начало аренды",
            'updated_at': 'Дата окончание аренды'
        }
        help_texts = {
            'text': 'Выберите приставку',
            'group': 'Укажите начало даты аренды',
            'image': 'Укажите окончание даты аренды'
        }
