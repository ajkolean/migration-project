from models import Food, Restaurant
from food.serializers import FoodSerializer, RestaurantSerializer
from rest_framework import generics
from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.


# def index(request):
#     foods = Food.objects.order_by('type')
#     context = {
#         'foods': foods
#     }
#     return render(request, 'index.html', context)

class HomeView(TemplateView):
    template_name = "index.html"


class list_foods(generics.ListAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()

class list_restaurants(generics.ListAPIView):
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        type = self.kwargs['type_name']
        food = Food.objects.get(type=type)
        return food.restaurants.all().order_by('-derrscore')


class restaurant_detail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RestaurantSerializer
    lookup_field = 'name'
    queryset = Restaurant.objects.all()








#def food_type(request, type_name):
#     context = {'foodtype' : type_name}
#
#     try:
#         type = Food.objects.get(type=type_name)
#         restaurants = type.restaurants.all().order_by('-derrscore')
#
#         context['restaurants'] = restaurants
#         context['type'] = type
#
#     except Food.DoesNotExist:
#         pass
#
#     return render(request, 'restaurant.html', context )