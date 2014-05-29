from django.forms import widgets
from rest_framework import serializers
from migrations.models import Food, Restaurant



class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('id', 'type', 'country', 'healthiness')


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'type', 'daysopen', 'location', 'derrscore', 'website')

