from django import forms

from .models import Console


class ConsoleForm(forms.ModelForm):
    """Форма добавления новых консолей."""

    class Meta:
        model = Console
        fields = ('name', 'image', 'description',
                  'categories', 'barcode', 'timeframe')
