from django.test import TestCase

from rest_framework.test import APIClient
from restaurant.models import Menu

class MenuViewTest(TestCase):

    def setUp(self):
        self.item1 = Menu.objects.create(title = 'First', price = 10, inventory = 100)
        self.item2 = Menu.objects.create(title = 'Second', price = 10, inventory = 100)
        self.client = APIClient()

    def test_getall(self):
        response = self.client.get('/api/menu/')
        data = response.json()

        self.assertEqual(len(data), 2)