from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie import fields
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie.authentication import BasicAuthentication

from django.contrib.auth.models import User
from community.models import Entry


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['password', 'is_active', 'is_staff', 'is_superuser']
        filtering = {
            'username': ALL,
        }

class EntryResource(ModelResource):
    User = fields.ForeignKey(UserResource, 'User')

    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'entry'
        excludes = ['Group']
        fields = ['User', 'Title', 'Content', 'Created', 'Comments']
        allowed_methods = ['get', 'post']
        authorization = Authorization()
        #filtering = {
        #    'User': ALL_WITH_RELATIONS,
        #    'Created': ['exact', 'lt', 'lte', 'gte', 'gt'],
        #}