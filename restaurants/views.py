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

def restaurants(request):
    restaurant = Restaurant.objects.order_by('restaurant_bio__restaurant_name')
    return render_to_response('restaurants/restaurants.html', {
        'restaurant': restaurant,
    })

def cuisine(request):
    cuisine = Style_Of_Food.objects.order_by('style_of_food')
    return render_to_response('restaurants/cuisine.html', {
        'cuisine': cuisine,
    })

def cuisinedetail(request, cuisine_id):
    cuisine = Style_Of_Food.objects.get(id=cuisine_id)
    restaurants = Restaurant.objects.filter(restaurant_bio__style_of_food = cuisine)
    return render_to_response('restaurants/cuisinedetail.html', {
        'cuisine': cuisine,
        'restaurants': restaurants,
    })
def restauranttype(request):
    restauranttype = Restaurant_Type.objects.order_by('restaurant_type')
    return render_to_response('restaurants/restauranttype.html', {
        'restauranttype': restauranttype,
    })

def restauranttypedetail(request, restauranttype_id):
    restauranttype = Restaurant_Type.objects.get(id=restauranttype_id)
    restaurants = Restaurant.objects.filter(restaurant_bio__restaurant_type = restauranttype)
    return render_to_response('restaurants/restauranttypedetail.html', {
        'restauranttype': restauranttype,
        'restaurants': restaurants,
    })

def states(request):
    states = State.objects.order_by('state')
    return render_to_response('restaurants/states.html', {
        'states': states,
    })

def statesdetail(request, states_id):
    states = State.objects.get(id=states_id)
    restaurants = Restaurant.objects.filter(location__state = states)
    return render_to_response('restaurants/statesdetail.html', {
        'states': states,
        'restaurants': restaurants,
    })

