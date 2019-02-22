from django.test import TestCase
from core.models import Talk


class TalkModelTalk(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title='Título da Palestra',
        )

        def test_create(self):
            self.assertTrue(Talk.objects.exists())

        def test_has_speaker(self):
            self.talk.speakers.create(
                name='Henrique Bastos',
                slug='henrique-bastos',
                website='http://henriquebastos.net'
            )
            self.assertEqual(1, self.talk.speakers.count())

        def test_description_blank(self):
            field = Talk._meta.get_field('description')
            self.assertTrue(field.blank)

        def test_speakers_blank(self):
            field = Talk._meta_get_field('speakers')
            self.assertTrue(field.blank)

        def test_start_blank(self):
            field = Talk._meta_get_field('start')
            self.assertTrue(field.blank)

        def test_start_null(self):
            field = Talk._meta_get_field('start')
            self.assertTrue(field.null)
        
        def test_str(self):
            self.assertEqual('Teste de Palestra', str(self.talk))
