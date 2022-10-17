from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from rent.models import Console, Cost, RentalRate, Order, User


class ConsoleSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = Console
        fields = '__all__'


class RentalRateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RentalRate
        fields = '__all__'


class CostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cost
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('console',)
