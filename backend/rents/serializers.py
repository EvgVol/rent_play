from django.db import models, transaction
from rest_framework import serializers

from users.serializers import UsersSerializer
from .models import Rent



class RentReadSerializers(serializers.ModelSerializer):
    """Сериализатор для возврата списка заказов."""

    user = UsersSerializer(read_only=True)

    class Meta:
        model = Rent
        fields = ('id', 'user', 'console', 'start_date', 'end_date',)


class RentCreateSerializers(serializers.ModelSerializer):
    """Сериализатор для создание заказов."""

    user = UsersSerializer(read_only=True)

    class Meta:
        model = Rent
        fields = ('id', 'user', 'console', 'start_date', 'end_date')
        read_only_fields = ('user',)


    @transaction.atomic
    def create(self, validated_data):
        user = self.context.get('request').user
        rent = Rent.objects.create(user=user, **validated_data)
        rent.save()
        return rent

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return RentReadSerializers(instance, context=context).data
