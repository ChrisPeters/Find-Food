from django.conf.urls.defaults import *

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'findfood.restaurants.views.homepage'),
    (r'^restaurants/(?P<restaurant_id>\d+)/$', 'restaurants.views.detail'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),
)


