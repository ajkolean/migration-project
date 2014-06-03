from django.test import TestCase
from models import Food, Restaurant
from rest_framework.test import APITestCase
from food.serializers import FoodSerializer, RestaurantSerializer


# Create your tests here.
class FoodTestCase(TestCase):
    def setUp(self):
        Food.objects.create(type="healthy", country="someplace", healthiness=0)
        Food.objects.create(type="unhealthy", country="someotherplace", healthiness=2)

    def test_health(self):
        healthy = Food.objects.get(type="healthy")
        unhealthy = Food.objects.get(type="unhealthy")
        self.assertEqual(healthy.health(), "this food is fine for you")
        self.assertEqual(unhealthy.health(), "this food is unhealthy")



class test_responses(APITestCase):
    def setUp(self):
        Food.objects.create(type="test_food", country="test_country", healthiness=1)
        food = Food.objects.get(type="test_food")
        Restaurant.objects.create(name="test_place", type=food, daysopen="monday", location="home", derrscore=4, website="test1.com")

    def test_food_response(self):
        response = self.client.get("http://127.0.0.1:8000/foods/")
        self.assertEqual(response.data, [{"id": 3, "type": "test_food", "country": "test_country", "healthiness": 1}])

    def test_restaurant_response(self):
        response = self.client.get("/restaurants/test_food/")
        self.assertEqual(response.data, [{'id': 2, 'name': 'test_place', 'type': 4, 'daysopen': 'monday', 'location': 'home', 'derrscore': 4.0, 'website': 'test1.com'}])


class test_serializers(TestCase):
    def setUp(self):
        Food.objects.create(type="test_food", country="test_country", healthiness=1)
        food = Food.objects.get(type="test_food")
        Restaurant.objects.create(name="test_place", type=food, daysopen="monday", location="home", derrscore=4, website="test1.com")
        rest = Restaurant.objects.get(name="test_place")

    def test_food_serializer(self):
        food = Food.objects.get(type="test_food")
        serializer = FoodSerializer()
        self.assertEqual(1, 0)
