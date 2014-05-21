from django.shortcuts import render
from django.http import HttpResponse
from models import Food, Restaurant

# Create your views here.
def index(request):
    foods = Food.objects.order_by('type')
    context = {
        'foods': foods
    }
    return render(request, 'index.html', context)

def food_type(request, type_name):
    context = {'foodtype' : type_name}

    try:
        type = Food.objects.get(type=type_name)
        restaurants = type.restaurants.all().order_by('-derrscore')

        context['restaurants'] = restaurants
        context['type'] = type

    except Food.DoesNotExist:
        pass

    return render(request, 'restaurant.html', context )
