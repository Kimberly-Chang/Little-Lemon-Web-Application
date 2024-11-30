from django.test import TestCase, Client
from restaurant.models import Menu

class MenuItemsViewTest(TestCase):
    def setUp(self):
        item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        item2 = Menu.objects.create(title="Cake", price=500, inventory=10)
    def test_getall(self):
        client = Client()
        response = client.get('/restaurant/menu/')
        self.assertEqual(response.content,b'{"count":2,"next":null,"previous":null,"results":[{"id":1,"title":"IceCream","price":"80.00","inventory":100},{"id":2,"title":"Cake","price":"500.00","inventory":10}]}')