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


    if type_name == 'italian':
        type_id = 1
    elif type_name == 'mexican':
        type_id = 4
    elif type_name == 'american':
        type_id = 5
    elif type_name == 'chinese':
        type_id = 6
    elif type_name == 'japanese':
        type_id = 7
    elif type_name == 'mediterranean':
        type_id = 8
    elif type_name == 'deli':
        type_id = 9
    elif type_name == 'greek':
        type_id = 10


    try:
        type = Food.objects.get(type=type_name)

        restaurants = Restaurant.objects.filter(type_id=type_id).order_by('-derrscore')

        context['restaurants'] = restaurants
        context['type'] = type

    except Food.DoesNotExist:
        pass

    return render(request, 'restaurant.html', context )
