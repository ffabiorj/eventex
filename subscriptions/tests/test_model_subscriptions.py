from django.test import TestCase
from subscriptions.models import Subscription
from datetime import datetime

class SubscriptionModel(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Fabio Oliveira',
            cpf='12345678901',
            email='fabiorj@com.br',
            phone='3333-2222'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr..."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Fabio Oliveira', str(self.obj))