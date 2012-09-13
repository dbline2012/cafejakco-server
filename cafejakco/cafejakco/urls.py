from django.conf.urls import patterns, include, url
from tastypie.api import Api
from community.api import EntryResource, UserResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

jakco_api = Api(api_name = 'jakco')
jakco_api.register(UserResource())
jakco_api.register(EntryResource())


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cafejakco.views.home', name='home'),
    # url(r'^cafejakco/', include('cafejakco.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    
    # REST API
    url(r'^api/', include(jakco_api.urls)),
)
