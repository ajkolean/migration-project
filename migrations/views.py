from django.shortcuts import render
from django.http import HttpResponse
from models import Food

# Create your views here.
def index(request):
    foods = Food.objects.order_by('type')
    context = {
        'foods': foods
    }
    return render(request, 'index.html', context)

def restaurants(request, 