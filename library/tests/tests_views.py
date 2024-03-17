from django.test import TestCase

from library.models import Genre


class GenreViewTestCase(TestCase):

    def setUp(self):
        self.url = "/library/genres/"

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        response = self.client.get(self.url)
        context = response.context
        self.assertIn('genres', context)
        genres = context["genres"]
        self.assertEqual(len(genres), 0)
        Genre.objects.create(name="ужасы")
        Genre.objects.create(name='фэнтези')
        response = self.client.get(self.url)
        context = response.context
        genres = context["genres"]
        self.assertEqual(len(genres), 2)
