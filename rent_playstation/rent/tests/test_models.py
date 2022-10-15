from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Order, Console, RentalRate

User = get_user_model()


class OrderModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='pers')
        cls.console = Console.objects.create(
            title='PlayStayion 4 Slim',
            slug='ps4_slim',
            description='Тестовое описание'
        )
        cls.rental_rate = RentalRate.objects.create(
            time='Неделя',
            cost=3000
        )
        cls.order = Order.objects.create(
            period=cls.rental_rate,
            console=cls.console
        )

    def test_help_text_order(self):
        field_help_texts = {
            'period': 'Укажите срок аренды',
            'console': 'Выберите приставку',
        }
        for field, expected_value in field_help_texts.items():
            with self.subTest(field=field):
                self.assertEqual(
                    self.order._meta.get_field(field)
                        .help_text, expected_value)
