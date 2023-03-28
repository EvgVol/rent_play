import datetime

from django.db import models, transaction
from rest_framework import serializers, exceptions, status

from core import texts
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
    # start_date = serializers.DataField()
    # end_date = serializers.DateField()

    class Meta:
        model = Rent
        fields = ('id', 'user', 'console', 'start_date', 'end_date')
        read_only_fields = ('user',)

    # def validate(self, data):
    #     super().validate(data)
    #     # check if data is in either the request or instance
    #     start_date, end_date = None, None
    #     if 'start_date' in data:
    #         start_date = data['start_date']
    #     elif self.instance:
    #         start_date = self.instance.start_date

    #     if 'end_date' in data:
    #         end_date = data['end_date']
    #     elif self.instance:
    #         end_date = self.instance.end_date

    #     # this error isn't raised
    #     if not (start_date or end_date):
    #         raise serializers.ValidationError({"date": _('This field is required.')})

    #     return data
    
    # def validate(self, data):
    #     """Проверяем, чтобы приставка была свободна, и невозможно было '
    #     'арендовать у самого себя.
    #     """
    #     author = self.instance
    #     console = self.context.get('console')
    #     user = self.context.get('request').user
    #     if Rent.objects.filter(console=console).all():
    #         raise exceptions.ValidationError(
    #             detail=texts.DUBLICAT_RENTAL,
    #             code=status.HTTP_400_BAD_REQUEST
    #         )
    #     if user == author:
    #         raise exceptions.ValidationError(
    #             detail=texts.SELF_RENTAL,
    #             code=status.HTTP_400_BAD_REQUEST
    #         )
    #     return data

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
