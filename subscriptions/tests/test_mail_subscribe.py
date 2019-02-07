from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r

class SubscribePostvalid(TestCase):
    def setUp(self):
        data = dict(name='Fabio Oliveira', cpf='12345678901',
                    email='fabio-oliveira@gmail.com', phone='21-3355-5566')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'fabio-oliveira@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Fabio Oliveira',
            '12345678901',
            'fabio-oliveira@gmail.com',
            '21-3355-5566'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)