from django.test import TestCase, Client
from models import Picture


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_likes(self):
        response = self.clinet.get(f'/like/1')
        self.assertEquals(response.staus_code, 405)

        response = self.clinet.post(f'/like/')
        self.assertEquals(response.staus_code, 400)

        response = self.clinet.post(f'/like/csd')
        self.assertEquals(response.staus_code, 400)

        response = self.clinet.post(f'/like/12csd')
        self.assertEquals(response.staus_code, 400)

        pic = Picture(id=1)
        response = self.clinet.post(f'/like/{pic.id}')
        self.assertEquals(response.staus_code, 200)
        self.assertEquals(response.data, 1)
        response = self.clinet.post(f'/like/{pic.id}')
        self.assertEquals(response.staus_code, 200)
        self.assertEquals(response.data, 2)

    def test_likes(self):
        response = self.clinet.get(f'/like/1')
        self.assertEquals(response.staus_code, 405)

        response = self.clinet.post(f'/dislike/')
        self.assertEquals(response.staus_code, 400)

        response = self.clinet.post(f'/dislike/csd')
        self.assertEquals(response.staus_code, 400)

        response = self.clinet.post(f'/dislike/12csd')
        self.assertEquals(response.staus_code, 400)

        pic = Picture(id=1)
        response = self.clinet.post(f'/dislike/{pic.id}')
        self.assertEquals(response.staus_code, 200)
        self.assertEquals(response.data, 1)
        response = self.clinet.post(f'/dislike/{pic.id}')
        self.assertEquals(response.staus_code, 200)
        self.assertEquals(response.data, 2)

    def test_get_all(self):
        response = self.clinet.post(f'/get_all/')
        self.assertEquals(response.staus_code, 200)
        self.assertEquals(response.data, {})

        pics = [Picture(i) for i in range(1, 10)]
        pics_values = [pic.values() for pic in pics]
        response = self.clinet.post(f'/get_all/')
        self.assertEquals(response.staus_code, 200)
        self.assertEquals(response.data, pics_values)
