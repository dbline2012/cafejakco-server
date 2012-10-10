from django.conf.urls import patterns, include, url
#from tastypie.api import Api
#from community.api import EntryResource, UserResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#jakco_api = Api(api_name = 'jakco')
#jakco_api.register(UserResource())
#jakco_api.register(EntryResource())


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cafejakco.views.home', name='home'),
    # url(r'^cafejakco/', include('cafejakco.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    
    # REST API
    #url(r'^api/', include(jakco_api.urls)),
    
    # Jakco Service view
    url(r'^$', 'community.views.index'),
    
    #Community Service
    url(r'^community/$', 'community.views.groupResource'),
    url(r'^community/(?P<group_id>\d+)/$', 'community.views.articleResource'),
    url(r'^community/(?P<group_id>\d+)/(?P<article_id>\d+)/$', 'community.views.articleDetailResource'),
    url(r'^community/image$', 'community.views.communityImageResource'),
    
    #Membership Service
    url(r'^membership/$', 'membership.views.memberResource'),
    url(r'^membership/(?P<user_id>\d+)/$', 'membership.views.memberDetailResource'),
    url(r'^coupon/$', 'membership.views.couponResource'),
    url(r'^coupon/(?P<coupon_id>\d+)/$', 'membership.views.couponDetailResource'),
    
    #Check-in Service
    #Check-in Service
    url(r'^checkin/$', 'checkin.views.checkinResource'),
    url(r'^checkin/(?P<user_id>\d+)/$', 'checkin.views.userCheckinResource'),
)
