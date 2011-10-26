from restaurants.models import City
from restaurants.models import State
from restaurants.models import Building
from restaurants.models import Location_Name
from restaurants.models import Restaurant_Name
from restaurants.models import Restaurant_Type
from restaurants.models import Style_Of_Food
from restaurants.models import Main_Combo
from restaurants.models import Location
from restaurants.models import Restaurant_Bio
from restaurants.models import Restaurant
from django.contrib import admin

admin.site.register(Restaurant)
admin.site.register(Restaurant_Bio)
admin.site.register(Restaurant_Name)
admin.site.register(Restaurant_Type)
admin.site.register(Style_Of_Food)
admin.site.register(Main_Combo)
admin.site.register(Location)
admin.site.register(Location_Name)
admin.site.register(Building)
admin.site.register(City)
admin.site.register(State)
