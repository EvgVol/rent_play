from django_filters.rest_framework import FilterSet, filters

from .models import Game


class GameFilter(FilterSet):
    """Фильтр для игр."""

    tags = filters.AllValuesMultipleFilter(field_name='tags__slug')

    class Meta:
        model = Game
        fields = ('tags',)
