from findfood.restaurants.models import City, State, Building, Location_Name, Restaurant_Name, Restaurant_Type, Style_Of_Food, Main_Combo, Location, Restaurant_Bio, Restaurant

from django.shortcuts import render_to_response

def homepage(request):

    restaurant = Restaurant.objects.order_by('restaurant_bio__restaurant_name')

    return render_to_response('restaurants/homepage.html', {

        'restaurant': restaurant,

    })

def detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    return render_to_response('restaurants/detail.html', {
        'restaurant': restaurant,
    })
