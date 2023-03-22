from rest_framework import serializers

from .models import TimeRent


class TimeRentSerializer(serializers.ModelSerializer):
    """Сериализатор для периода аренды."""

    class Meta:
        model = TimeRent
        fields = '__all__'
