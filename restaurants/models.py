from django.db import models

class City(models.Model):
    city = models.CharField(max_length=255)
    def get_absolute_url(self):
        return "/city/%i/" % self.id
    def __unicode__(self):
        return self.city

class State(models.Model):
    state = models.CharField(max_length=255)
    def get_absolute_url(self):
        return "/states/%i/" % self.id
    def __unicode__(self):
        return self.state

class Building(models.Model):
    building = models.CharField(max_length=255, blank=True)
    def get_absolute_url(self):
        return "/building/%i/" % self.id
    def __unicode__(self):
        return self.building

class Location_Name(models.Model):
    location_name = models.CharField(max_length=255, blank=True)
    def get_absolute_url(self):
        return "/location_name/%i/" % self.id
    def __unicode__(self):
        return self.location_name

class Restaurant_Name(models.Model):
    restaurant_name = models.CharField(max_length=255)
    def get_absolute_url(self):
        return "/restaurant_name/%i/" % self.id
    def __unicode__(self):
        return self.restaurant_name

class Restaurant_Type(models.Model):
    restaurant_type = models.CharField(max_length=255)
    def get_absolute_url(self):
        return "/restauranttype/%i/" % self.id
    def __unicode__(self):
        return self.restaurant_type

class Style_Of_Food(models.Model):
    style_of_food = models.CharField(max_length=255)
    def get_absolute_url(self):
        return "/cuisine/%i/" % self.id
    def __unicode__(self):
        return self.style_of_food

class Main_Combo(models.Model):
    main_combo = models.CharField(max_length=255, blank=True)
    def get_absolute_url(self):
        return "/main_combo/%i/" % self.id
    def __unicode__(self):
        return self.main_combo

class Location(models.Model):
    location_name = models.ForeignKey(Location_Name)
    building = models.ForeignKey(Building)
    address = models.TextField(blank=True)
    city = models.ForeignKey(City)
    state = models.ForeignKey(State)
    point = models.CharField(max_length=255, blank=True)
    intersection = models.CharField(max_length=255, blank=True)
    def get_absolute_url(self):
        return "/location/%i/" % self.id
    def __unicode__(self):
        return self.location_name.location_name

class Restaurant_Bio(models.Model):
    restaurant_name = models.ForeignKey(Restaurant_Name)
    restaurant_type = models.ForeignKey(Restaurant_Type)
    style_of_food = models.ForeignKey(Style_Of_Food)
    main_combo = models.ForeignKey(Main_Combo)
    price_of_number_one_combo = models.CharField(max_length=255, blank=True)
    grams_of_fat_of_number_one_combo = models.IntegerField(blank=True)
    dollar_menu = models.BooleanField()
    local = models.BooleanField()
    def get_absolute_url(self):
        return "/restaurant_bio/%i/" % self.id
    def __unicode__(self):
        return self.restaurant_name.restaurant_name

class Restaurant(models.Model):
    location = models.ForeignKey(Location)
    restaurant_bio = models.ForeignKey(Restaurant_Bio)
    phone_number = models.CharField(max_length=255, blank=True)
    closing_time = models.CharField(max_length=255, blank=True)
    drive_thru = models.BooleanField()
    delivery = models.BooleanField()
    notes = models.TextField(blank=True)
    def get_absolute_url(self):
        return "/restaurants/%i/" % self.id
    def __unicode__(self):
        return self.restaurant_bio.restaurant_name.restaurant_name


