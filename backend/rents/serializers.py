import datetime

from django.db import models, transaction
from rest_framework import serializers, exceptions, status, relations

from core import texts
from consoles.models import Console
from users.serializers import UsersSerializer
from .models import Rent


class RentReadSerializers(serializers.ModelSerializer):
    """Сериализатор для возврата списка заказов."""

    user = UsersSerializer(read_only=True)
    tental_time = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Rent
        fields = ('id', 'user', 'console', 'start_date',
                  'end_date', 'tental_time')

    def get_tental_time(self, obj):
        """Достаем количество дней аренды."""
        return (obj.end_date - obj.start_date).days
    
    # def validate(self, data):
    #     start_date = self.instance
    #     end_date = self.instance
    #     if (
    #         start_date < datetime.date.today() 
    #         or start_date == end_date 
    #         or end_date < start_date
    #     ):
    #         raise exceptions.ValidationError(
    #             detail='Проверьте правильно ли вы указали период аренды',
    #             code=status.HTTP_400_BAD_REQUEST
    #         )
    #     return data
    


class RentCreateSerializers(serializers.ModelSerializer):
    """Сериализатор для создание заказов."""

    user = UsersSerializer(read_only=True)
    console = relations.PrimaryKeyRelatedField(
        queryset=Console.objects.all()
    )
    start_date = serializers.DateField()
    end_date = serializers.DateField()

    class Meta:
        model = Rent
        fields = ('id', 'user', 'console', 'start_date', 'end_date')
        read_only_fields = ('user',)

    def validate(self, data):
        author = self.instance
        user = self.context.get('request').user
        if (data['start_date'] > data['end_date']
            or data['start_date'] == data['end_date']
            or data['start_date'] < datetime.date.today()):
            raise serializers.ValidationError(texts.ERROR_TIME)
        if user == author:
            raise exceptions.ValidationError(texts.ERROR_TIME)
        return data

    def validate_console(self, value):
        """Проверяем, чтобы приставка была свободна."""
        if Rent.objects.filter(console=value).all():
            raise exceptions.ValidationError(texts.DUBLICAT_RENTAL)
        return value

    @transaction.atomic
    def create(self, validate):
        user = self.context.get('request').user
        rent = Rent.objects.create(user=user, **validate)
        rent.save()
        return rent

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return RentReadSerializers(instance, context=context).data
