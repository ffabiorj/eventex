from django.core.exceptions import ValidationError
from django.test import TestCase
from core.models import Speaker, Contact

class ContactMedelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Fabio Oliveira',
            slug='fabio-oliveira',
            photo='http://hbn.link/hb-pic'
        )
    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.EMAIL,
                                         value='fabio@gmail.com.net')

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.PHONE,
                                         value='21-3333-3333')

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E or P"""
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker, kind=Contact.EMAIL,
                                         value='fabio@gmail.com.net')
        self.assertEqual('fabio@gmail.com.net', str(contact))
