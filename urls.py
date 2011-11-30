from django.conf.urls.defaults import *

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'findfood.restaurants.views.homepage'),
    (r'^restaurants/(?P<restaurant_id>\d+)/$', 'restaurants.views.detail'),
    (r'^restaurants/$', 'restaurants.views.restaurants'),
    (r'^cuisine/$', 'restaurants.views.cuisine'),
    (r'^cuisine/(?P<cuisine_id>\d+)/$', 'restaurants.views.cuisinedetail'),
    (r'^restauranttype/$', 'restaurants.views.restauranttype'),
    (r'^restauranttype/(?P<restauranttype_id>\d+)/$', 'restaurants.views.restauranttypedetail'),
    (r'^states/$', 'restaurants.views.states'),
    (r'^states/(?P<states_id>\d+)/$', 'restaurants.views.statesdetail'),



    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),
)

