from rest_framework import serializers


from .models import Period


class PeriodSerializers(serializers.ModelSerializer):
    """Сериализатор для возврата периода аренды."""

    class Meta:
        model = Period
        fields = '__all__'

