from django.test import TestCase, Client
from .models import Picture
from django.forms.models import model_to_dict


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_likes(self):
        response = self.client.get(f'/like/1')
        self.assertEquals(response.staus_code, 405)

        response = self.client.post(f'/like/')
        print(response)
        self.assertEquals(response.staus_code, 404)

        response = self.client.post(f'/like/csd')
        self.assertEquals(response.staus_code, 404)

        response = self.client.post(f'/like/12csd')
        self.assertEquals(response.staus_code, 404)

        pic = Picture(id=1)
        response = self.client.post(f'/like/{pic.id}')
        self.assertEquals(response.staus_code, 200)
        self.assertEquals(response.data, 1)
        response = self.client.post(f'/like/{pic.id}')
        self.assertEquals(response.staus_code, 200)
        self.assertEquals(response.data, 2)

    def test_dislikes(self):
        response = self.client.get(f'/like/1')
        self.assertEquals(response.staus_code, 405)

        response = self.client.post(f'/dislike/')
        print(response)
        self.assertEquals(response.staus_code, 404)

        response = self.client.post(f'/dislike/csd')
        self.assertEquals(response.staus_code, 400)

        response = self.client.post(f'/dislike/12csd')
        self.assertEquals(response.staus_code, 400)

        pic = Picture(id=1)
        response = self.client.post(f'/dislike/{pic.id}')
        self.assertEquals(response.staus_code, 200)
        self.assertEquals(response.data, 1)
        response = self.client.post(f'/dislike/{pic.id}')
        self.assertEquals(response.staus_code, 200)
        self.assertEquals(response.data, 2)

    def test_get_all(self):
        response = self.client.post(f'/get_all/')
        print(response)
        self.assertEquals(response.staus_code, 200)
        self.assertEquals(response.data, {})

        pics = [Picture(i) for i in range(1, 10)]
        pics_values = [model_to_dict(pic) for pic in pics]
        response = self.client.post(f'/get_all/')
        self.assertEquals(response.staus_code, 200)
        self.assertEquals(response.data, pics_values)
